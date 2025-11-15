"""
Waveworks Expense Summary ETL Job.

This script serves as the main entry point for the ETL process.
It orchestrates the flow of data by:
1. Extracting raw expense data from the folder/SQLite database.
2. Transforming the data (aggregating, mapping, and cleaning).
3. Loading the final summary data into the PostgreSQL database.
"""

from models import extract, extract_db, transform, load

def main():
    #data = extract(folder_path='data/waveworks_db/daily_expenses')
    data = extract_db(path='data/waveworks_db/wave_daily.db', table='daily_expenses')
    tdf = transform(data)
    load(tdf)

if __name__ == '__main__':
    main()
