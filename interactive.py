import streamlit as st
import pandas as pd

# title
st.title("Interactive Elements")


#sidebar
st.sidebar.title("This is my Sidebar")
st.sidebar.selectbox(label="Select a color",
                     options=["red", "green", "blue"])

# file upload
file = st.file_uploader(label="Upload a file")

df = pd.read_csv(file)

df.to_csv("./data/temp.csv", index=None)

st.dataframe(df.head())

# button
btn = st.button(label="Click Me")

st.write(btn)

if btn:
    st.write("button was pressed")
    
# checkbox
check = st.checkbox(label="Display Plot",value=True)
st.write(check)

sample_dict = {1: {
    "name": "Mukesh",
    "age": 30,
    "city": "Mumbai"
},
    2: {
        "name": "Rahul",
        "age": 23,
        "city": "Pune"
    },
    3: {
        "name": "Anaya",
        "age": 27,
        "city": "Indore"
    }}

def fmt_func(text):
    return text.upper()

# radio button
radio_button = st.radio(label="Select me", options=[
    "Option 1",
    "Option 2",
    "Option 3"
], index=1, help="Select one of the options", format_func=fmt_func)

st.write(radio_button)

if radio_button == "Option 3":
    st.json(sample_dict)
    
# selectbox
select_box = st.selectbox(label="Select Fruit",
              options=["Apple", "Banana", "Cherry"], index=1,
              )

st.write(select_box)

# multiselect

multi = st.multiselect(label="Select Cities",
               options=["Mumbai", "Pune", "Indore", "Delhi"])


st.write(multi)

# select slider

st.select_slider(label="Select a number",
                 options=["A", "B" , "C"])


# slider
s = st.slider(label="Select a number from range slider",
          min_value=1, max_value=20, step=2, value=(5,7))

st.write(s)

# number input

num = st.number_input(label="Enter a number",
                min_value=0, max_value=100, help="add number in integers")

st.write(num)

# date input

date = st.date_input(label="Select a date", format="DD/MM/YYYY")

st.write(date)


# text input
name = st.text_input(label="Enter your name")
st.write(name)


# text area
area = st.text_area(label="Enter the text")
st.write(area)

