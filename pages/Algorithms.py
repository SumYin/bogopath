import streamlit as st

st.write("""
# Bogo-Path Algorithms
List of the algorithms that are used in the Bogo-Path project.
""")

st.write("""
### Caluclate number of possible subgraphs using # of edges
summation of the binomial coefficient
         """)
st.latex(r"""
   \sum_{n=1}^{x}\operatorname{nCr}\left(x,n\right)
    """)

st.write("""
### Caluclate Chance of selecting the correct graph depending on the number of edges and number of correct subgraphs
last equation as denominator
         """)
st.latex(r"""
   \frac{number \ of\ answers}{\sum_{n=1}^{x}\operatorname{nCr}\left(x,n\right)}
    """)

st.write("""
### Caluclate Expected itterations depending on the number of edges and number of correct subgraphs
last equation to the power of -1
         """)
st.latex(r"""
   \frac{\sum_{n=1}^{x}\operatorname{nCr}\left(x,n\right)}{number \ of\ answers}
    """)

st.write("""
### Caluclate # of edges in subgraph probability distribution
         """)
st.latex(r"""
   a = \sum_{x=1}^{l} {l \choose x}
    """)
st.latex(r"""
chances[x] = \frac{{l \choose x}}{a} \quad \text{for} \quad x \in [1, l]
    """)

st.latex(r"""
n = \text{random choice from } [1, l] \text{ with probabilities } chances
    """)

st.write("""
`l` is the number of edges in the graph g.\n
`x` is the number of edges in the subgraph.\n
`a` is the total number of possible subgraphs of g.\n
`chances` is the probability distribution of the number of edges in the subgraph.\n
`n` is the randomly selected number of edges for the subgraph.
    """)