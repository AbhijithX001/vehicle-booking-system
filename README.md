# Vehicle Inventory & Booking System API

REST API for vehicle rental management built with Django REST Framework.

## Project Overview

Backend API system for managing vehicle inventory and bookings with automatic price calculation, validation, and double-booking prevention.

**Framework**: Django REST Framework  
**Database**: SQLite

---

## Features

- Vehicle CRUD operations
- Booking system with auto-calculated pricing
- Double-booking prevention
- Date and phone validation
- Vehicle filtering by brand, fuel type, availability
- Django admin panel

---

## Models

### Vehicle
- name, brand, year
- price_per_day (DecimalField)
- fuel_type (Petrol/Diesel/Electric/Hybrid)
- is_available (Boolean, default=True)

### Booking
- vehicle (ForeignKey)
- customer_name, customer_phone
- start_date, end_date
- total_amount (auto-calculated)
- created_at

---

## Business Rules

- No overlapping bookings for same vehicle
- total_amount = (end_date - start_date) × price_per_day
- Start date cannot be in past
- End date must be after start date
- Phone must be exactly 10 digits
- Vehicle becomes unavailable after booking

---

## Setup

### Installation

```bash
git clone https://github.com/AbhijithX001/vehicle-booking-system.git
cd vehicle-booking-system
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Access at: `http://127.0.0.1:8000/`

---

## API Endpoints

### Vehicles
- `GET /api/vehicles/` - List all
- `POST /api/vehicles/` - Create
- `GET /api/vehicles/{id}/` - Retrieve
- `PUT /api/vehicles/{id}/` - Update
- `DELETE /api/vehicles/{id}/` - Delete

### Bookings
- `GET /api/bookings/` - List all
- `POST /api/bookings/` - Create
- `GET /api/bookings/{id}/` - Retrieve

### Filtering
```
/api/vehicles/?brand=Toyota
/api/vehicles/?fuel_type=Electric
/api/vehicles/?is_available=true
```

---

## Sample Requests

### Create Vehicle
```bash
POST /api/vehicles/
Content-Type: application/json

{
    "name": "Fortuner",
    "brand": "Toyota",
    "year": 2024,
    "price_per_day": 5000,
    "fuel_type": "Diesel",
    "is_available": true
}
```

### Create Booking
```bash
POST /api/bookings/
Content-Type: application/json

{
    "vehicle": 1,
    "customer_name": "Abhijith P",
    "customer_phone": "9876543210",
    "start_date": "2026-01-05",
    "end_date": "2026-01-10"
}
```

Response includes auto-calculated `total_amount`.

---

## Testing with Postman

1. Import endpoints into Postman
2. Create vehicles using POST `/api/vehicles/`
3. Create booking using POST `/api/bookings/`
4. Test validations:
   - Past start date
   - End date before start date
   - Overlapping bookings
   - Invalid phone number (not 10 digits)
5. Verify vehicle availability changes after booking

---

## Environment Variables

Create `.env` file using `.env.example`:

```
SECRET_KEY=secret-key
DEBUG=True
DATABASE_NAME=db.sqlite3
```

---

## Project Structure

```
vehicle-booking-system/
├── vehicle_system/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── inventory/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Technologies

- Django 6.0
- Django REST Framework
- Django Filter
- SQLite

---

## Demo Video

[will add this later]

---

## Live API

[will add this later]

---

## Admin Panel

Access Django admin at: `http://127.0.0.1:8000/admin/`

Login with superuser credentials to manage vehicles and bookings.

---

## Validation Examples

### Successful Booking
```json
{
    "vehicle": 1,
    "customer_name": "Abhijith P",
    "customer_phone": "9876543210",
    "start_date": "2026-01-10",
    "end_date": "2026-01-15"
}
```

### Failed Validations

**Past date:**
```json
{
    "start_date": "2025-12-01",
    "end_date": "2026-01-05"
}
```
Error: "start date is in the past, it cannot be like that"

**Invalid phone:**
```json
{
    "customer_phone": "12345"
}
```
Error: "phone numbers must be exactly 10 digits"

**Overlapping booking:**
Error: "the vehicle is already booked, please try a diff one"

---

## Repository

https://github.com/AbhijithX001/vehicle-booking-system