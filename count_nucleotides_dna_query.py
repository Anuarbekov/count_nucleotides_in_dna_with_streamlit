import altair as alt
import streamlit as st
import pandas as pd
st.write("""
# DNA Nucletide Web App

This app counts the nucleotide composition of DNA query!

***
""")
#inputing the dna sequence
st.header("Enter DNA sequence")
sequence_input = '>DNA query\nGAAGACAACCGA\nGAAAAC'
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
"""
)
#prints the input
st.header('YOUR INPUT (DNA QUERY)')
sequence

#prints the output
st.header('OUTPUT (DNA Nucleotide Count)')
# 1 - dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
    return d
X = DNA_nucleotide_count(sequence)


X
st.write("""
***
"""
)
# 2 - in text form
st.subheader('2. Print text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')

st.write("""
***
"""
)
# 3 - dataframe
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename(columns = {0: 'count'})
df.reset_index(inplace=True)
df = df.rename(columns = {'index': 'nucleotide'})
st.write(df)

st.write("""
***
"""
)
# 4 - barchart
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  #control width of each chart(initially width is thin)
)
st.write(p)
