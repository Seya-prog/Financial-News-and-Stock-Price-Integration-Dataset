# pynance.py (to be placed in the 'notebooks' directory)
import pandas as pd
import numpy as np

class Pynance:
    """
    A local shim class to provide Pynance-like functionality
    as expected by the notebook task2_quantitative_analysis.ipynb,
    particularly the get_returns() and get_log_returns() methods.
    This allows 'from pynance import Pynance' to work if this
    file is in the same directory as the notebook.
    """
    def __init__(self, dataframe_with_renamed_cols):
        """
        Initializes with a pandas DataFrame.
        The DataFrame is expected to have a 'date' column (datetime)
        and a 'close' column, among others like 'open', 'high', 'low', 'volume'.
        The input dataframe_with_renamed_cols has 'date' as a column, not yet an index.
        """
        self.df = dataframe_with_renamed_cols.copy()
        if 'date' not in self.df.columns:
            raise ValueError("Input DataFrame must contain a 'date' column that can be set as index.")
        
        # Ensure 'date' column is datetime and set it as index
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.df.set_index('date', inplace=True)
        
        if 'close' not in self.df.columns:
            raise ValueError("Input DataFrame must contain a 'close' column for calculations.")

    def get_returns(self):
        """
        Calculates simple daily percentage returns based on the 'close' price.
        """
        if 'close' not in self.df.columns:
            raise ValueError("'close' column not found in DataFrame.")
        return self.df['close'].pct_change()

    def get_log_returns(self):
        """
        Calculates simple daily logarithmic returns based on the 'close' price.
        """
        if 'close' not in self.df.columns:
            raise ValueError("'close' column not found in DataFrame.")
        # Calculate log returns as log(current_price / previous_price)
        return np.log(self.df['close'] / self.df['close'].shift(1))
