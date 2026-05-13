# app/services/trip_service.py
from decimal import Decimal
from sqlalchemy.orm import Session
from datetime import datetime
from app.models.trip import Trip, TripItem


class TripService:
    # Vẫn giữ lại các hàm tính toán này phòng trường hợp bạn cần dùng cho các API thống kê sau này
    @staticmethod
    def calculate_gross_profit(
        freight_revenue: Decimal, vendor_cost: Decimal
    ) -> Decimal:
        return freight_revenue - vendor_cost

    @staticmethod
    def calculate_remaining_debt(
        vendor_cost: Decimal, advance_payment: Decimal
    ) -> Decimal:
        return vendor_cost - advance_payment

    @classmethod
    def generate_trip_id(cls, db: Session) -> str:
        """
        Generates a sequential Trip ID automatically, e.g., TM-2026-0001
        """
        year = datetime.now().year
        count = db.query(Trip).filter(Trip.id.like(f"TM-{year}-%")).count()
        return f"TM-{year}-{count + 1:04d}"

    @classmethod
    def create_trip(cls, db: Session, trip_data) -> Trip:
        """
        Handles the core business logic for creating a new dispatch order and its items.
        """
        # 1. Tạo ID tự động cho chuyến xe
        new_trip_id = cls.generate_trip_id(db)

        # 2. Tạo phần Header của chuyến xe (thông tin chung)
        new_trip = Trip(
            id=new_trip_id,
            delivery_date=trip_data.delivery_date,
            truck_plate=trip_data.truck_plate,
            invoice_status=trip_data.invoice_status,
            payment_status=trip_data.payment_status,
        )

        # Thêm chuyến xe vào session và 'flush' để lấy ID (nhưng chưa commit chính thức)
        db.add(new_trip)
        db.flush()

        # 3. Khai báo mức thuế VAT (Mặc định 8%)
        VAT_RATE = Decimal("0.08")

        # 4. Duyệt qua danh sách các mặt hàng người dùng gửi lên
        for item_data in trip_data.items:

            # Tự động tính toán Thành tiền trước thuế và sau thuế
            thanh_tien_truoc_thue = item_data.quantity * item_data.unit_price
            tien_thue = thanh_tien_truoc_thue * VAT_RATE
            thanh_tien_sau_thue = thanh_tien_truoc_thue + tien_thue

            # Tạo bản ghi chi tiết hàng hóa (liên kết với chuyến xe qua trip_id)
            new_item = TripItem(
                trip_id=new_trip_id,
                item_name=item_data.item_name,
                unit=item_data.unit,
                quantity=item_data.quantity,
                unit_price=item_data.unit_price,
                total_before_tax=thanh_tien_truoc_thue,
                total_after_tax=thanh_tien_sau_thue,
            )
            db.add(new_item)

        # 5. Lưu toàn bộ (Chuyến xe + Tất cả mặt hàng) vào Database PostgreSQL
        db.commit()
        db.refresh(new_trip)

        return new_trip
