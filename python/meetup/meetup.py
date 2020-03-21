from calendar import Calendar

def meetup_day(year, month, day, which):
    all_days = [date for date in Calendar().itermonthdates(year, month) if date.month == month if date.strftime('%A') == day]
    for d in all_days:
        if which == 'teenth' and 12 < d.day < 20:
            return d
    if which == 'last':
        return all_days[-1]
    elif int(which[0]) > len(all_days):
        raise MeetupDayException()
    else:
        return all_days[int(which[0])-1]


class MeetupDayException(Exception):
    def __init__(self):
            self.message = 'Incorrect input values'

    def __str__(self):
        return repr(self.message)

