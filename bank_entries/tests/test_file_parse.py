from collections.abc import Iterator
from datetime import datetime

from bank_entries.bank_entries import _read_log
from bank_entries.tests.datetimes_mixin import DatetimesMixin
from bank_entries.tests.file_test_case import FileTestCase


class FileParseTest(DatetimesMixin, FileTestCase):
    def setUp(self) -> None:
        data = (
            f'{date.strftime("%Y-%m-%d %H:%M:%S")} - Abertura da Porta OK'
            for date in self.datetimes
        )
        with open(self.filename, 'w') as file_:
            file_.write('\n'.join(data))

    def test_read_log_exists(self):
        self.assertTrue(callable(_read_log))

    def test_read_log_iterator(self):
        self.assertIsInstance(_read_log(self.filename), Iterator)

    def test_datetimes_length(self):
        self.assertEqual(len(list(_read_log(self.filename))), len(self.datetimes))

    def test_read_log_is_datetime(self):
        for i, date in enumerate(_read_log(self.filename)):
            self.assertIsInstance(date, datetime)
            self.assertEqual(date, self.datetimes[i])
