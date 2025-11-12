''' ETL to merge sales_wholesale.csv with customers_wholesale.csv 
 Filter unpaid invoices, sum outstanding amount per customer, count open invoices.'''


import warnings
from models.extract import extract
from models.transform import transform
from models.load import load


warnings.filterwarnings("ignore")

data=extract(path1='C:\Mini Task\etl-processing-engine-anwar-store-1\data\sales_wholesale.csv',
            path2='C:\Mini Task\etl-processing-engine-anwar-store-1\data\customers_wholesale.csv' )




tdf=transform(data)
load=load(tdf)