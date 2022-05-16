import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# Load data
df = pd.read_csv("data/df_final_filtered.csv", index_col=0)

#Title
st.title('Gapminder Data')

col1,col2 = st.columns([2,1])

# Select countries
with col1:
    countries = st.multiselect('Select one/ multiple countries', np.unique(df['country']))

# Select year
year = col2.select_slider('Select a year', np.unique(df['year']))

#Filter df
df_filtered = df.loc[(df.country.isin(countries))&(df.year==year),:]

#Define plot
fig = px.scatter(df_filtered,
    x="GNI per capita",
    y='life expectancy',
	size="population", #Third Parameter
    log_x=True,
    size_max=60,
    color=df_filtered.country)

fig.update_layout(xaxis_range=[0,np.log(np.max(df["GNI per capita"]))])

#Plot
st.plotly_chart(fig, use_container_width=True)
