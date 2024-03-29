import csv

# Function to check if DOSAGEFORMNAME contains "CAPSULE" or "TABLET"
def contains_capsule_or_tablet(dosage_form):
    return "CAPSULE" in dosage_form.upper() or "TABLET" in dosage_form.upper()

# Input and output file paths
input_file = "ndcxls/product.csv"
output_file = "ndcxls/filtered_products.csv"

# Open input and output files
with open(input_file, mode='r', newline='', encoding='utf-8') as csv_file, \
        open(output_file, mode='w', newline='', encoding='utf-8') as output_csv_file:

    # Create CSV reader and writer objects
    reader = csv.DictReader(csv_file)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(output_csv_file, fieldnames=fieldnames)
    
    # Write header to output file
    writer.writeheader()
    
    # Read each row from the input CSV file
    for row in reader:
        # Check if DOSAGEFORMNAME contains "CAPSULE" or "TABLET"
        if contains_capsule_or_tablet(row["DOSAGEFORMNAME"]):
            # Write the row to the output CSV file
            writer.writerow(row)
