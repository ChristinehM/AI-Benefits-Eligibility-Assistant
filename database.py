import sqlite3
from datetime import date


# Create the database and employees table
def create_database():
    connection = sqlite3.connect("benefits.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_name TEXT NOT NULL,
            employment_status TEXT NOT NULL,
            hours_worked INTEGER NOT NULL,
            eligibility_status TEXT NOT NULL,
            date_checked TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# Save an employee eligibility check
def save_employee(
    employee_name,
    employment_status,
    hours_worked,
    eligibility_status
):
    connection = sqlite3.connect("benefits.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO employees (
            employee_name,
            employment_status,
            hours_worked,
            eligibility_status,
            date_checked
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        employee_name,
        employment_status,
        hours_worked,
        eligibility_status,
        str(date.today())
    ))

    connection.commit()
    connection.close()


# Get all saved eligibility records
def get_employees():
    connection = sqlite3.connect("benefits.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            employee_name,
            employment_status,
            hours_worked,
            eligibility_status,
            date_checked
        FROM employees
        ORDER BY id DESC
    """)

    employees = cursor.fetchall()

    connection.close()

    return employees


# Create database when this file is imported
create_database()