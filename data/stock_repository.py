import pandas as pd
import yfinance as yf

class StockRepository:
    def __init__(self):
        self.cache = {}

    def get_stock_data(self, symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
        """Fetch stock data from Yahoo Finance"""
        if symbol not in self.cache:
            stock = yf.Ticker(symbol)
            self.cache[symbol] = stock.history(start=start_date, end=end_date)
        return self.cache[symbol]

    def clear_cache(self):
        """Clear cached stock data"""
        self.cache.clear()
