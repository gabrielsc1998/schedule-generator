from typing import List
from datetime import date, timedelta


class ScheduleHelpers:

    @staticmethod
    def get_all_sundays_between_dates(start_date: date, end_date: date) -> List[date]:
        all_sundays = []
        days_between_dates = (end_date - start_date).days + 1
        for n in range(days_between_dates):
            date = start_date + timedelta(days=n)
            if date.weekday() == 6:
                all_sundays.append(date)
        return all_sundays
