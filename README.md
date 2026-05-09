# Hospital Management System

A terminal-based hospital management system built in Python for a university OOP project demonstrating inheritance and encapsulation.

## Features
- Register patients and doctors with auto-generated IDs
- Book and cancel appointments matched by doctor specialization
- Display all patients, doctors, and appointments
- Save and load data from local text files
- Reset all data
- Duplicate detection on registration

## OOP Concepts
- **Inheritance** — `Patient` and `Doctor` inherit from `Person`
- **Encapsulation** — Patient IDs are private, accessible only via `get_id()`

## How to Run
```bash
python main.py
```

## Data Storage
Records saved as `|` separated values. Example: `Ahmad|20|P0001`

## Author
Adil — BS Software Engineering