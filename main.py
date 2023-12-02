"""
В модулі функція, яка визначає співробітників-іменинників протягом тижня.
"""
from datetime import date, datetime, timedelta


def get_birthdays_per_week(input_users):
    """
    Функція визначає список співробітників, які святкують день народження протягом тижня.

    Args:
    input_users (list): Список співробітників у форматі {"name": str, "birthday": date}.

    Returns:
    dict: Словник із списками співробітників-іменинників.
    """
    if not input_users:
        return {}

    today = date.today()
    # Якщо сьогодні понеділок, то починаємо відлік з минулої суботи (-2 дні)
    if today.weekday() == 0:
        today -= timedelta(days=2)
    elif today.weekday() == 6:
        today -= timedelta(days=1)

    birthdays_per_week = {
        'Monday': [], 'Tuesday': [], 'Wednesday': [],
        'Thursday': [], 'Friday': []
    }

    for i in range(7):

        current_date = today + timedelta(days=i)
        for user in input_users:
            birthday_date = user['birthday']
            if current_date.day == birthday_date.day and current_date.month == birthday_date.month:
                day_week = current_date.strftime('%A')
                if day_week in ('Saturday', 'Sunday'):
                    day_week = 'Monday'

                birthdays_per_week[day_week].append(user['name'])

    # Видаляємо дні з порожніми списками
    birthdays_per_week = {day: names for day, names in birthdays_per_week.items() if names}

    return birthdays_per_week


if __name__ == '__main__':

    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
