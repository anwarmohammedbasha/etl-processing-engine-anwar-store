import pandas as pd

def load(final_df,Output_path:str):
    print("Start loading data")


    final_df.to_csv("src/App/Job/Product_Profitability_Snapshot/result/ws_revenue_by_customer.csv",
                    index=False)

    print("Data successfully loaded")