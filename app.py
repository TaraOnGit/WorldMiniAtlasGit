import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

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
plot_value = ['bar', 'scatter', 'line', 'histogram']
plot_name = ['Bar', 'Scatter', 'Line', 'Histogram']
pt = st.sidebar.radio('Plot Type : ', plot_name, captions=plot_value, horizontal=True)
x = None
btn1 = st.sidebar.button('Get Data')

col1, col2 = st.columns(2)

if btn1:
    with col1:
        cont = world[world['Country/Territory'] == country_param]['Continent'].values
        cap = world[world['Country/Territory'] == country_param]['Capital'].values
        st.header('Country : ' + country_param)
        st.subheader('Continent : ' + str(cont)[2:-2])
        st.subheader('Capital : ' + str(cap)[2:-2])
        param1_val = world[world['Country/Territory'] == country_param][param1].values
        param2_val = world[world['Country/Territory'] == country_param][param2].values
        st.subheader(str(param1)+' : '+str(param1_val))
        st.subheader(str(param2)+' : '+str(param2_val))


    with col2:
        if pt == 'Bar' :
            st.write(px.bar(world,x=param1,y=param2,color=continent,hover_data='Country/Territory',
                            animation_frame='Growth Rate'))

        elif pt == 'Scatter' :
            st.write(px.scatter(world, x=param1, y=param2, color=continent, hover_data='Country/Territory',
                            animation_frame='Growth Rate'))

        elif pt == 'Line' :
            st.write(px.line(world, x=param1, y=param2, color=continent, hover_data='Country/Territory',
                                animation_frame='Growth Rate'))

        elif pt == 'Histogram' :
            st.write(px.histogram(world, x=param1, y=param2, color=continent, hover_data='Country/Territory',
                                animation_frame='Growth Rate'))





