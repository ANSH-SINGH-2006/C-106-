import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df, x="Temperature", y="Ice-cream Sales")
        fig.show()

def getDataSource(data_path):
    ice_cream_sales=[]
    temperature=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)

        for row in csv_reader:
            ice_cream_sales.append(float(row["Ice-cream Sales"]))
            temperature.append(float(row["Temperature"]))
    return {"x": temperature, "y": ice_cream_sales}

def findCorelation(dataSource):
    corelation=np.corrcoef(dataSource["x"], dataSource["y"])
    print("Corelation between temperature VS ice-cream sales is: ", corelation[0,1])

def setup():
    data_path="temp-ice.csv"
    dataSource=getDataSource(data_path)
    findCorelation(dataSource)
    plotFigure(data_path)

setup()