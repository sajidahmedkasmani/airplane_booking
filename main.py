from fastapi import FastAPI
# from fastapi import FastAPI.TemplateResponse
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from schemas import BookingCreate
import sqlite3
    
app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home():
    # return templates.TemplateResponse(
    #     "index.html",
    #     {"request": request}
    # )
    return FileResponse("templates/index.html")


@app.get("/seats")
def get_seats():

    conn = sqlite3.connect("aeroplane.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM flights
    """)

    seats = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return seats


@app.post("/book-seat")
def book_seat(data: BookingCreate):

    conn = sqlite3.connect("aeroplane.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM flights
        WHERE seat_no = ?
    """, (data.seat_no,))

    seat = cursor.fetchone()

    if not seat:
        conn.close()
        return {"error": "Seat not found"}

    cursor.execute("""
        INSERT INTO bookings(passenger_name, seat_no, cnic, dob, phone, email, cabin, meal)
        VALUES(?, ?)
    """, (data.passenger_name, data.seat_no, data.cnic, data.dob, data.phone, data.email, data.cabin, data.meal))

    cursor.execute("""
        UPDATE flights
        SET is_booked = 1
        WHERE seat_no = ?
    """, (data.seat_no,))

    conn.commit()
    conn.close()

    return {
        "message": "Seat booked successfully"
    }