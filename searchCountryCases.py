#Search for specific country's graph of confirmed cases since 1/22/2020
#Need to fix the captilization of name inputs with multiple words such as San Marino (which prints San marino) or West Bank and Gaza
import pandas as pd
import plotly
import plotly.express as px


df = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv') # change link from my copy to orginal
df = pd.DataFrame(df)

df =df.drop(columns=['Lat','Long'])   #Country/Region row is still here
df=df.rename(columns={'Country/Region':'Time'})
df = df.set_index('Time').transpose()
df = df.drop(["Province/State"]) #removed Province/State from rows
df = df.groupby(by=df.columns, axis=1).sum()
df = df.rename(columns={"US":"United States"})


list_of_countries = list(df.columns)



name = input("Enter a country! ")     #Problem with countries that are separated into multiple rows based on region e.x. Canada has multiple rows in resp.
name = name.capitalize()
#print(name)
if name == "Us":
  name = "United States"
elif name == "Usa":
  name = "United States"
elif name == "America":
  name = "United States"
elif name == "United states":
    name == "United States"


if name in list_of_countries:
  fig = px.line(df, x=df.index, y= name, title="Number of Confirmed Cases in " + name,)
  fig.update_xaxes(title="Time")
  fig.update_yaxes(title="Number of Confirmed Cases")
  #fig.show()
  fig.write_html("covidGraph_" + name +".html")
else:
	print("No data :( Please input a different country.")
