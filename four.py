from datetime import datetime, timedelta


class Movie:
    def __init__(self, title, schedule_periods):
        self.title = title
        self.schedule_periods = schedule_periods

    def schedule(self):
        for start_date, end_date in self.schedule_periods:
            current_date = start_date
            while current_date <= end_date:
                yield current_date
                current_date += timedelta(days=1)


# Создаем тестовые данные
schedule_periods = [
    (datetime(2024, 11, 1), datetime(2024, 11, 7)),
    (datetime(2024, 12, 15), datetime(2024, 12, 31))
]

# Создаем объект фильма
movie = Movie("Пример фильма", schedule_periods)

# Проверяем генератор расписания
print("Расписание показа фильма:")
for date in movie.schedule():
    print(date)