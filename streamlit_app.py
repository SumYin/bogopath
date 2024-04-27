import streamlit as st
import math
import graphviz
from bogopath import *

# py -3.12 -m streamlit run streamlit_app.py

st.write("""
# Bogo-Sort Demo
This is a demo of the bogosort algorithm where you can enter your own custom graph and the algorithm will try to solve it.
""")

edges = st.slider('how many edges do you want?', 1, 10, 1)
    
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

limit=10000
if edges > 5:
    limit=5000
number_of_iterations=st.slider('how many times to run the algorithm?', 1, limit, 1000)


if st.button('Run Algorithm'):
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


    st.write(f"""
        ## Results
        #### Average Iterations: {sum(itterations)/len(itterations)} - {len(itterations)}/{sum(itterations)}
        #### Expected Iterations: {sum(math.comb(edges, x) for x in range(1, edges+1))/cpaths}
        #### Longest Iteration: {max(itterations)}
        #### Shortest Iteration: {min(itterations)}
    """)
