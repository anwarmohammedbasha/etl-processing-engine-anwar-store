
import pandas as pd

def extract(sales_path: str, product_path: str):

    sales = pd.read_csv(sales_path, low_memory=False)
    products = pd.read_csv(product_path, low_memory=False)

    sales.columns = sales.columns.str.lower()
    products.columns = products.columns.str.lower()

    sales['sale_date'] = pd.to_datetime(sales['sale_date'])
    return sales, products
