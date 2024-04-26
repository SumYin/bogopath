import streamlit as st
import pandas as pd
import graphviz

st.write("""
# Bogo-Sort Demo
This is a demo of the bogosort algorithm where you can enter your own custom graph and the algorithm will try to solve it.
""")

graph=[("a", "b"), ("b", "c")]

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df