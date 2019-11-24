from datetime import datetime

BUSINESS_START = 10
BUSINESS_STOP = 16


def _read_log(filename: str):
    with open(filename, 'r') as file_:
        line = file_.readline()
        while line:
            yield datetime.strptime(
                line.split(' - ')[0],
                '%Y-%m-%d %H:%M:%S'
            )
            line = file_.readline()


def _is_business(datetime_: datetime):
    if BUSINESS_START <= datetime_.hour < BUSINESS_STOP:
        return True

    if datetime_.hour == BUSINESS_STOP:
        return datetime_.minute == 0 and datetime_.second == 0

    return False


def get_people_entered(filename: str):
    total_people = 0
    for datetime_ in _read_log(filename):
        if _is_business(datetime_):
            total_people += 1
    return total_people
