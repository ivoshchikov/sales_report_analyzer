import argparse
import yaml
from data_loader import load_data
from analyzer import (
    summarize_by_category,
    summarize_by_day,
    summarize_by_region,
    summarize_by_sales_rep
)
from visualizer import plot_bar, plot_line
from excel_exporter import export_report


def main() -> None:
    parser = argparse.ArgumentParser(description="Sales Report Analyzer")
    parser.add_argument("--config", default="config.yaml", help="Path to config YAML")
    args = parser.parse_args()

    # Load configuration
    config = yaml.safe_load(open(args.config, encoding="utf-8"))

    # Load data
    df = load_data(
        config["input_file"],
        sheet_name=config["sheets"]["data"]
    )

    # Analyze
    by_cat = summarize_by_category(df)
    by_day = summarize_by_day(df)
    by_region = summarize_by_region(df)
    by_rep = summarize_by_sales_rep(df)

    # Visualize
    charts = {
        config["sheets"]["summary_by_category"]: plot_bar(by_cat, x="Category", y="Total", title="Sales by Category"),
        config["sheets"]["summary_by_day"]: plot_line(by_day, x="Date", y="Total", title="Daily Sales"),
        config["sheets"]["summary_by_region"]: plot_bar(by_region, x="Region", y="Total", title="Sales by Region"),
        config["sheets"]["summary_by_sales_rep"]: plot_bar(by_rep, x="SalesRep", y="Total", title="Sales by Sales Rep"),
    }

    # Export
    export_report(
        output_path=config["output_file"],
        raw_df=df,
        summary_category=by_cat,
        summary_day=by_day,
        summary_region=by_region,
        summary_sales_rep=by_rep,
        charts=charts,
        config=config
    )

if __name__ == "__main__":
    main()