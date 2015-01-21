#!/bin/python
import currency as cy

rates = [("USD", "EUR", 0.86), ("EUR", "JPY", 137.05)]


def test_dollar_for_dollar():
    assert cy.convert(rates, 1, "USD", "USD") == 1


def test_conversion():
    assert cy.convert(rates, 1, "USD", "EUR") == .86


def test_converting_more():
    assert cy.convert(rates, 444, "EUR", "JPY") == 60850.2
