import pandas as pd


def transform(data):
    print('transforming')
    print(data.columns)

    # unpaid =data.columns
    unpaid=data[data['payment_status']!='Paid']

    
    unpaid_data=unpaid.groupby(['customer_id']).agg(
    total_amount=("final_line_total_INR",'sum'),
    open_invoices=("invoice_id",'count'),
    pending_data=("payment_status",'count')


    )



    print('Data transformed')
    return unpaid_data

