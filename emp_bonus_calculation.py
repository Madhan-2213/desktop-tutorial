def calculate_bonus(experience):
    if experience > 8:
        return 10
    elif experience > 4:
        return 7
    elif experience > 2:
        return 4
    else:
        return 0

def calculate_charge(units):
    if units <= 100:
        return 0
    elif units <= 200:
        return (units - 100) * 5
    else:
        return (units - 200) * 10 + 100 * 5

def calculate_total_salary(experience, units):
    bonus_percentage = calculate_bonus(experience)
    bonus_amount = units * bonus_percentage / 100
    charge = calculate_charge(units)
    total_salary = units + bonus_amount - charge
    return total_salary

experience = 6
units = 250
total_salary = calculate_total_salary(experience, units)
print("Total Salary:", total_salary)
