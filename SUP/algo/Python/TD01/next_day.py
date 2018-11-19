def leap(y):
    """Tests whether the year is leap."""
    return (y % 4 == 0) and ((y % 100 != 0) or (y % 400 == 0))

def nb_days(m, y):
    """Number of days in a month."""
    if m == 2:
        return 28 + leap(y)
    else:
        return 30 + (m % 7) % 2 + (m == 7)
    
def valid_date(d, m, y):
    """Tests whether date is valid."""
    return (0 < m and m < 13) and (0 < d <= nb_days(m, y))

def next_day(d, m, y):
    """Computes next day's date."""
    nbdays = nb_days(m, y)
    d = (d % nbdays) + 1
    if d == 1:
        m = (m % 12) + 1
        if m == 1:
            y = y + 1
    return d, m, y 

# main 
d = int(input("Give me a date, days to start : "))
m = int(input("Next is month : "))
y = int(input("What year?"))

if not valid_date(d, m, y):
    raise Exception("Date is note valid.")
else:   
    print("Date of next day is : ", next_day(d, m, y))