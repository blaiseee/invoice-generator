from fpdf import FPDF
from datetime import datetime
import os

# Helper function to format currency
def php(amount):
    return f"PHP{amount:,.2f}"

# Invoice Data
seller_info = {
    "name": "",
    "address": "",
    "contact": "",
    "email": ""
}

client_info = {
    "name": "",
    "address": "",
    "contact": "",
    "email": ""
}

invoice_number = f"EC-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
invoice_date = datetime.now().strftime("%Y-%m-%d")
due_date = "Due upon receipt"
payment_method = ""

services = []

print("Enter service details. Type 'done' when finished.\n")

while True:
  description = input("Service Description: ")
  if description.lower() == "done":
    break
  try:
    amount = float(input("Amount (PHP): "))
    services.append({"description": description, "amount": amount})
  except ValueError:
    print("Invalid amount. Please enter a valid number.")
    

total_amount = sum(service["amount"] for service in services)

# Generate PDF Invoice
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "INVOICE", ln=True, align="C")

pdf.set_font("Arial", "", 12)
pdf.cell(0, 10, f"Invoice Number: {invoice_number}", ln=True)
pdf.cell(0, 10, f"Invoice Date: {invoice_date}", ln=True)
pdf.cell(0, 10, f"Due Date: {due_date}", ln=True)
pdf.cell(0, 10, f"Payment Method: {payment_method}", ln=True)

pdf.ln(10)
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "From:", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, f"{seller_info['name']}\n{seller_info['address']}\n{seller_info['contact']}\n{seller_info['email']}")

pdf.ln(5)
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Bill To:", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, f"{client_info['name']}\n{client_info['address']}\n{client_info['email']}")

pdf.ln(10)
pdf.set_font("Arial", "B", 12)
pdf.cell(130, 10, "Description", border=1)
pdf.cell(60, 10, "Amount", border=1, ln=True)

pdf.set_font("Arial", "", 12)
for service in services:
    pdf.cell(130, 10, service["description"], border=1)
    pdf.cell(60, 10, php(service["amount"]), border=1, ln=True)

pdf.set_font("Arial", "B", 12)
pdf.cell(130, 10, "Total", border=1)
pdf.cell(60, 10, php(total_amount), border=1, ln=True)

pdf.ln(10)
pdf.set_font("Arial", "I", 10)
pdf.multi_cell(0, 10, "Thank you for your business!\nPlease make the payment as soon as possible.")

pdf_path = f"invoice_blaise{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf"
pdf.output(pdf_path)

pdf_path  # Return PDF path for download link

