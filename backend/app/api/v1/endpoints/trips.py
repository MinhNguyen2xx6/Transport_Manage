from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.trip_schema import TripCreate, TripResponse
from app.services.trip_service import TripService

router = APIRouter()


@router.post("/", response_model=TripResponse)
def create_new_trip(trip_in: TripCreate, db: Session = Depends(get_db)):
    """
    API: Create new trip
    """
    try:

        new_trip = TripService.create_trip(db=db, trip_data=trip_in)
        return new_trip
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Can not create new trip !!!: {str(e)}"
        )
