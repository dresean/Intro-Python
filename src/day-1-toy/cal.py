# Use the 'calendar' module to draw calendars to the console
# https://docs.python.org/3.6/library/calendar.html
#
# Use the sys module to look for command line arguments in the `argv` list
# variable.
# import sys
# import calendar
# cal = calendar.



#   if len(sys.arv) == 2 :
#     cal.print
#     month = input('Enter a year: ')
#     year = input('Enter a month: ')
#   if sys.argv[1] and sys.argv[2]
# """
# ask for a month and year separated by commas
# check system arguments as of now
# not the path to the file but the other ones, all of them.
# if there are a month and year,  
# draw the calendar for a month
# if nothing inputed into the command line
# draw todays month calendar
# """

# def calendar_generator(month, year):

# #
# If the user specifies two command line arguments, month and year, then draw
# the calendar for that month.

# Stretch goal: if the user doesn't specify anything on the command line, show
# the calendar for the current month. See the 'datetime' module.

# Hint: this should be about 15 lines of code. No loops are required. Read the
# docs for the calendar module closely.
#cheated again lol
import sys
import calendar

# Parse command line
l = len(sys.argv)

if l == 2:
    month = None
    year = int(sys.argv[1])
elif l == 3:
    month = int(sys.argv[1])
    year = int(sys.argv[2])
else:
    print("usage: cal.py [month] year")
    sys.exit(1)

# Make a new calendar
c = calendar.TextCalendar()

if month != None:
    # If the user specified a month, print that month
    c.prmonth(year, month)
else:
    # Otherwise just print it for the year
    c.pryear(year)