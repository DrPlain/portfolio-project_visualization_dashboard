import streamlit as st
import pandas as pd
from layout import layout_settings_and_styling
import plotly.express as px

# import matplotlib.pyplot as plt
# -----------------LAYOUT CONFIGURATION AND STYLING-------------------
layout_settings_and_styling()

# ------------------------SIDE BAR-----------------------------------
# st.sidebar.title("Visualization Settings")
st.sidebar.markdown("""
<h1 style='text-align: left; color: white;'>Visualization Settings</h1>
""", unsafe_allow_html=True)

data_source = st.sidebar.selectbox("Select data to visualize",
                                   ['Use demo data set', 'Upload data'])

if data_source == 'Use demo data set':
    gapmider = px.data.gapminder()
    df = gapmider.query('year > 2000')
    # df = pd.read_csv('demo_data.csv')
    st.markdown("""
    <h1 style='text-align: left;'>Demo Data set</h1>
    """, unsafe_allow_html=True)

    st.write(df)

elif data_source == "Upload data":
    uploaded_file = st.sidebar.file_uploader(label='Upload your CSV or Excel files',
                                             type=['csv', 'xlsx'])
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.markdown("""
            <h1 style='text-align: left;'>Uploaded Data Set</h1>
            """, unsafe_allow_html=True)
            st.write(df)
        except Exception as err:
            df = pd.read_excel(uploaded_file)
            st.write(df)

# Selection of chart type for visualization
try:
    chart_type = st.sidebar.selectbox("Select the chart type",
                                      ['Bar chart', 'Scatter plot', 'Histogram', 'Line plot', 'Pie chart'])

    if chart_type == 'Bar chart':
        nominal_variables = []
        numerical_variables = []
        for key in df.keys():
            if df[key].dtypes == 'object':
                nominal_variables.append(key)
            elif df[key].dtypes == 'int64' or df[key].dtypes == 'float64':
                numerical_variables.append(key)
        x_axis = st.sidebar.selectbox("X axis", sorted(nominal_variables))
        # height = st.sidebar.selectbox("Height", numerical_variables)
        fig = px.bar(df,
                        #  x=height,
                         x=x_axis)
        # ax.scatter(df[x_axis], df[y_axis])
        st.markdown("""
    <h1 style='text-align: left;'>Chart</h1>
    """, unsafe_allow_html=True)

        st.plotly_chart(fig)

    if chart_type == 'Pie chart':
        nominal_variables = []
        for key in df.keys():
            if df[key].dtypes == 'object':
                nominal_variables.append(key)
        names = st.sidebar.selectbox("Select variable", sorted(nominal_variables))
        fig = px.pie(df,
                    names=names)
        # ax.scatter(df[x_axis], df[y_axis])
        st.markdown("""
    <h1 style='text-align: left;'>Chart</h1>
    """, unsafe_allow_html=True)

        st.plotly_chart(fig)


    if chart_type == 'Scatter plot':
        variables = []
        color_legend = []
        for key in df.keys():
            if df[key].dtypes == 'int64' or df[key].dtypes == 'float64':
                variables.append(key)
            elif df[key].dtypes == 'object':
                color_legend.append(key)
        x_axis = st.sidebar.selectbox("X axis", sorted(variables))
        y_axis = st.sidebar.selectbox("Y axis", sorted(variables))
        legend = st.sidebar.selectbox("Color by", sorted(color_legend))

        fig = px.scatter(df,
                         x=x_axis,
                         y=y_axis,
                         color=legend)
        # ax.scatter(df[x_axis], df[y_axis])
        st.markdown("""
    <h1 style='text-align: left;'>Chart</h1>
    """, unsafe_allow_html=True)
        st.plotly_chart(fig)

    if chart_type == 'Histogram':
        variables = []
        for key in df.keys():
            if df[key].dtypes == 'int64' or df[key].dtypes == 'float64':
                variables.append(key)
        x_axis = st.sidebar.selectbox("X axis", sorted(variables))
        bar_no = st.sidebar.slider("Select number of bars to display",
                  min_value=5, max_value=20)
        fig = px.histogram(df,
                      x=x_axis)
        
        st.markdown("""
    <h1 style='text-align: left;'>Chart</h1>
    """, unsafe_allow_html=True)
        st.plotly_chart(fig)

        
except Exception as err:
    pass