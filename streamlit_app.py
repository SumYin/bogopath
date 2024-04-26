import streamlit as st
import pandas as pd
import math
import graphviz

st.write("""
# Bogo-Sort Demo
This is a demo of the bogosort algorithm where you can enter your own custom graph and the algorithm will try to solve it.
""")

edges = st.slider('how many edges do you want?', 1, 10, 1)
    
cpaths = st.slider('how many possible simple paths will it have?', 0, edges, 1)

graph=[("a", "b")] * cpaths + [("a", "c")] * (edges - cpaths)

df = pd.DataFrame(graph)

df

f = graphviz.Graph('finite_state_machine', filename='fsm.gv')
f.attr(rankdir='LR', size='8,5')

f.attr('node', shape='circle')
f.attr(bgcolor="transparent")

for i in graph:
    f.edge(i[0], i[1])

st.graphviz_chart(f)
