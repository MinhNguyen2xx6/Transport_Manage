from sqlalchemy import Column, String, Numeric, Date, Text, DateTime, func
from sqlalchemy import Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base


class Trip(Base):
    __tablename__ = "trips"

    # Thong tin chung cua chuyen hang (Header)
    id = Column(String, primary_key=True, index=True)  # STT
    delivery_date = Column(Date, nullable=False)  # Ngay van chuyen
    truck_plate = Column(String, index=True, nullable=False)  # Bien kiem soat

    # Trang thai ke toan
    invoice_status = Column(Boolean, default=False)  # Tinh trang xuat hoa don
    payment_status = Column(Boolean, default=False)  # Tinh trang chuyen khoan

    # Relationship
    items = relationship(
        "TripItem", back_populates="trip", cascade="all, delete-orphan"
    )


class TripItem(Base):
    __tablename__ = "trip_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    trip_id = Column(String, ForeignKey("trips.id"))  # khoa ngoai lien ket voi bang

    # Chi tiet hang hoa
    item_name = Column(String, nullable=False)  # Ten hang hoa
    unit = Column(String, nullable=False)  # Don vi tinh
    quantity = Column(Numeric(10, 2), nullable=False)  # So luong
    unit_price = Column(Numeric(15, 2), nullable=False)  # Don gia

    # Thanh tien
    total_before_tax = Column(Numeric(15, 2), nullable=False)  # Thanh tien truoc thue
    total_after_tax = Column(Numeric(15, 2), nullable=False)  # Thanh tien sau thue

    trip = relationship("Trip", back_populates="items")
