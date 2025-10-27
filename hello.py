import datetime


def say_hello(name: str) -> None:
    """Prints a greeting message."""
    print(f"Hello, {name}")


def say_day_of_week(today: datetime.date) -> None:
    """Prints the current day of the week and date."""
    print(f"Today is {today.strftime('%A, %B %d, %Y')}")


if __name__ == "__main__":
    say_hello("VS Code")
    say_day_of_week(datetime.date.today())