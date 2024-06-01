from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet



DATA = [
    ["Date", "Name", "Subscription", "Price (Rs.)"],
    ["05/05/2024",
     "Python Web Scraping - Live Event",
     "Real Python", 
     "15,000.99/-",],
     ["12/05/2024", "Future DevOps :  Live Session,", "7 months", "9.999.00/-"],
     ["Sub Total", "", "","24.999.99/-" ],
     ["Discount", "", "","-4.999.99/-" ],
     ["Total", "", "", "20,000.00/-"],
]
pdf =  SimpleDocTemplate("report.pdf", pagesize = A4)
styles = getSampleStyleSheet()
title_style = styles[ "Heading1" ]
title_style.alignment = 1 
title = Paragraph("Promotion Classes", title_style)
style =  TableStyle([
    ("BOX", (0,0), (-1,-1), 1 , colors.black),
    ("GRID", (0,0), (4,4), 1, colors.black),
    ("BACKGROUND", (0,0), (3,0), colors.grey),
    ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke ),
    ("ALIGN", (0,0), (-1, -1), "CENTER"),
    ("BACKGROUND", (0,1), (-1, -1), colors.beige),
])
#creates the table object and passes the style to it 
table = Table(DATA, style = style)
#builds the actual pdf putting all of the elements
pdf.build([title, table])