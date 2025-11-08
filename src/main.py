from models.extrfun import extract, transform, load

data = extract(path="./data/daily_expenses.csv")
transformed_data = transform(data)
load(transformed_data)