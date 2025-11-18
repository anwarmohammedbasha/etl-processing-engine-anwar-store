import pandas as pd

def transform(sales_df, purchase_df):

    print("Start transforming data")

    # Correct groupby & rename
    avg_cost_df = (
        purchase_df.groupby('product_id')['cost_per_box_INR']
        .mean()
        .reset_index()
        .rename(columns={'cost_per_box_INR': 'avg_cost_per_box_INR'})
    )


    merged_df = pd.merge(sales_df, avg_cost_df, on='product_id', how='left')

    # Total Revenue
    merged_df['Total_revenue_INR'] = (
        merged_df['billed_quantity_boxes'] * merged_df['price_per_box_at_sale_INR']
    )

    # Total Cost
    merged_df['total_cost_INR'] = (
        merged_df['billed_quantity_boxes'] * merged_df['avg_cost_per_box_INR']
    )

    # Gross Margin
    merged_df['Gross_Margin'] = (
        merged_df['Total_revenue_INR'] - merged_df['total_cost_INR']
    )

    print("Transformed Data")
    return merged_df
