from models.extrfun import e_t, load

data = e_t(path="./data/daily_expenses.csv")
load(data)