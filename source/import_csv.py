import csv
import matplotlib.pyplot as plt

filename = 'historical_sales_data.csv'

with open(filename) as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    header_row = next(reader)
    
for index, column_header in enumerate(header_row):
    print(index, column_header)
    

