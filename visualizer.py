import matplotlib.pyplot as plt
from typing import Any, Dict


def plot_bar(
    df,
    x: str,
    y: str,
    title: str = "",
    xlabel: str = None,
    ylabel: str = None
) -> plt.Figure:
    """
    Create a bar chart from a DataFrame.

    :param df: DataFrame containing data to plot.
    :param x: Column name for the x-axis.
    :param y: Column name for the y-axis.
    :param title: (Optional) Title of the chart.
    :param xlabel: (Optional) Label for the x-axis.
    :param ylabel: (Optional) Label for the y-axis.
    :return: Matplotlib Figure object.
    """
    fig, ax = plt.subplots()
    df.plot.bar(x=x, y=y, ax=ax)
    ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    fig.tight_layout()
    return fig


def plot_line(
    df,
    x: str,
    y: str,
    title: str = "",
    xlabel: str = None,
    ylabel: str = None
) -> plt.Figure:
    """
    Create a line chart from a DataFrame.

    :param df: DataFrame containing data to plot.
    :param x: Column name for the x-axis.
    :param y: Column name for the y-axis.
    :param title: (Optional) Title of the chart.
    :param xlabel: (Optional) Label for the x-axis.
    :param ylabel: (Optional) Label for the y-axis.
    :return: Matplotlib Figure object.
    """
    fig, ax = plt.subplots()
    df.plot.line(x=x, y=y, ax=ax)
    ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    fig.autofmt_xdate()
    fig.tight_layout()
    return fig