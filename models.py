from pydantic import BaseModel

class BookingRequest(BaseModel):
    name: str
    age: int
    flight_type: str
    seat_no: str
    payment_type: str