from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from datetime import date
from typing import List


# Schema cho tung mat hang (TripTtem)
class TripItemBase(BaseModel):
    item_name: str
    unit: str
    quantity: Decimal
    unit_price: Decimal


class TripItemCreate(TripItemBase):
    pass  # User goi len 4 truong co ban tren


class TripItemResponse(TripItemBase):
    id: int
    total_before_tax: Decimal
    total_after_tax: Decimal
    model_config = ConfigDict(from_attributes=True)


# Schema cho chuyen xe
class TripBase(BaseModel):
    delivery_date: date
    truck_plate: str
    invoice_status: bool = False
    payment_status: bool = False


class TripCreate(TripBase):
    items: List[TripItemCreate]


class TripResponse(TripBase):
    id: str
    items: List[TripItemResponse]  # Khi tra ve thi tra chi tiet cac mat hang
    model_config = ConfigDict(from_attributes=True)
