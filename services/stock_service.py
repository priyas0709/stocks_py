from data.stock_repository import StockRepository
from models.stock import Stock

class StockService:
    def __init__(self, repository: StockRepository):
        self.repository = repository

    def get_stock(self, symbol: str, start_date: str, end_date: str) -> Stock:
        """Get stock data and return Stock object"""
        data = self.repository.get_stock_data(symbol, start_date, end_date)
        return Stock(symbol=symbol, data=data)
