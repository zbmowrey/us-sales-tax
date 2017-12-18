# us-sales-tax
When fed one or more CSV files, rates.py will consume that data and turn it into a SQLite3 database file for you.

The order of columns is:

Region Abbreviation     <-- AK, AL, IL, FL, etc
Postal Code             <-- 10011, 12345, etc
Region Name or Label    <-- "Illinois" or "St. Johns County"
Region Tax Percentage   <-- 0.01  <-- in the US, we call this a state
Total Tax Percentage    <-- 0.04  <-- all other taxes summed
County Tax Percentage   <-- 0.01  
Local Tax Percentage    <-- 0.01
Special Tax Percentage  <-- 0.01
Risk Score              <-- 1, 2, 3, etc
