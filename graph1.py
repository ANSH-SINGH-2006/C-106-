import plotly.express as px
import csv

with open("temp-ice.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df, x="Temperature", y="Ice-cream Sales")
    fig.show()

with open("coffee.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df, x="Coffee in ml", y="sleep in hours")
    fig.show()