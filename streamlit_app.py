import streamlit as st
import pandas as pd

st.title('Meu app de finanças')
st.header('Minha tabela financeira:')

data = pd.read_csv('https://raw.githubusercontent.com/rafabandoni/finance-streamlit-app/main/fake-data.csv')
data.set_index(['data'], inplace=True)
st.dataframe(data)

data['gastos_fixos'] = data['agua'] + data['luz'] + data['gás'] + data['internet'] + data['aluguel'] + data['condominio']
data['gastos_variaveis'] = data['cartao_credito']
data['sobra_mes'] = data['gastos_fixos'] + data['gastos_variaveis'] - data['salario']

st.dataframe(data)