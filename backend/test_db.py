from app.db.database import engine, Base
from app.models.trip import Trip, TripItem

if __name__ == "__main__":
    print("\n🔍 Đang kiểm tra kết nối Database...")
    print(f"🔗 URL Kết nối hiện tại: {engine.url}")

    print("🔨 Bắt đầu ép tạo bảng...")
    # Lệnh này sẽ tạo bảng ngay lập tức
    Base.metadata.create_all(bind=engine)
    print("✅ Hoàn tất tạo bảng!\n")
