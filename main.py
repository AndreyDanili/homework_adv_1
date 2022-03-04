from application import salary
from application.db import people
import datetime


def main():
    date_now = datetime.date.today()
    print(date_now)


if __name__ == '__main__':
    example_one = salary.calculate_salary()
    example_two = people.get_employees()
    main()
