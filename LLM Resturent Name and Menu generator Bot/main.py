import streamlit as st
import llm

st.header("Welcome to My Streamlit App")

st.sidebar.header("Navigation")
items = st.sidebar.selectbox("Choose an option", ["Sri Lanka", "United State", "India", "Japan", "Italian"])

custom_input = st.text_input("Or enter a custom country/restaurant:")

# Use custom input if provided, otherwise use sidebar selection
selected = custom_input if custom_input else items

if items:
    result = llm.LLM(selected)
    st.header(result["Resturent_Name"].strip())
    menu = result["menu_items"].strip().split(',')
    st.write("Menu Items:")
    for items in menu:
        st.write("-", items.strip())