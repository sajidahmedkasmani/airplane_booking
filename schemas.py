from pydantic import BaseModel

class UserRegister(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str

class BookingCreate(BaseModel):
    passenger_name: str
    seat_no: str