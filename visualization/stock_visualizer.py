import matplotlib.pyplot as plt
from models.stock import Stock

class StockVisualizer:
    @staticmethod
    def plot_price_and_volume(stock: Stock):
        """Create a plot with price and volume"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), height_ratios=[2, 1])

        # Plot closing price
        ax1.plot(stock.data.index, stock.get_closing_prices(), 'b-')
        ax1.set_title(f'{stock.symbol} Stock Price')
        ax1.set_ylabel('Price ($)')
        ax1.grid(True)

        # Plot volume
        ax2.bar(stock.data.index, stock.get_volume())
        ax2.set_title('Trading Volume')
        ax2.set_ylabel('Volume')
        ax2.grid(True)

        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_moving_average(stock: Stock, window: int = 20):
        """Plot stock price with moving average"""
        plt.figure(figsize=(12, 6))

        # Plot closing price
        plt.plot(stock.data.index, stock.get_closing_prices(), label='Closing Price', alpha=0.5)

        # Plot moving average
        moving_avg = stock.get_closing_prices().rolling(window=window).mean()
        plt.plot(stock.data.index, moving_avg, label=f'{window}-day Moving Average', color='orange')

        plt.title(f'{stock.symbol} Stock Price with Moving Average')
        plt.ylabel('Price ($)')
        plt.legend()
        plt.grid(True)
        plt.show()
