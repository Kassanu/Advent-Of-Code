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
    outputString = ''
    
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
    print 'Floor ' + parseInput(inputString)

def parseInput(inputString):
    floor = 0
    for c in inputString:
        if (c == '('):
            floor += 1
        elif (c == ')'):
            floor -= 1
    return str(floor)
 
if __name__ == "__main__":
    main(sys.argv[1:])
