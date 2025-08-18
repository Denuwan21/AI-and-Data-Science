import streamlit as st
from streamlit import session_state as state
from streamlit_extras.app_logo import add_logo

import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt

api = "vBiqua3OPNitEb8j87hVmfNwM32PHXQM6y3WKdSD"

st.set_page_config(
    page_title="Data Analysis System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)



st.markdown("""
    <style>
        .stPlot {
            background-color: #161616 !important;
        }
        .css-1p8k9yc {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)


def data(file):
    df = pd.read_csv(file)
    df.dropna(axis=1, how='all', inplace=True)
    return df


file_data = st.sidebar.file_uploader("Upload CSV File")

if file_data is None:
    st.info("No file uploaded. Please upload a CSV file to proceed.", icon="ℹ️")
    st.stop()

df = data(file_data)








st.sidebar.write("---")


st.sidebar.title("Filters")

Cty = st.sidebar.multiselect(
    "Select City",
    options=df["City"].unique(),
    default=df["City"].unique() 
)

Prod = st.sidebar.multiselect(
    "Select Product",
    options=df["Product"].unique(),
    default=df["Product"].unique() 
)

Pay = st.sidebar.multiselect(
    "Select Payment Method",
    options=df["Purchase Type"].unique(),
    default=df["Purchase Type"].unique() 
) 
st.sidebar.write("---")


#df_selection = df.query(
#    "City == @City and Product == @Product and `Purchase Type` == @Purchase_Type"
#)





Col_1, Col_2, Col_3, Col_4 = st.columns(4)

filterd_df = df[
    (df["City"].isin(Cty)) &(df["Product"].isin(Prod)) & (df["Purchase Type"].isin(Pay))
]

product_Beverage_count = (filterd_df[filterd_df['Product']=="Beverages"]['Quantity']).sum().astype(int)
product_Fries_count = (filterd_df[filterd_df['Product']=="Fries"]['Quantity']).sum().astype(int)
product_Burger_count = (filterd_df[filterd_df['Product'] == "Burgers"]['Quantity']).sum().astype(int)
product_C_Sandwich_count = (filterd_df[filterd_df['Product'] == "Chicken Sandwiches"]['Quantity']).sum().astype(int)

with Col_1:
    st.subheader(product_Beverage_count)
    st.write("Total Count of Beverage")
    
     

with Col_2:
    st.subheader(product_Fries_count)
    st.write("Total Count of Fries")
    
     

with Col_3:
    st.subheader(product_Burger_count)
    st.write("Totol Count of Burgers ")
    

with Col_4:
    st.subheader(product_C_Sandwich_count)
    st.write("Totol Count of Chicken Sandwiches") 

st.write("---")


with st.expander("Data Preview"):
    st.write(df)

st.write("Total Amount by Date")
chart = st.bar_chart(
    data=filterd_df.set_index("Date")["Total Amount"],
    use_container_width=True,
    height=400
)

Col_1, Col_2= st.columns(2)
with Col_1:
    st.write("Total Amount by City")
    city_amount = filterd_df.groupby("City")["Total Amount"].sum().reset_index()
    city_bar = st.line_chart(city_amount.set_index("City"))
    

with Col_2:
    Pay_type = filterd_df.groupby("Purchase Type")["Total Amount"].sum().reset_index()
    fig = px.pie(Pay_type, names='Purchase Type', values='Total Amount', title='Total Amount by Purchase Type')
    st.plotly_chart(fig, use_container_width=True)
    




st.write("Total Amount by City & Purchase Type")
hist = filterd_df.groupby(['City', 'Purchase Type'])['Total Amount'].sum().reset_index()
fig = px.bar(
    hist,
    x="Purchase Type",
    y="Total Amount",
    color="City",
    barmode="group",
    title="Total Amount Distribution by City & Purchase Type"

)
st.plotly_chart(fig, use_container_width=True)


st.write("Total Amount by Product")
product_amount = filterd_df.groupby("Product")["Total Amount"].sum().reset_index()
st.bar_chart(product_amount.set_index("Product"))








     















