import streamlit as st
import pandas as pd

from eligibility import check_eligibility
from database import save_employee, get_employees


# Page title
st.title("Employee Health Benefits Eligibility")

st.write(
    "This application checks whether an employee qualifies "
    "for health benefits based on employment status and hours worked."
)


# Employee information
employee_name = st.text_input("Employee Name")

employment_status = st.selectbox(
    "Employment Status",
    ["Active", "Inactive"]
)

hours_worked = st.number_input(
    "Total Hours Worked",
    min_value=0,
    max_value=5000,
    value=0,
    step=1
)


# Eligibility requirement
required_hours = 400

st.write(f"Eligibility requirement: **{required_hours} hours**")


# Check eligibility
if st.button("Check Eligibility"):

    status = check_eligibility(
        hours_worked,
        employment_status
    )

    hours_remaining = max(
        required_hours - hours_worked,
        0
    )

    # Create explanation
    if status == "Eligible for Health Benefits":

        explanation = (
            f"{employee_name or 'Employee'} is actively employed "
            f"and has reached the required {required_hours} hours."
        )

    elif employment_status == "Inactive":

        explanation = (
            f"{employee_name or 'Employee'} is currently inactive."
        )

    else:

        hour_word = "hour" if hours_remaining == 1 else "hours"

        explanation = (
            f"{employee_name or 'Employee'} needs "
            f"{hours_remaining} more {hour_word} to qualify."
        )

    # Save result to database
    save_employee(
        employee_name or "Not provided",
        employment_status,
        hours_worked,
        status
    )

    # Display result
    st.subheader("Eligibility Summary")

    st.write(f"**Employee:** {employee_name or 'Not provided'}")
    st.write(f"**Employment Status:** {employment_status}")
    st.write(f"**Hours Worked:** {hours_worked}")
    st.write(f"**Required Hours:** {required_hours}")
    st.write(f"**Hours Remaining:** {hours_remaining}")

    if status == "Eligible for Health Benefits":
        st.success(status)
    else:
        st.error(status)

    st.write(explanation)


# Eligibility history
st.divider()

st.subheader("Eligibility History")

employees = get_employees()

if employees:

    df = pd.DataFrame(
        employees,
        columns=[
            "Employee",
            "Employment Status",
            "Hours Worked",
            "Eligibility Status",
            "Date Checked"
        ]
    )

    st.dataframe(
        df,
        hide_index=True,
        use_container_width=True
    )

else:
    st.info("No eligibility records found.")