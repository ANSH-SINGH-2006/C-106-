import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df, x="Size of TV", y="time")
        fig.show()

def getDataSource(data_path):
    time=[]
    size=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)

        for row in csv_reader:
            time.append(float(row["Size of TV"]))
            size.append(float(row["time"]))
    return {"x": size, "y": time}

def findCorelation(dataSource):
    corelation=np.corrcoef(dataSource["x"], dataSource["y"])
    print("Corelation between size VS TV is: ", corelation[0,1])

def setup():
    data_path="tv-hours.csv"
    dataSource=getDataSource(data_path)
    findCorelation(dataSource)
    plotFigure(data_path)

setup()