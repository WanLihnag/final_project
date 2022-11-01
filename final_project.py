import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
plt.style.use('seaborn')

st.title('Final project by group 54')

df = pd.read_csv('online_fraud.csv')
# df = df.sample(6666) 
# df['isFraud'][df['isFraud'] == 1] = 'Fraud'
# df['isFraud'][df['isFraud'] == 0] = 'Not Fraud'
df = df.sort_values(by = 'amount', ignore_index= 'True',ascending= False)


amount_filter = st.slider('Minimal Amount of transaction:', 0, 5000000, 50000)

step_filter = st.sidebar.multiselect(
     'Step Selector',
     df.step.unique(),  # options
     df.step.unique())  # defaults

form = st.sidebar.radio("Fraud Selector",('Fraud','Not Fraud','ALL'))

df = df[df.amount >= amount_filter]
df = df[df.step.isin(step_filter)]

if form == 'Fraud':
    df = df[df.isFraud == 1]
elif form == 'ALL':
    df = df[(df.isFraud == 1) | (df.isFraud == 0)]
else :
    df = df[df.isFraud == 0]

df[['step','oldbalanceOrg','type','amount','isFraud']]


fig, ax = plt.subplots()
val = df.type.hist(bins=9)
st.pyplot(fig)

data = df[df.isFraud == 1]

# figa, axa = plt.subplots(figsize=(13,8))

# type = data["type"].value_counts()
# transactions = type.index
# quantity = type.values
# figure = px.pie(data, values=quantity, names=transactions, hole = 0.5, title="Distribution of Transaction Type")
# figure.show()

# d = pd.Series(df.amount,df.oldbalanceOrg)
fig , ax1 = plt.subplots()
df.plot.scatter(x='oldbalanceOrg',y='amount',ax=ax1)
ax1.set_xlabel('balance')
ax1.set_ylabel('amount')
plt.xticks(rotation=0)
st.pyplot(fig)

# ticket_price = df.sort_values(by = 'amount', ignore_index= 'True',ascending= False)#ignore_index
# ticket_price.amount.plot().set_ylabel('amount')