from pprint import pprint
from faker import Faker
from datetime import date

fake = Faker()
Faker.seed(0)
birthdays=[]
def get_user_birthdays(n):
    user = []
    for _ in range(n):
        name = fake.name()
        birthday = date(2023,3, int(fake.day_of_month()))
        user.append({'name': name, 'birthday': str(birthday)})
    return user


if __name__=='__main__':
    pprint(get_user_birthdays(100))