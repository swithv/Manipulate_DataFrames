import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

st.title('Análise de Vendas')
relatorios_df = pd.read_csv('vendas_ansi.csv', encoding='ansi', sep=';')
tabela_df = relatorios_df[[
    'Número do Pedido', 
    'Data', 
    'Subtotal', 
    'Desconto', 
    'Valor do Frete', 
    'Total', 
    'Nome do comprador', 
    'Estado'
  ]].groupby('Número do Pedido').sum()

AgGrid(tabela_df, height=600)
