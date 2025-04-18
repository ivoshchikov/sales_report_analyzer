import pandas as pd
from typing import Optional


def summarize_by_category(
    df: pd.DataFrame,
    category_col: str = "Category",
    total_col: str = "Total"
) -> pd.DataFrame:
    """
    Aggregate sales by category.
    """
    return (
        df.groupby(category_col)[total_col]
          .agg(Total="sum", Average="mean", Transactions="count")
          .reset_index()
    )


def summarize_by_day(
    df: pd.DataFrame,
    date_col: str = "Date",
    total_col: str = "Total"
) -> pd.DataFrame:
    """
    Aggregate sales by day.
    """
    return (
        df.groupby(date_col)[total_col]
          .agg(Total="sum", Transactions="count")
          .reset_index()
    )


def summarize_by_region(
    df: pd.DataFrame,
    region_col: str = "Region",
    total_col: str = "Total"
) -> pd.DataFrame:
    """
    Aggregate sales by region.
    """
    return (
        df.groupby(region_col)[total_col]
          .agg(Total="sum", Average="mean", Transactions="count")
          .reset_index()
    )


def summarize_by_sales_rep(
    df: pd.DataFrame,
    rep_col: str = "SalesRep",
    total_col: str = "Total"
) -> pd.DataFrame:
    """
    Aggregate sales by sales representative.
    """
    return (
        df.groupby(rep_col)[total_col]
          .agg(Total="sum", Average="mean", Transactions="count")
          .reset_index()
    )