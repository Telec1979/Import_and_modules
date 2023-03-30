import application.salary as salary
import application.db.people as people
from datetime import date

if __name__ == '__main__':
    today = date.today()
    n = input('Name:')
    salary.calculate_salary(n, today)
    people.get_employees(today)

