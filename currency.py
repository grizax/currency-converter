#!/bin/python

rates = [("USD", "EUR", 0.86), ("EUR", "JPY", 137.05)]


def convert(rates, value, from_a, to_b):
    """Convert one currency to another using the current exchange rate"""
    if from_a == to_b:
        return value
    else:
        new_list = [(start, end, rate)
                    for (start, end, rate)
                    in rates if from_a == start]
        elput = new_list[0]
        new_rate = elput[2]
        new_value = new_rate * value
        return round(new_value, 2)
