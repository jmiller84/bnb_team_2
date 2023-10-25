import calendar
from datetime import date

current_year = date.today().year
current_month = date.today().month
str_month = date.today().strftime("%B")

cal = calendar.Calendar(firstweekday=0).monthdatescalendar(current_year,current_month)


