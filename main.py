from data.stock_repository import StockRepository
from services.stock_service import StockService
from visualization.stock_visualizer import StockVisualizer

def main():
    # Initialize components
    repository = StockRepository()
    service = StockService(repository)

    # Get stock data (example: Apple stock for the last 6 months)
    symbol = "AAPL"
    start_date = "2024-09-01"
    end_date = "2025-03-01"

    # Fetch stock data
    stock = service.get_stock(symbol, start_date, end_date)

    # Visualize the data
    visualizer = StockVisualizer()
    visualizer.plot_price_and_volume(stock)
    visualizer.plot_moving_average(stock)

if __name__ == "__main__":
    main()
