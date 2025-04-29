# 🧾 Python Invoice Generator

A simple Python script to generate PDF invoices using user-defined service details. Built with `FPDF` and `datetime`, this tool is perfect for freelancers, contractors, and small business owners who want quick and customizable invoice creation.

## 📦 Features

- Dynamic input for services (description + amount)
- Auto-generated invoice number and date
- Professional PDF output
- Local saving of generated files
- Philippine Peso (₱) currency formatting
- Editable sender/client information

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- [fpdf2](https://pypi.org/project/fpdf/) library

Install it via pip:

```bash
pip install fpdf
```

## 🔧 How to Use

Run the script and follow the prompts to input your invoice data:
```bash
python main.py
```

You'll be asked to enter:
- Service description
- Amount (in PHP)
- Type done to finish input

A PDF invoice will be generated in the same directory.

## 🖥 Example Output
```bash
Invoice Number: EC-20250429_151230
Invoice Date  : April 29, 2025
Services:
 - Design (25%)       ₱10,000.00
 - Development (25%)  ₱10,000.00
Total:                ₱20,000.00
```

## 📂 Output Files
- invoice_blaise.pdf – the main PDF invoice

## 🧑‍💻 Author<br>
Blaise A. Florendo<br>
📧 blsflorendo@gmail.com / mynameisblaiseflorendo@gmail.com

## 📃 License
This project is open source and available under the MIT License.
