#!/usr/bin/python
import sys

''' Difference between two dates = g(y2,m2,d2) - g(y1,m1,d1) 
    Where g() gives us the Gregorian Calendar Day
    Inspired  by discussion at:
    https://stackoverflow.com/questions/12862226/the-implementation-of-calculating-the-number-of-days-between-2-dates
'''

def days( y,m,d ):
  ''' input year and month are shifted to begin the year in march'''
  m = (m + 9) % 12 
  y = y - m/10

  ''' with (m*306 + 5)/10 the number of days from march 1 to the current 'm' month '''
  result = 365*y + y/4 - y/100 + y/400 + (m*306 + 5)/10 + ( d - 1 )
  return result

def diff(one,two):
  [y1,m1,d1] = one.split('-')
  [y2,m2,d2] = two.split('-')
  # strings to integers
  year2 = days( int(y2),int(m2),int(d2))
  year1 = days( int(y1), int(m1), int(d1) )
  return year2 - year1

if __name__ == "__main__":
  one = sys.argv[1]
  two = sys.argv[2]
  print diff(one,two)