from unittest import TestCase

from bank_entries.bank_entries import _is_business
from bank_entries.tests.datetimes_mixin import DatetimesMixin


class IsBusinessTest(DatetimesMixin, TestCase):
    def test_is_business(self):
        datetimes_business = [
            False,
            True,
            True,
            True,
            False,
            False
        ]

        for datetime_, is_business in zip(self.datetimes, datetimes_business):
            with self.subTest():
                self.assertEqual(_is_business(datetime_), is_business)
