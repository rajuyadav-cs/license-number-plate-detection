# IntelliPlate - Automatic Number Plate Recognition System

## Overview

IntelliPlate is a Django-based Automatic Number Plate Recognition (ANPR) system that detects vehicle license plates using a custom-trained YOLO model and extracts plate text using OCR.

The system provides a complete workflow for plate detection, result visualization, history tracking, dashboard analytics, and PostgreSQL data storage.

---

## Features

* License Plate Detection using YOLO
* OCR-based Plate Text Recognition
* Image Upload Interface
* Detection Confidence Score
* Plate Crop Extraction
* Detection History Management
* Detailed Detection View
* Dashboard Analytics
* Search Functionality
* Date-based Filtering
* Pagination Support
* PostgreSQL Integration
* Responsive Tailwind CSS Interface

---

## Tech Stack

### Backend

* Django
* PostgreSQL
* OpenCV
* Ultralytics YOLO
* EasyOCR

### Frontend

* HTML
* Tailwind CSS

### Database

* PostgreSQL

---

## Project Structure

```text
intelliplate/
│
├── dashboard/
├── detection/
├── vehicles/
├── templates/
├── static/
├── media/
├── ml_models/
└── manage.py
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/intelliplate.git
cd intelliplate
```

### Create Virtual Environment

```bash
python -m venv .env
```

### Activate Environment

Windows:

```bash
.env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Setup

Update PostgreSQL credentials inside:

```text
intelliplate/settings.py
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Run Project

```bash
python manage.py runserver
```

---

## Model Setup

Place the trained YOLO model inside:

```text
ml_models/
└── licence_plate_detection.pt
```

Model files are excluded from the repository because of their large size.

---

## Screenshots

Add screenshots of:

* Home Page
* Detection Page
* Detection Results
* Dashboard
* Detection History

---

## Future Improvements

* Real-Time Camera Detection
* Advanced OCR Pipeline
* Vehicle Analytics
* Export Reports
* User Authentication

---

## Author

Raju Yadav

Built as a portfolio project to demonstrate Computer Vision, Deep Learning, Django, PostgreSQL, and Full Stack Development skills.
