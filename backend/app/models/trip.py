from sqlalchemy import Column, String, Numeric, DateTime, func
from app.db.base_class import Base


class Trip(Base):
    __tablename__ = "trips"

    id = Column(String(50), primary_key=True, index=True)
    truck_plate = Column(String(20), nullable=False, index=True)
    driver_name = Column(String(100), nullable=True)
    status = Column(String(50), default="PENDING")  # PENDING, IN_PROGRESS, COMPLETED

    advance_payment = Column(Numeric(15, 2), default=0)
    freight_revenue = Column(Numeric(15, 2), default=0)
    vendor_cost = Column(Numeric(15, 2), default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
