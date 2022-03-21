import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
from user_interface import UI


class RealTimeCurrencyConverter():
    def __init__(self, url):
        self.date = requests.get(url).json()
        self.currencies = self.date['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        # first convert to USD if not in USD. This is required because the base currency is USD
        if from_currency != 'USD':
            amount = round(initial_amount / self.currencies[from_currency], 4)

        return amount


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)

    UI(converter)
    mainloop()
