import streamlit as st
import pandas as pd
world = pd.read_csv('world_population.csv')
cols = world.columns
country = world['Country/Territory']
continent = world['Continent']
capital = world['Capital']

cols_drop = ['Country/Territory','Continent','Capital']

st.title('World Mini Atlas')
st.sidebar.title('Choose the Demographics')

country_param = st.sidebar.selectbox('Country',world['Country/Territory'])
param1 = st.sidebar.selectbox('Choose Parameter 1',cols.drop(cols_drop))
cols_drop.append(param1)
param2 = st.sidebar.selectbox('Choose Parameter 2',cols.drop(cols_drop))

btn = st.sidebar.button('Get Data')
result_df = pd.DataFrame()
result_df['Country/Territory'] = country
result_df['Continent'] = continent
result_df['Capital'] = capital

result_df = result_df[result_df['Country/Territory'] == country_param]

if btn:
    st.header('Here is your requested data : ')
    st.dataframe(result_df)



