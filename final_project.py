import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

st.title('Final project by group 54')

df = pd.read_csv('online_fraud.csv')
# df = df.sample(6666)
df['isFraud'][df['isFraud'] == 1] = 'Fraud'
df['isFraud'][df['isFraud'] == 0] = 'Not Fraud'
# df = df.sort_values(by = 'amount', ignore_index= 'True',ascending= False)


amount_filter = st.sidebar.slider(
    'Minimal Amount of transaction:', 0, 5000000, 50000)

step_filter = st.sidebar.multiselect(
    'Step Selector',
    df.step.unique(),  # options
    df.step.unique())  # defaults

form = st.sidebar.radio("Fraud Selector", ('ALL', 'Fraud', 'Not Fraud'))

df = df[df.amount >= amount_filter]
df = df[df.step.isin(step_filter)]

if form == 'Fraud':
    df = df[df.isFraud == 'Fraud']
elif form == 'ALL':
    df = df[(df.isFraud == 'Fraud') | (df.isFraud == 'Not Fraud')]
else:
    df = df[df.isFraud == 'Not Fraud']

st.subheader('The filtered table:')
df[['step', 'type', 'amount', 'isFraud']]

st.subheader('The quantity and proportion:')
c = df.groupby('isFraud').sum()
c['number'] = df.isFraud.value_counts()
c['percentage'] = (c.number / df.shape[0]).apply(lambda x: format(x, '.2%'))
c[['number', 'percentage']]


st.subheader('Payment type and quantities:')
fig, ax = plt.subplots()
val = df.type.hist(bins=9)
st.pyplot(fig)

st.subheader('A Line Chart Of The Ticket Price')
fig, ax0 = plt.subplots()
_step = df.sort_values(by='step', ignore_index='True', ascending=True)
_step.step.plot().set_ylabel('step')
st.pyplot(fig)


data = df[df.isFraud == 'Fraud']

# figa, axa = plt.subplots(figsize=(13,8))

# type = data["type"].value_counts()
# transactions = type.index
# quantity = type.values
# figure = px.pie(data, values=quantity, names=transactions, hole = 0.5, title= "Distribution of Transaction Type")
# figure.show()

st.subheader('Scatter plot of amount and balance')
fig, ax1 = plt.subplots()
df.plot.scatter(x='oldbalanceOrg', y='amount', ax=ax1)
ax1.set_xlabel('balance')
ax1.set_ylabel('amount')
# plt.ylim(0,2000000)
plt.xticks(rotation=0)
st.pyplot(fig)
