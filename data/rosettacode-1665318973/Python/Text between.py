#!/usr/bin/env python
from sys import argv

# textBetween in python
# Get the text between two delimiters
# Usage:
# python textBetween.py "hello Rosetta Code world" "hello " " world"

def textBetween( thisText, startString, endString ):
    try:
    	if startString is 'start':
    		startIndex = 0
    	else:
    		startIndex = thisText.index( startString ) 
    	
    	if not (startIndex >= 0):
    		return 'Start delimiter not found'
    	else:
        	if startString is not 'start':
        		startIndex = startIndex + len( startString )
        
        returnText = thisText[startIndex:]


    	if endString is 'end':
    		return returnText
    	else:
    		endIndex = returnText.index( endString )

    	if not (endIndex >= 0):
    		return 'End delimiter not found'
    	else:
        	returnText = returnText[:endIndex]

        return returnText
    except ValueError:
        return "Value error"

script, first, second, third = argv

thisText = first
startString = second
endString = third

print textBetween( thisText, startString, endString )