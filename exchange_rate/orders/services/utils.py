
from datetime import datetime


def convert_date_format(date: str) -> str:
    dt = datetime.strptime(date, "%d.%m.%Y")
    return dt.strftime('%Y-%m-%d')



    