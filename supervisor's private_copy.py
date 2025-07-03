from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
import json

def load_data(filename="price_data.json"):
    with open(filename, 'r') as f:
        return json.load(f)

def create_pptx(data, output_file="price_dashboard.pptx"):
    prs = Presentation()

    # Summary Slide
    summary_slide = prs.slides.add_slide(prs.slide_layouts[5])
    title_shape = summary_slide.shapes.title
    title_shape.text = "Price Change Summary Dashboard"

    total_products = len(data)
    price_changes = [item for item in data if item['old_price'] != item['new_price']]
    anomalies = [item for item in data if item.get('is_anomaly', False)]

    summary = f"""
    Total Products Tracked: {total_products}
    Price Changes Detected: {len(price_changes)}
    Flagged Anomalies: {len(anomalies)}
    """
    textbox = summary_slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(2))
    tf = textbox.text_frame
    tf.text = summary.strip()

    # Price Change Detail Slide
    detail_slide = prs.slides.add_slide(prs.slide_layouts[5])
    title_shape = detail_slide.shapes.title
    title_shape.text = "Major Price Changes"

    sorted_changes = sorted(price_changes, key=lambda x: abs(x['percent_change']), reverse=True)[:5]

    text = "Top 5 Changes:\n"
    for item in sorted_changes:
        text += f"{item['name']} ({item['sku']}): {item['old_price']} → {item['new_price']} ({item['percent_change']}%)\n"

    textbox = detail_slide.shapes.add_textbox(Inches(1), Inches(1.2), Inches(8), Inches(4))
    tf = textbox.text_frame
    tf.text = text.strip()

    # Anomaly Slide
    anomaly_slide = prs.slides.add_slide(prs.slide_layouts[5])
    title_shape = anomaly_slide.shapes.title
    title_shape.text = "Price Anomalies"

    if anomalies:
        text = "Anomalies Detected:\n"
        for item in anomalies:
            text += f"{item['name']} ({item['sku']}): {item['old_price']} → {item['new_price']} ({item['percent_change']}%)\n"
    else:
        text = "No anomalies detected."

    textbox = anomaly_slide.shapes.add_textbox(Inches(1), Inches(1.2), Inches(8), Inches(4))
    tf = textbox.text_frame
    tf.text = text.strip()

    prs.save(output_file)
    print(f"PowerPoint dashboard saved as {output_file}")

# Run
data = load_data("price_data.json")
create_pptx(data)
