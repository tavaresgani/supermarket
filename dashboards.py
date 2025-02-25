import streamlit as st
import plotly.express as px
import pandas as pd


#ocupar a tela toda
st.set_page_config(layout="wide")

#faturamento por unidade...
#tipo de produto mais vendido, contribuição por filial
#desempenho das formas de pagamento
#como estão as avaliações das filiais
df = pd.read_csv("supermarket_sales (cópia).csv", sep=";", decimal=",")

#trasnformando em data
df["Date"] = pd.to_datetime(df["Date"])
df["Date"]
#Ordenando
df = df.sort_values("Date")

#concatenando mês e ano
df["Month"] =  df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

#caixa de seleção para selecionar o mês
month = st.sidebar.selectbox("Mês", df["Month"].unique())

#Filtrar o mês
df_filtered = df[df["Month"] == month]
df_filtered

#criando duas caixas de coluna divididos por 2 e 3

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

#Plotando os gráficos

#Faturamento por unidade
fig_date =  px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)

#Por tipo de produto
fig_prod =  px.bar(df_filtered, x="Date", y="Product line", color="City", title="Faturamento por tipo de produto", orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

#Contribuição por filial
city_total =  df_filtered.groupby("City")[["Total"]].sum().reset_index() #agrupando os dados
fig_city = px.bar(df_filtered, x="City", y="Total", title="Faturamento por filial") #geração do grafico
col3.plotly_chart(fig_city, use_container_width=True) #exibindo

#Faturamento por tipo de pagamento
fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)

#Avaliação média por cidade
city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(df_filtered, y="Rating", x="City", title="Avaliação")
col5.plotly_chart(fig_rating, use_container_width=True)

