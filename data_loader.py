import pandas as pd
from typing import Optional

def load_data(
    path: str,
    sheet_name: Optional[str] = None,
    parse_dates: bool = True
) -> pd.DataFrame:
    """
    Load sales data from an Excel file into a pandas DataFrame.

    :param path: Path to the Excel file (e.g., 'sales_data.xlsx').
    :param sheet_name: Name of the worksheet. If None, the first sheet is used.
    :param parse_dates: Whether to parse the 'Date' column as datetime.
    :return: DataFrame containing the sales data.
    """
    if sheet_name is None:
        xls = pd.ExcelFile(path)
        sheet_name = xls.sheet_names[0]
    if parse_dates:
        return pd.read_excel(path, sheet_name=sheet_name, parse_dates=["Date"])
    return pd.read_excel(path, sheet_name=sheet_name)