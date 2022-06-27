import streamlit as st
import pandas as pd

st.title('Meu app de finanças')
st.header('Minha tabela financeira:')

data = pd.read_csv('https://raw.githubusercontent.com/rafabandoni/finance-streamlit-app/main/fake-data.csv')
st.dataframe(data)
