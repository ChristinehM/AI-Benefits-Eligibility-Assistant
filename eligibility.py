

def check_eligibility(hours_worked, employment_status):
    if employment_status.lower() != "active":
        return "Not Eligible - Employee is not actively employed"

    if hours_worked >= 400:
        return "Eligible for Health Benefits"

    hours_remaining = 400 - hours_worked

    if hours_remaining == 1:
        return "Not Eligible - 1 hour remaining"

    return f"Not Eligible - {hours_remaining} hours remaining"

