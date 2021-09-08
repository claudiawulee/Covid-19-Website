#Number of Confirmed Cases in Each Country since 1/22/2020

import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objs as go 
import plotly.io as pio


df = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv') # changed link from my copy to orginal data set
df = pd.DataFrame(df)


df =df.drop(columns=['Province/State', 'Lat','Long'])
df=df.rename(columns={'Country/Region':'Time'})
df = df.set_index('Time').transpose()


no_duplicates = df.groupby(df.columns, axis=1).sum()



fig = go.Figure()
for col in no_duplicates.columns:
    fig.add_trace(go.Scatter(x=df.index, y=df[col],  mode='lines', name = col))
fig.update_layout(title = "Number of Confirmed Cases in Each Country")
#fig.show()
fig.write_html("covidOverallGraphs.html")
