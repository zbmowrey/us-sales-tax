#!/usr/bin/python3.5

from os import listdir
from os.path import isfile, join
import sys
import csv
import sqlite3


files = [f for f in listdir("rates") if isfile(join("rates",f))]
if files:
    print("Found one or more files, checking to see if they're usable.")
    conn = sqlite3.connect('tax_rates.sqlite')
    c = conn.cursor()
    # Create table and/or empty it of existing values.
    c.execute('''CREATE TABLE IF NOT EXISTS rates (state_abbr, zip_code, tax_region_name, tax_state, tax_total, tax_county, tax_city, tax_special, risk_level)''')
    c.execute('''DELETE FROM rates''')
    for f in files:
        if f.endswith('.csv'):
            print("Processing " + f)
            with open("rates/"+f,newline="") as csvfile:
                reader = csv.reader(csvfile,delimiter=",",quotechar="\\")
                i = 0
                for row in reader:
                    if i > 0:
                        row[1] = int(row[1])
                        row[3] = float(row[3])
                        row[4] = float(row[4])
                        row[5] = float(row[5])
                        row[6] = float(row[6])
                        row[7] = float(row[7])
                        row[8] = int(row[8])
                        c.execute("INSERT INTO rates VALUES (?,?,?,?,?,?,?,?,?)",row)
                        # Save (commit) the changes
                    i = i + 1
    conn.commit()
    # Close the connection when we're done
    conn.close()
    print("Operation completed without errors.")
else:
    print("No files found to process.")
