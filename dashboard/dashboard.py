import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

# Gettering data
all_df = pd.read_csv("all_data.csv")

# plot number of daily orders (2021)
st.header('Nama : Muchammad Muchib Zainul Fikry')
st.header('Email : muchammadmuchib@gmail.com')
st.header('Dicoding Collection Dashboard :sparkles:')
st.subheader('Dashboard Humidity & Temperature')

# Dashboard monitoring realtime
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))
sns.barplot(x="instant", y="hum", data=all_df.head(30), palette=None, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Realtime Data Performing Humidity", loc="center", fontsize=15)
ax[0].tick_params(axis ='y', labelsize=12)

sns.barplot(x="instant", y="temp", data=all_df.head(30), palette=None, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Realtime Data Performing Temperature", loc="center", fontsize=15)
ax[1].tick_params(axis ='y', labelsize=12)

st.pyplot(fig)

x = "Keterangan grafik sumbu X gambar dibawah merupakan day dihitung dari awal bulan sampai akhir bulan."
y ="Keterangan grafik sumbu Y gambar dibawah merupakan nilai derajat temperature dan humidity."

st.text(x)
st.text(y)
st.caption('Copyright © Dicoding 2023')
