# --- core_logic.py ---
import pandas as pd

def load_and_filter_data(filepath: str, min_value: float) -> pd.DataFrame:
    """Loads CSV and filters rows based on a column value."""
    try:
        df = pd.read_csv(filepath)
        # Basic validation
        if 'value' not in df.columns:
            raise ValueError("CSV must contain a 'value' column.")
        filtered_df = df[df['value'] >= min_value]
        return filtered_df
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except Exception as e:
        # Catch other potential pandas errors or general issues
        raise RuntimeError(f"Error processing data: {str(e)}")

