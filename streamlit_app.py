import streamlit as st
import math
import graphviz
from bogopath import *
import plotly.express as px
import scipy
import pandas as pd
# py -3.12 -m streamlit run streamlit_app.py

st.write("""
# Bogo-Path Demo
This is a demo of the bogopath algorithm where you can enter your own custom graph and the algorithm will try to solve it.
""")

edges = st.slider('how many edges do you want?', 1, 10, 2)
    
cpaths = st.slider("""
how many possible simple paths will it have? 
# *Will defult to 1 if set to zero as the algorithm would run forever*""", 0, edges, 1)

if cpaths == 0:
    cpaths = 1

graph=[("a", "b")] * cpaths + [("a", "c")] * (edges - cpaths)

# df = pd.DataFrame(graph)

# df

st.write("""
## Graph Generated
Our goal is a simple path from *a* to *b*.""")

f = graphviz.Graph('finite_state_machine', filename='fsm.gv')
f.attr(rankdir='LR', size='8,5')

tc="#FF4B4B"

f.attr('node', shape='circle')
f.attr(bgcolor="transparent")
f.attr('edge', color=tc, penwidth="2")
f.attr('node', color=tc, penwidth="2")
f.attr('node', fontcolor=tc)

for i in graph:
    f.edge(i[0], i[1])

st.graphviz_chart(f)


vertex_start="a"
vertex_end="b"

limit=2000
if edges > 5:
    limit=500
number_of_iterations=st.slider('how many times to run the algorithm?', 0, limit, 500, 50)
if number_of_iterations == 0:
    number_of_iterations = 1

if st.button('Run Algorithm'):
    progress_text = "Running the algorithm..."
    progress_bar = st.progress(0, text=progress_text)  # Create a progress bar
    itterations = []

    for i in (range(number_of_iterations)):
        z=0
        path = []
        while check_path(path, vertex_start, vertex_end) == False:
            z+=1
            path = random_subgraph(graph)
            for edge in path:
                f.edge(edge[0], edge[1], color='blue')  # Change the color of the edge

        itterations.append(z)
        progress_bar.progress((i + 1) / number_of_iterations, text=progress_text)  # Update the progress bar
    # graph the histogram
    df = px.data.tips()
    df = pd.DataFrame({'value': itterations})
    fig = px.histogram(df, x="value", histnorm='probability density', color_discrete_sequence=[tc], marginal="box")
    fig.update_layout(
        title="Number of Iterations to find the correct path",
        xaxis_title="Iterations",
        yaxis_title="Frequency",
    )
    st.plotly_chart(fig)
    col1, col2, col3 = st.columns(3)

    col1.metric(label="Average Iterations vs Expected", value=str(sum(itterations)/len(itterations)), delta=str((sum(math.comb(edges, x) for x in range(1, edges+1))/cpaths)-(sum(itterations)/len(itterations))))
    col2.metric(label="Shortest Iteration", value=str(min(itterations)))
    col3.metric(label="Longest Iteration", value=str(max(itterations)))
