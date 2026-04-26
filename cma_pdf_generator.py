#!/usr/bin/env python3
"""
Professional CMA PDF Generator - Robust Template
Matches 1131 Heath Ave design exactly with full sections
"""
import json
import sys
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

# Colors matching reference design
NAVY = colors.HexColor("#1a2b4a")
GOLD = colors.HexColor("#c8973a")
TEAL = colors.HexColor("#2e7d6c")
LIGHT_GRAY = colors.HexColor("#f5f5f5")
LIGHT_BEIGE = colors.HexColor("#f9f5ed")
GREEN_LIGHT = colors.HexColor("#e8f5e9")
WHITE = colors.white
DARK_TEXT = colors.HexColor("#2a2a2a")

def generate_cma_pdf(data, output_path):
    """Generate professional CMA PDF matching robust template design"""
    
    doc = SimpleDocTemplate(output_path, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch, 
                           leftMargin=0.6*inch, rightMargin=0.6*inch)
    story = []
    
    # Define all paragraph styles
    title_style = ParagraphStyle(
        'Title',
        fontName='Helvetica-Bold',
        fontSize=24,
        textColor=WHITE,
        alignment=TA_CENTER,
        spaceAfter=12
    )
    
    header_text_style = ParagraphStyle(
        'HeaderText',
        fontName='Helvetica',
        fontSize=10,
        textColor=colors.HexColor("#cccccc"),
        alignment=TA_CENTER,
        spaceAfter=4
    )
    
    address_style = ParagraphStyle(
        'Address',
        fontName='Helvetica-Bold',
        fontSize=16,
        textColor=GOLD,
        alignment=TA_CENTER,
        spaceAfter=8
    )
    
    section_style = ParagraphStyle(
        'SectionHeader',
        fontName='Helvetica-Bold',
        fontSize=11,
        textColor=NAVY,
        spaceAfter=8
    )
    
    body_style = ParagraphStyle(
        'Body',
        fontName='Helvetica',
        fontSize=9,
        textColor=DARK_TEXT,
        spaceAfter=8
    )
    
    label_style = ParagraphStyle('Label', fontName='Helvetica', fontSize=9, textColor=DARK_TEXT, alignment=TA_LEFT)
    value_style = ParagraphStyle('Value', fontName='Helvetica', fontSize=9, textColor=DARK_TEXT, alignment=TA_LEFT)
    
    # ===== 1. HEADER BANNER =====
    realtor_name = data.get('realtor_name', 'N/A')
    header_data = [
        [Paragraph("COMPARATIVE MARKET ANALYSIS", title_style)],
        [Paragraph(f"{data['address']}", address_style)],
        [Paragraph(f"{data.get('subdivision', 'N/A')} | {data.get('county', 'N/A')}, Virginia", header_text_style)],
        [Paragraph(f"Report Date: {datetime.now().strftime('%B %d, %Y')}", header_text_style)],
        [Paragraph(f"Prepared for: {realtor_name}", header_text_style)]
    ]
    
    header_table = Table(header_data, colWidths=[6.8*inch])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), NAVY),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 14),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 14),
    ]))
    
    story.append(header_table)
    story.append(Spacer(1, 0.2*inch))
    
    # ===== 2. NOTICE BOX =====
    notice_text = "NOTICE: This Comparative Market Analysis is not an appraisal and should not be used as a substitute for one. Values are derived from publicly available MLS sold data and automated valuation estimates. Market conditions change rapidly."
    notice_para = Paragraph(notice_text, ParagraphStyle('Notice', fontName='Helvetica', fontSize=8, textColor=DARK_TEXT))
    
    notice_table = Table([[notice_para]], colWidths=[6.8*inch])
    notice_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_BEIGE),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#d4c5a9")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    
    story.append(notice_table)
    story.append(Spacer(1, 0.2*inch))
    
    # ===== 3. SUBJECT PROPERTY OVERVIEW =====
    story.append(Paragraph("SECTION 1 — SUBJECT PROPERTY OVERVIEW", section_style))
    
    # Quick facts row
    quick_facts = [
        [data.get('beds', 'N/A'), data.get('baths', 'N/A'), f"{data.get('sqft', 'N/A')} Sq Ft", 
         data.get('lot', 'N/A'), data.get('year', 'N/A')],
        ["Bedrooms", "Bathrooms", "Above-Grade Sq Ft", "Lot Size", "Year Built"]
    ]
    
    quick_table = Table(quick_facts, colWidths=[1.1*inch, 1.1*inch, 1.4*inch, 1.1*inch, 1.1*inch])
    quick_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), LIGHT_GRAY),
        ('BACKGROUND', (0, 1), (-1, 1), WHITE),
        ('ALIGN', (0, 0), (-1, 1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, 1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, 1), 8),
        ('TEXTCOLOR', (0, 0), (-1, 1), DARK_TEXT),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#cccccc")),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    
    story.append(quick_table)
    story.append(Spacer(1, 0.15*inch))
    
    # Property details (2-column)
    prop_details = [
        [Paragraph("Address", label_style), Paragraph(data['address'], value_style), 
         Paragraph("Subdivision", label_style), Paragraph(data.get('subdivision', 'N/A'), value_style)],
        [Paragraph("Property Type", label_style), Paragraph(data.get('property_type', 'N/A'), value_style), 
         Paragraph("Style", label_style), Paragraph(data.get('style', 'N/A'), value_style)],
        [Paragraph("Total Building Sq Ft", label_style), Paragraph(f"{data.get('sqft', 'N/A')} sq ft", value_style), 
         Paragraph("County", label_style), Paragraph(data.get('county', 'N/A'), value_style)],
        [Paragraph("Exterior / Roof", label_style), Paragraph(data.get('exterior', 'N/A'), value_style), 
         Paragraph("HVAC", label_style), Paragraph(data.get('hvac', 'N/A'), value_style)],
        [Paragraph("Zoning", label_style), Paragraph(data.get('zoning', 'N/A'), value_style), 
         Paragraph("APN", label_style), Paragraph(data.get('apn', 'N/A'), value_style)],
        [Paragraph("Last Sold", label_style), Paragraph(data.get('last_sold', 'N/A'), value_style), 
         Paragraph("2025 Assessment", label_style), Paragraph(data.get('assessment', 'N/A'), value_style)]
    ]
    
    detail_table = Table(prop_details, colWidths=[1.4*inch, 1.9*inch, 1.4*inch, 1.9*inch])
    detail_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), LIGHT_GRAY),
        ('BACKGROUND', (2, 0), (2, -1), LIGHT_GRAY),
        ('BACKGROUND', (1, 0), (1, -1), WHITE),
        ('BACKGROUND', (3, 0), (3, -1), WHITE),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TEXTCOLOR', (0, 0), (-1, -1), DARK_TEXT),
        ('BORDER', (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    
    story.append(detail_table)
    story.append(Spacer(1, 0.25*inch))
    
    # ===== 4. AUTOMATED VALUE ESTIMATES =====
    story.append(Paragraph("SECTION 2 — AUTOMATED VALUE ESTIMATES", section_style))
    
    est_text = "Industry automated valuation models (AVMs) provide supplemental data points for comparison alongside the comparable sales analysis:"
    story.append(Paragraph(est_text, body_style))
    story.append(Spacer(1, 0.1*inch))
    
    estimates = data.get('estimates', {})
    est_rows = [
        [f"${estimates.get('redfin', 'N/A'):,}" if isinstance(estimates.get('redfin'), (int, float)) else estimates.get('redfin', 'N/A'),
         f"${estimates.get('homescom', 'N/A'):,}" if isinstance(estimates.get('homescom'), (int, float)) else estimates.get('homescom', 'N/A'),
         f"${estimates.get('city_assessment', 'N/A'):,}" if isinstance(estimates.get('city_assessment'), (int, float)) else estimates.get('city_assessment', 'N/A'),
         f"${data.get('value_mid', 'N/A'):,}" if isinstance(data.get('value_mid'), (int, float)) else data.get('value_mid', 'N/A')],
        ["Redfin Estimate", "Homes.com Estimate", "City Assessment", "CMA Recommended Value"]
    ]
    
    est_table = Table(est_rows, colWidths=[1.7*inch, 1.7*inch, 1.7*inch, 1.7*inch])
    est_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), LIGHT_GRAY),
        ('BACKGROUND', (0, 1), (-1, 1), WHITE),
        ('ALIGN', (0, 0), (-1, 1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, 1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, 1), 8),
        ('TEXTCOLOR', (0, 0), (-1, 1), DARK_TEXT),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#cccccc")),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    
    story.append(est_table)
    story.append(Spacer(1, 0.25*inch))
    
    # ===== 5. COMPARABLE SALES =====
    story.append(Paragraph("SECTION 3 — RECENT COMPARABLE SOLD PROPERTIES", section_style))
    
    comp_intro = data.get('comp_intro', "Five to seven comparable properties sold within 6-12 months and 1-2 miles of the subject property were selected based on similar characteristics including bedroom/bathroom count, square footage, age, and construction type.")
    story.append(Paragraph(comp_intro, body_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Comps table
    comps = data.get('comps', [])
    comp_rows = [["Comp", "Address", "Sale Date", "Sale Price", "Bed/Bath", "Sq Ft", "Year Built", "$/Sq Ft", "Notes"]]
    
    for i, comp in enumerate(comps[:7]):  # 5-7 comps
        comp_rows.append([
            chr(65 + i),  # A, B, C, etc.
            Paragraph(comp.get('address', 'N/A'), ParagraphStyle('CompAddr', fontName='Helvetica', fontSize=8)),
            comp.get('sold_date', 'N/A'),
            f"${comp.get('sold_price', 0):,.0f}",
            f"{comp.get('beds', 'N/A')}/{comp.get('baths', 'N/A')}",
            f"{comp.get('sqft', 'N/A'):,}",
            comp.get('year', 'N/A'),
            f"${comp.get('sold_price', 0) / max(comp.get('sqft', 1), 1):.0f}",
            comp.get('notes', '')
        ])
    
    # Subject row
    subject_sqft = data.get('sqft', 1)
    comp_rows.append([
        "SU",
        data['address'],
        "—",
        "—",
        f"{data.get('beds', 'N/A')}/{data.get('baths', 'N/A')}",
        f"{subject_sqft:,}",
        data.get('year', 'N/A'),
        "—",
        "Subject property"
    ])
    
    comp_table = Table(comp_rows, colWidths=[0.4*inch, 1.4*inch, 0.65*inch, 0.8*inch, 0.6*inch, 0.55*inch, 0.55*inch, 0.55*inch, 0.95*inch])
    comp_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
        ('BACKGROUND', (0, -1), (-1, -1), GREEN_LIGHT),
        ('FONTNAME', (0, 1), (-1, -2), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -2), 8),
        ('ALIGN', (3, 1), (7, -2), 'RIGHT'),
        ('ALIGN', (0, 1), (2, -2), 'LEFT'),
        ('ALIGN', (8, 1), (8, -2), 'LEFT'),
        ('TEXTCOLOR', (0, 1), (-1, -1), DARK_TEXT),
        ('BORDER', (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    
    story.append(comp_table)
    story.append(Spacer(1, 0.25*inch))
    
    # ===== 6. ADJUSTMENT ANALYSIS =====
    story.append(Paragraph("SECTION 4 — PRICE ADJUSTMENT ANALYSIS", section_style))
    
    adj_text = "Each comparable property has been adjusted to account for material differences compared to the subject property. Key adjustment factors include property size ($/sqft), bathroom count, and time-on-market appreciation/depreciation."
    story.append(Paragraph(adj_text, body_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Adjustment table
    adj_rows = [["Comp", "Sale Price", "Size Adjustment", "Bath Adjustment", "Time Adjustment", "Adjusted Value"]]
    
    for i, comp in enumerate(comps[:7]):
        adj_rows.append([
            chr(65 + i),
            f"${comp.get('sold_price', 0):,.0f}",
            f"${comp.get('size_adj', 0):,.0f}",
            f"${comp.get('bath_adj', 0):,.0f}",
            f"${comp.get('time_adj', 0):,.0f}",
            f"${comp.get('adjusted_value', comp.get('sold_price', 0)):,.0f}"
        ])
    
    adj_table = Table(adj_rows, colWidths=[0.6*inch, 1.15*inch, 1.15*inch, 1.15*inch, 1.15*inch, 1.5*inch])
    adj_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('BACKGROUND', (0, 1), (-1, -1), LIGHT_GRAY),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('ALIGN', (1, 1), (-1, -1), 'RIGHT'),
        ('ALIGN', (0, 1), (0, -1), 'CENTER'),
        ('TEXTCOLOR', (0, 1), (-1, -1), DARK_TEXT),
        ('BORDER', (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    
    story.append(adj_table)
    story.append(Spacer(1, 0.25*inch))
    
    # ===== 7. MARKET CONDITIONS =====
    story.append(Paragraph("SECTION 5 — LOCAL MARKET CONDITIONS", section_style))
    
    market = data.get('market_data', {})
    market_vals = [
        [f"${market.get('median_price', 'N/A'):,}" if isinstance(market.get('median_price'), (int, float)) else market.get('median_price', 'N/A'),
         market.get('sale_to_list', 'N/A'),
         market.get('days_on_market', 'N/A'),
         market.get('market_type', 'N/A')],
        ["Median Sale Price", "Sale-to-List Ratio", "Avg. Days on Market", "Market Condition"]
    ]
    
    market_table = Table(market_vals, colWidths=[1.7*inch, 1.7*inch, 1.7*inch, 1.7*inch])
    market_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), LIGHT_GRAY),
        ('BACKGROUND', (0, 1), (-1, 1), WHITE),
        ('ALIGN', (0, 0), (-1, 1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, 1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, 1), 8),
        ('TEXTCOLOR', (0, 0), (-1, 1), DARK_TEXT),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#cccccc")),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    
    story.append(market_table)
    story.append(Spacer(1, 0.15*inch))
    
    market_narrative = data.get('market_narrative', f"The {data.get('subdivision', 'local')} market is currently {market.get('market_type', 'balanced')}. Properties are selling at approximately {market.get('sale_to_list', '95')}% of list price, with an average of {market.get('days_on_market', '30')} days on market.")
    story.append(Paragraph(market_narrative, body_style))
    story.append(Spacer(1, 0.25*inch))
    
    # ===== 8. PRICING RECOMMENDATION =====
    story.append(Paragraph("SECTION 6 — PRICING RECOMMENDATION", section_style))
    
    val_low = data.get('value_low', 300000)
    val_mid = data.get('value_mid', 335000)
    val_high = data.get('value_high', 365000)
    
    # 3-tier pricing boxes
    value_rows = [
        ["Conservative", "Recommended", "Aggressive"],
        [f"${val_low:,.0f}", f"${val_mid:,.0f}", f"${val_high:,.0f}"]
    ]
    
    value_table = Table(value_rows, colWidths=[2.26*inch, 2.27*inch, 2.27*inch])
    value_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('BACKGROUND', (0, 1), (-1, 1), GREEN_LIGHT),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 1), (-1, 1), 14),
        ('ALIGN', (0, 1), (-1, 1), 'CENTER'),
        ('TEXTCOLOR', (0, 1), (-1, 1), TEAL),
        ('BORDER', (0, 0), (-1, -1), 2, GOLD),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    
    story.append(value_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Pricing narrative
    pricing_narrative = data.get('pricing_narrative', f"Based on the comparable sales analysis and adjusted values, the recommended listing price range is ${val_low:,.0f} to ${val_high:,.0f}, with a midpoint of ${val_mid:,.0f}. This range reflects current market conditions and property characteristics.")
    story.append(Paragraph(pricing_narrative, body_style))
    story.append(Spacer(1, 0.25*inch))
    
    # ===== 9. KEY FACTORS =====
    story.append(Paragraph("KEY FACTORS IN THIS VALUATION", section_style))
    
    key_factors = data.get('key_factors', "• Market conditions favor buyers in this area\n• Property condition is comparable to recent sales\n• Location and accessibility are strong points\n• Recent comparable sales support the recommended value")
    story.append(Paragraph(key_factors, body_style))
    story.append(Spacer(1, 0.25*inch))
    
    # ===== 10. DISCLAIMER =====
    disclaimer_text = "This Comparative Market Analysis has been prepared based on publicly available information, including MLS data, automated valuation models, and market research. While prepared with care, this analysis is not a professional appraisal and should not be used as a substitute for one. Market values can fluctuate based on economic conditions, interest rates, and local market factors. This report is valid for 30 days from the report date."
    
    disclaimer_para = Paragraph(disclaimer_text, ParagraphStyle('Disclaimer', fontName='Helvetica', fontSize=8, textColor=DARK_TEXT))
    disclaimer_table = Table([[disclaimer_para]], colWidths=[6.8*inch])
    disclaimer_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_BEIGE),
        ('BORDER', (0, 0), (-1, -1), 1, colors.HexColor("#d4c5a9")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    
    story.append(disclaimer_table)
    
    # Build PDF
    doc.build(story)
    return output_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 cma_pdf_generator.py <json_file_path>")
        sys.exit(1)
    
    # Read JSON data from file (passed as argument)
    json_file = sys.argv[1]
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    address = data.get('address', 'Property')
    output_file = f"/tmp/{address.replace(' ', '_').replace(',', '')}.pdf"
    
    result = generate_cma_pdf(data, output_file)
    print(result)
