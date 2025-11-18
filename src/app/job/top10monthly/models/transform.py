import pandas as pd

def transform(sales,products):

#Merge
    merged =pd.merge(sales, products, on='product_id', how='left')

#date column is datetime
    merged['sale_date'] = pd.to_datetime(merged['sale_date'])

#month column
    merged['month'] = merged['sale_date'].dt.to_period('M').astype(str)

#aggregate monthly units + revenue

    monthly = merged.groupby(['month', 'product_id'], as_index=False).agg(
        total_units=('quantity_units_sold', 'sum'),
        total_revenue=('final_line_total_inr', 'sum')
    )

#Rank top 10 per month
    monthly['rank'] = monthly.groupby('month')['total_units'] \
                              .rank(method='dense', ascending=False)\
                              .astype(int)

    top10= monthly[monthly['rank'] <= 10]

    top10 = top10.sort_values(by=['month', 'rank'], ascending=[True, True])

    return top10