import streamlit as st
import pandas as pd
import numpy as np

st.title("First test Streamlit Application!")

with st.sidebar:
    st.header("About app")
    st.write("Table of contents")
    st.radio("Select one:", [1, 2, 3, 4])

st.header('This is a header with a divider', divider='blue')

st.markdown("This is created using st.markdown")
# Insert a chat message container.
with st.chat_message("user"):
    st.write("Test Chat Application")
    st.line_chart(np.random.randn(30, 3))

# Display a chat input widget inline.
with st.container():
    st.chat_input("Say something")

st.subheader("x2 Column Header")
col1, col2 = st.columns(2)

with col1:
    x = st.slider("Choose an x value", 1, 10)
with col2:
    st.write("The value of :red[***x***] is", x)

st.subheader("Area Chart Header")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

st.button("Click me")



#streamlit run streamlit_app.py