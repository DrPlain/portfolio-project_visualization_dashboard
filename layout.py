import streamlit as st 

def layout_settings_and_styling():
    # ------------------------LAYOUT CONFIGURATION----------------------------
    st.set_page_config(page_title="Visualization Dashboard",
                    page_icon=':bar_chart:',
                    layout='wide')
    st.markdown("""
    <style>
    .css-18ni7ap
    {
        background-color: #154c79; #header
    }
    .css-14xtw13
    {
        visibility: hidden;
    }

    .css-z5fcl4
    {
        background-color: white; #abdbe3
    }
    .css-vk3wp9
    {
        background-color: #154c79;#sidebar
    }
    .css-81oif8 
    {
        color: white;
        font-size: 20px;
    }
    footer 
    {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h1 style='text-align: center; color: #154c79;'>Data Visualization Dashboard</h1>
    """, unsafe_allow_html=True)

