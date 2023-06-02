import pandas as pd

def read_csv(file_name):
    """
    Read the CSV file and return the data as a pandas DataFrame.
    """
    data = pd.read_csv(file_name)
    return data

def extract_equities(data):
    """
    Extract equity symbols and current prices from the data.
    Return a dictionary mapping symbols to prices.
    """
    equity_data = data[data['Asset Class'] == 'Equity']
    symbols = equity_data['Symbol'].tolist()
    prices = equity_data['Current Price'].tolist()
    equity_prices = {symbol: price for symbol, price in zip(symbols, prices)}
    return equity_prices

def extract_bonds(data):
    """
    Extract bond details from the data.
    Return a list of bond names.
    """
    bond_data = data[data['Asset Class'] == 'Bond']
    bond_names = bond_data['Bond Name'].tolist()
    return bond_names

def adjust_equity_prices(current_prices):
    """
    Adjust the current prices of equities based on the buy price adjustment formula.
    Return a dictionary mapping symbols to adjusted prices.
    """
    adjusted_prices = {symbol: price - 0.05 * price for symbol, price in current_prices.items()}
    return adjusted_prices
