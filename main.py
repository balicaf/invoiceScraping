import pdfplumber
import glob
sum1=0
# Load PDF
pdfs = sorted(glob.glob("./*.pdf"))
#pdfs = glob.glob("./*.pdf")

# Loop through PDFs
for pdf_file in pdfs:
#with pdfplumber.open("8194771357595337_payment.pdf") as pdf:
	pdf = pdfplumber.open(pdf_file) 
# Extract text 
	text = pdf.pages[0].extract_text()

	# Find tax table section
	#table_text = text.split('VAT% Taxable base (in EUR) Total VAT (in EUR)\n')[1]
	table_text = text.split('Amount paid')[1]
	# Get taxable base value  
	parts = table_text.split('\n')[0].split(' ')
	#print(parts)
	base = float(parts[2])  
	# Print total taxable base  
	print(pdf_file , " ", base)
	sum1 += base

	pdf.close()
print(f"Total taxable base: {sum1}")
