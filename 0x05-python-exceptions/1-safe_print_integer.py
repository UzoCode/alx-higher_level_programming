#!/usr/bin/python3

def safe_print_integer(value):
	Integer = False
	try:
		print("{:d}".format(value))
		Integer = True
	except ValueError:
		Integer = False
	finally:
		return Integer
