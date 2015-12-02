#!/usr/bin/python

"""
Advent of Code
Day 1: Not Quite Lisp
http://adventofcode.com/day/1
"""

import sys, getopt

def main(argv):
    helpString = 'day1.py -i <inputString>'
    inputString = ''
    
    try:
        opts, args = getopt.getopt(argv,"h:i:",[])
    except getopt.GetoptError:
        print helpString
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print helpString
            sys.exit(2)
        elif opt in ('-i'):
            inputString = arg
    floor, positionEnterBasement = parseInput(inputString)
    print 'Floor ' + str(floor)
    if (positionEnterBasement == -1):
        print 'He did not enter the basement'
    else:
        print 'He entered the basement at position ' + str(positionEnterBasement)

def parseInput(inputString):
    floor = 0
    positionEnterBasement = -1
    for i, c in enumerate(inputString):
        if (c == '('):
            floor += 1
        elif (c == ')'):
            floor -= 1
        if (floor == -1 and positionEnterBasement == -1):
            positionEnterBasement = i+1
    return floor, positionEnterBasement
 
if __name__ == "__main__":
    main(sys.argv[1:])
