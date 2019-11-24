from bank_entries.bank_entries import get_people_entered
from bank_entries.tests.datetimes_mixin import DatetimesMixin
from bank_entries.tests.file_test_case import FileTestCase


class PeopleEnteredTest(DatetimesMixin, FileTestCase):
    def test_get_people_entered_exists(self) -> None:
        self.assertTrue(callable(get_people_entered))

    def test_how_many_entered(self) -> None:
        data = (
            f'{date.strftime("%Y-%m-%d %H:%M:%S")} - Abertura da Porta OK'
            for date in self.datetimes
        )
        with open(self.filename, 'w') as file_:
            file_.write('\n'.join(data))

        self.assertEqual(get_people_entered(self.filename), 3)
