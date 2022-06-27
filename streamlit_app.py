import streamlit as st
import pandas as pd

st.title('Meu app de finanças')
st.header('Minha tabela financeira:')

data = pd.read_csv('https://raw.githubusercontent.com/rafabandoni/finance-streamlit-app/main/fake-data.csv', decimal='.')
data.set_index(['data'], inplace=True)
data = data.round(2)
st.dataframe(data)

st.header('Tabela de gastos fixos e variáveis versus salário')

data['gastos_fixos'] = data['agua'] + data['luz'] + data['gás'] + data['internet'] + data['aluguel'] + data['condominio']
data['gastos_variaveis'] = data['cartao_credito']
data['sobra_mes'] = data['salario'] - (data['gastos_fixos'] + data['gastos_variaveis'])

st.dataframe(data[['gastos_fixos', 'gastos_variaveis', 'salario', 'sobra_mes']])

poupanca = data['sobra_mes'].sum()

st.write('O valor que você tem na poupança deveria ser de:', poupanca)