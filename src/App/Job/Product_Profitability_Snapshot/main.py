from src.App.Job.Product_Profitability_Snapshot.models.extract import extract
from src.App.Job.Product_Profitability_Snapshot.models.transform import transform
from src.App.Job.Product_Profitability_Snapshot.models.load import load

import warnings
warnings.filterwarnings("ignore")

# ---- ADD YOUR FILE PATHS ----
sales_path = r"C:/Users/sandh/PycharmProjects/etl-processing-engine-anwar-store/data/sales_wholesale.csv"
purchase_path = r"C:/Users/sandh/PycharmProjects/etl-processing-engine-anwar-store/data/purchase_wholesale_inwards.csv"

print("Start Extracting...")

# ---- EXTRACT ----
sales_df, purchase_df = extract(sales_path, purchase_path)

print("Start Transforming...")

# ---- TRANSFORM ----
tdf = transform(sales_df, purchase_df)

print("Start Loading...")

# ---- LOAD ----
tdf.to_csv(
    r"C:/Users/sandh/PycharmProjects/etl-processing-engine-anwar-store/src/App/Job/Product_Profitability_Snapshot/Loaddata/ws_revenue_by_customer.csv",
    index=False
)

print("Data Loaded Successfully!")
