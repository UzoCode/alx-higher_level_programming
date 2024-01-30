#!/usr/bin/python3

def safe_print_division(a, b):
	try:
		dive = a / b
	except (ValueError, TypeError, ZeroDivisionError):
		dive = None
	finally:
		print("Inside result: {}".format(dive))
	return dive
	
