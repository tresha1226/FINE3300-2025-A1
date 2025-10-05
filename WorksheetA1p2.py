print("testing")
# Question 2: Exchange Rates
# In this part of the assignment, data from an excel file (csv format) called "BankOfCanadaExchangeRates" is pulled to convert $100,000 USD to CAD, and vice versa.

import csv

# opening the Bank of Canada Exchange Rates file and reading its contents
with open("BankOfCanadaExchangeRates.csv", newline="") as f:
    reader = csv.DictReader(f)
    latest_rate = float(list(reader)[-1]["USD/CAD"])

# defining a function that converts the currencies (USD and CAD)
def convert(amount, frm, to):
    if frm == "USD" and to == "CAD":
        return amount * latest_rate
    elif frm == "CAD" and to == "USD":
        return amount / latest_rate
    else:
        return 0

# prompting the user to enter the amount for conversion
amount = float(input("Enter the $ Amount: "))
frm = input("From (USD or CAD): ").upper()
to = input("To (USD or CAD): ").upper()

converted = convert(amount, frm, to)
print(f"{amount} {frm} is equal to {converted:.2f} {to}")