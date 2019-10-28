"""
Currency Conversion with Matrix Multiplication

Over the years you have traveled to eight different countries and just happen to have leftover local currency from
each of your trips. You are planning to return to one of the eight countries, but you aren't sure which one just yet.
You are waiting to find out which will have the cheapest airfare. In preparation, for the trip you will want convert
all your local currency into the currency local of the place you will be traveling to. Therefore, to double check the
bank's conversion of your currency, you want to compute the total amount of currency you would expect for each of the
eight countries. To compute the conversion you first need to import a matrix that contains the currency conversion
rates for each of the eight countries. The data we will be use comes from the Overview Matrix of Exchange Rates from
Bloomberg Cross-Rates Overall Chart on January, 10 2018.
"""

import numpy as np
import pandas as pd

# Creates numpy vector from a list to represent money (inputs) vector.
money = np.array([70, 100, 20, 80, 40, 70, 60, 100])

# Creates pandas dataframe with column labels(currency_label) from the numpy vector for printing.
currency_label = ["USD", "EUR", "JPY", "GBP", "CHF", "CAD", "AUD", "HKD"]
money_df = pd.DataFrame(data=money, index=currency_label, columns=["Amounts"])
print("Inputs Vector:")
print(money_df.T)

# Imports conversion rates(weights) matrix as a pandas dataframe.
conversion_rates_df = pd.read_csv("currencyConversionMatrix.csv", header=0, index_col=0)

# Creates numpy matrix from a pandas dataframe to create the conversion rates(weights) matrix.
conversion_rates = conversion_rates_df.values

# Prints conversion rates matrix.
print("Weights Matrix:")
print(conversion_rates_df)


# TODO 1.: Calculates the money totals(outputs) vector using matrix multiplication in numpy.
money_totals = np.matmul(money, conversion_rates)

# Converts the resulting money totals vector into a dataframe for printing.
money_totals_df = pd.DataFrame(data = money_totals, index = currency_label, columns = ["Money Totals"])
print("Outputs Vector:")
print(money_totals_df.T)
