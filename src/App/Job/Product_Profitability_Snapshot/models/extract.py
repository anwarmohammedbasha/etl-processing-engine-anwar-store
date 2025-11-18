import pandas as pd

def extract(sales_path:str,purchase_path:str):
    """Read the sales and purchase csv files"""

    sales_df=pd.read_csv(sales_path)
    purchase_df=pd.read_csv(purchase_path)

    return sales_df, purchase_df

sales_path=r"C:\Users\sandh\PycharmProjects\etl-processing-engine-anwar-store\data\sales_wholesale.csv"
purchase_path=r"C:\Users\sandh\PycharmProjects\etl-processing-engine-anwar-store\data\purchase_wholesale_inwards.csv"

sales_df,purchase_df=extract(sales_path,purchase_path)

print("Files are Extracted successfully!!")

