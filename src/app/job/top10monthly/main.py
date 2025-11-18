from src.app.job.top10monthly.models.extract import extract
from src.app.job.top10monthly.models.transform import transform
from src.app.job.top10monthly.models.load import load



def main():
    sales_file = ("C:/Users/black/PycharmProjects/etl-processing-engine-anwar-store/data/sales_retail.csv")
    product_file = ("C:/Users/black/PycharmProjects/etl-processing-engine-anwar-store/data/products.csv")
    output_file = ("C:/Users/black/PycharmProjects/etl-processing-engine-anwar-store/src/app/job/top10monthly/result/top10_monthly.csv")

    sales, products = extract(sales_file, product_file)
    print("Sales rows:", len(sales))
    print("Products rows:", len(products))

    result = transform(sales, products)
    print("After transform rows:", len(result))
    load(result, output_file)

if __name__ == "__main__":
    main()

