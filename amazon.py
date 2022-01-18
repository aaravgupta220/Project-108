import csv
import pandas as pd
import plotly.figure_factory as ff

reader = pd.read_csv("amazon.csv")

fig = ff.create_distplot([reader["Avg Rating"].tolist()], ["Average Rating of Mobile"], show_hist=False)
fig.show()