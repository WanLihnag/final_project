import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('Final project by group 54')

df = pd.read_csv('online_fraud.csv')
df = df.sample(6666) 






