import streamlit as st
import pandas as pd

st.title("Streamlit Write :100:")
st.write("We learn Streamlit!")

l1 = [1, 2, 3, 4, 5]
st.write(l1)

# using magic

'Display using magic :sparkles:'

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df
