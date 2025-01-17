def life_in_weeks(age):
    remaining_age = 90 - age
    days_in_year =  365
    days_left =  remaining_age * days_in_year
    weeks_left = days_left/7
    print(f"You have {round(weeks_left)} weeks left.")

life_in_weeks(56)