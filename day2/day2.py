#!/usr/bin/python

"""
Advent of Code
Day 2: I Was Told There Would Be No Math
http://adventofcode.com/day/2
"""

import sys, getopt

def main(argv):
    helpString = 'day1.py -i <inputFile>'
    inputFile = ''
    
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
            inputFile = arg
	f = open(inputFile, 'r')
	totalPaper,totalRibbon = parseFile(f)
	print "Paper: " + str(totalPaper)
	print "Ribbon: " + str(totalRibbon)
	
def parseFile(f):
	totalFeetPaper = 0
	totalFeetRibbon = 0
	for line in f:
		l,w,h = extractNumbers(line)
		totalFeetPaper = totalFeetPaper + (2*l*w + 2*w*h + 2*h*l + getSmallestSide(l*w,w*h,h*l))
		totalFeetRibbon = totalFeetRibbon + (getSmallestPerimeter(l,w,h) + getVolume(l,w,h))
	return totalFeetPaper, totalFeetRibbon
	
def extractNumbers(s):
	return [int(n) for n in s.split('x')]

def getSmallestSide(l,w,h):
    return min(int(n) for n in [l,w,h])

def getSmallestPerimeter(l,w,h):
	n = sorted([l,w,h])
	return (n[0]*2) + (n[1]*2)

def getVolume(l,w,h):
	return l*w*h

if __name__ == "__main__":
    main(sys.argv[1:])
