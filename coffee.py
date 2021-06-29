import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df, x="Coffee in ml", y="sleep in hours")
        fig.show()

def getDataSource(data_path):
    coffee_ml=[]
    sleep=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)

        for row in csv_reader:
            coffee_ml.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return {"x": sleep, "y": coffee_ml}

def findCorelation(dataSource):
    corelation=np.corrcoef(dataSource["x"], dataSource["y"])
    print("Corelation between sleep VS coffee is: ", corelation[0,1])

def setup():
    data_path="coffee.csv"
    dataSource=getDataSource(data_path)
    findCorelation(dataSource)
    plotFigure(data_path)

setup()