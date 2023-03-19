from datetime import  datetime, timedelta, date
from collections import defaultdict
from pprint import pprint
from data import get_user_birthdays


def get_next_week_start(d:datetime):
    diff_days = 6 - d.weekday()
    return d + timedelta(days=diff_days)

def prepare_birthaday(text: str):
    try:
        bd =  datetime.strptime(text, '%d-%m-%Y')
    except ValueError:
        if text == '29-02-2023':
            bd = datetime(2023,3,1)

    return bd.replace().date()

def get_birthdays_per_week(users):
    birthdays = defaultdict(list)

    # today = datetime.now().date()

    today = datetime(2023,2,26).date()

    next_week_start = get_next_week_start(today)
    start_period = next_week_start - timedelta(2)
    end_period = next_week_start + timedelta(4)

    happy_users = [user for user in users if start_period <= prepare_birthaday(user['birthday']) <= end_period]

    for user in happy_users:
        curent_bd: date = prepare_birthaday(user['birthday'])
        if curent_bd.weekday() in(5,6):
            birthdays['Monday'].append(user['name'])
        else:
            birthdays[curent_bd.strftime('%A')].append(user['name'])
    
    return birthdays


if __name__=="__main__":
    pprint(get_birthdays_per_week(get_user_birthdays))