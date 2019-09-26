from datetime import datetime

def get_time():
    return datetime.now()


def format_datetime(date: datetime, format_str: str):
    return date.strftime(format_str)