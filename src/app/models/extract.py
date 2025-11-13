import pandas as pd

def extract(path1,path2,id_col='customer_id'):

    s_df=pd.read_csv(path1,parse_dates=['order_date'],dayfirst=False,infer_datetime_format=True)
    c_df=pd.read_csv(path2,dayfirst=False,infer_datetime_format=True)


    merge_df=s_df.merge(c_df,how='left',on=id_col)
    print('Data Extracted')

    return merge_df