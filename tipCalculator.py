#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
	tip = meal_cost * (tip_percent * .01)
	tax = meal_cost * (tax_percent * .01)
	totalCost = meal_cost + tip + tax
	print("The total meal cost is $%f dollars." % totalCost)
	return totalCost
	
if __name__ == '__main__':
	meal_cost = float(input())

	tip_percent = float(input())

	tax_percent = float(input())

	solve(meal_cost, tip_percent, tax_percent)

