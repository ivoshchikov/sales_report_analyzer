import pandas as pd
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as OpenpyxlImage
from io import BytesIO
from typing import Dict, Any


def export_report(
    output_path: str,
    raw_df: pd.DataFrame,
    summary_category: pd.DataFrame,
    summary_day: pd.DataFrame,
    summary_region: pd.DataFrame,
    summary_sales_rep: pd.DataFrame,
    charts: Dict[str, Any],
    config: Dict[str, Any]
) -> None:
    """
    Export raw data, multiple summary tables, and charts into an Excel file.
    """
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        raw_df.to_excel(writer, sheet_name=config["sheets"]["data"], index=False)
        summary_category.to_excel(writer, sheet_name=config["sheets"]["summary_by_category"], index=False)
        summary_day.to_excel(writer, sheet_name=config["sheets"]["summary_by_day"], index=False)
        summary_region.to_excel(writer, sheet_name=config["sheets"]["summary_by_region"], index=False)
        summary_sales_rep.to_excel(writer, sheet_name=config["sheets"]["summary_by_sales_rep"], index=False)

    wb = load_workbook(output_path)
    for sheet_name, fig in charts.items():
        buffer = BytesIO()
        fig.savefig(buffer, format="png", bbox_inches="tight")
        buffer.seek(0)
        img = OpenpyxlImage(buffer)
        wb[sheet_name].add_image(img, "B2")
    wb.save(output_path)