import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio



df = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv') #changed link from my copy to original
df = pd.DataFrame(df)

df =df.drop(columns=['Province/State', 'Lat','Long'])
df=df.rename(columns={'Country/Region':'Time'})
df = df.set_index('Time').transpose()
list_of_countries = list(df.columns)

name = input("Enter a country! ")     
name = name.capitalize()
if name in list_of_countries:
  fig = px.line(df, x=df.index, y= name, title="Number of Confirmed Cases in " + name,)
  fig.update_xaxes(title="Time")
  fig.update_yaxes(title="Number of Confirmed Cases")
  fig.show()
else:
	print("No data :( Please input a different country.")


pio.write_html(fig, file='index.html', auto_open=True)
