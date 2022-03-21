import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk


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


class UI(tk.Tk):
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = 'Currency Converter'
        self.currency_converter = converter

        self.geometry("500x200")

        # Label
        self.intro_label = Label(
            self, text="Welcome to Jake's Currency Converter, It's Real time!", fg='blue', relief=tk.RAISED, borderwidth=3)
        self.intro_label.config(font=('Courier', 15, 'bold'))

        self.date_label = Label(
            self, text=f"1 Indian Rupee equals = {self.currency_converter.convert('INR', 'USD', 1)} USD \n Date : {self.currency_converter.date['date']}", relief=tk.GROOVE, borderwidth=5)

        self.intro_label.place(x=10, y=5)
        self.date_label.place(x=170, y=50)

        self.date_label.place(x=170, y=50)


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)

    UI(converter)
    mainloop()
