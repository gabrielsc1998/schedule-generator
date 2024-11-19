import unittest
from datetime import date

from ..helpers import ScheduleHelpers


class TestScheduleHelpers(unittest.TestCase):

    def test_no_sundays_between_dates(self):
        start_date = date(2023, 10, 2)  # Monday
        end_date = date(2023, 10, 7)    # Saturday
        result = ScheduleHelpers.get_all_sundays_between_dates(start_date, end_date)
        self.assertEqual(result, [])

    def test_one_sunday_between_dates(self):
        start_date = date(2023, 10, 1)  # Sunday
        end_date = date(2023, 10, 8)    # Next Sunday
        result = ScheduleHelpers.get_all_sundays_between_dates(start_date, end_date)
        self.assertEqual(result, [date(2023, 10, 1), date(2023, 10, 8)])

    def test_multiple_sundays_between_dates(self):
        start_date = date(2023, 10, 1)  # Sunday
        end_date = date(2023, 10, 22)   # Three Sundays later
        result = ScheduleHelpers.get_all_sundays_between_dates(start_date, end_date)
        self.assertEqual(result, [date(2023, 10, 1), date(2023, 10, 8), date(2023, 10, 15), date(2023, 10, 22)])

    def test_start_date_is_sunday(self):
        start_date = date(2023, 10, 1)  # Sunday
        end_date = date(2023, 10, 2)    # Monday
        result = ScheduleHelpers.get_all_sundays_between_dates(start_date, end_date)
        self.assertEqual(result, [date(2023, 10, 1)])

    def test_end_date_is_sunday(self):
        start_date = date(2023, 9, 25)  # Monday
        end_date = date(2023, 10, 1)    # Sunday
        result = ScheduleHelpers.get_all_sundays_between_dates(start_date, end_date)
        self.assertEqual(result, [date(2023, 10, 1)])
