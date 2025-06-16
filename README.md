# Car Rental Management System

## Overview

This project is a **Car Rental Management System**, designed as a web-based application for car rental agencies and their customers. The system allows users to book cars online, while enabling agencies to efficiently manage bookings, customers, and their fleet. It aims to modernize traditional booking processes, reduce paperwork, and make car rentals accessible and streamlined via an online platform.

## Features

- **Online Car Booking**: Customers can view available cars, register, view their profiles, and book cars online.
- **Admin Panel**: Administrators can manage bookings, confirm or cancel reservations based on car and driver availability, and track all customer and car records.
- **Partner Integration**: Car owners can register their vehicles with the agency to be included in the pool of rentable cars.
- **User Management**: Both customers and car owners can maintain and update their profiles.
- **Interactive UI**: The system uses modern UI elements like carousels, animated navigation, parallax backgrounds, and pop-up galleries for a smooth user experience.
- **Booking Tracking**: Customers and administrators can track booking statuses in real time.
- **Responsive Design**: The frontend adapts to mobile devices and desktops for ease of use.

## How It Works

1. **For Customers**:
   - Browse available cars and view details.
   - Register and log in to book a car.
   - Manage their profile and view current/past bookings.

2. **For Car Owners/Partners**:
   - Register their vehicles with the agency to offer them for bookings.
   - Track the status of their vehicle rentals.

3. **For Admins**:
   - Manage the fleet, bookings, and customer details.
   - Confirm or cancel bookings.
   - Monitor system usage and generate reports.

## Technologies Used

- **Frontend**: HTML, CSS (SCSS), JavaScript (jQuery, Bootstrap, OwlCarousel, MagnificPopup, Scrollax, AOS, Chart.js)
- **Templates**: HTML (for user and admin pages)
- **Backend**: (Likely Python/Django or similar, inferred from directory structure, but not visible in this code snapshot)
- **Admin Dashboard**: Enhanced with charts and interactive elements for data visualization.

## Why Use This System?

> "It is useful for car booking agencies that are specialized in hiring cabs to customers. Using this system, many car-booking agencies are moving ahead to become pioneers in the vehicle rental industry by completely focusing on customers. Using this system it is very easy for customers to book a car online and for car-booking agencies to track their booking online. So it is also very useful for car booking agencies. It is an online system through which customers can view available cabs, register the cabs, view profiles, and book cabs. Most people use cab service for their daily transportation needs. It will simplify the task and reduce the paperwork. Using this car booking management system, car owners can also become partners of car booking agencies by giving their cars for booking. Online Car Rental Management System is a web-based application that allows users to book a car online. From this system, car rental companies can manage all car bookings and customer information. Users can book cars and admin can confirm or cancel bookings on the basis of the availability of cars and drivers."
>

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/No-one9/carRental.git
   ```
2. **Install dependencies** (see backend framework requirements or `requirements.txt` if available).
3. **Run database migrations** (if using Django or similar backend).
4. **Start the development server**:
   ```
   python manage.py runserver
   ```
5. **Access the application**: Open your browser and go to `http://localhost:8000/`

## Project Structure

- `CarRentalApp/templates/`: HTML templates for user and admin interfaces.
- `CarRentalApp/static/`: Static files (CSS, JS, images) used in the frontend.
- `CarRentalApp/static/js/main.js`: Core frontend functionality, animations, and navigation.
- `CarRentalApp/static/admin/`: Admin dashboard assets, plugins, and scripts.
- `CarRentalApp/static/scss/`: SCSS source files for custom styles.

## License

This project is for educational/demo purposes. Please check the repository for a license file or contact the owner for usage details.

---

