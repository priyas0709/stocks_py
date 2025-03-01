from dataclasses import dataclass
from typing import cast
from pandas import Series, DataFrame

@dataclass
class Stock:
    symbol: str
    data: DataFrame

    def get_closing_prices(self) -> Series:
        if 'Close' not in self.data.columns:
            raise ValueError("No 'Close' column found in the data")

        return cast(Series, self.data['Close'])

    def get_volume(self) -> Series:
        if 'Volume' not in self.data.columns:
            raise ValueError("No 'Volume' column found in the data")

        return cast(Series, self.data['Volume'])
