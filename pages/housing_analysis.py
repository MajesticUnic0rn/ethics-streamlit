import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Sample data
home_price = 300000
annual_rent = 12000
mortgage_rate = 3.5  # in percent
years = 30
rent_increase_rate = 2  # Annual increase in rent in percent

# Mortgage calculation
monthly_rate = mortgage_rate / 100 / 12
n_payments = years * 12
monthly_mortgage = home_price * (monthly_rate * (1 + monthly_rate) ** n_payments) / ((1 + monthly_rate) ** n_payments - 1)
annual_mortgage = monthly_mortgage * 12

# Generate data for each year
data = []
for year in range(1, years + 1):
    total_rent = annual_rent * ((1 + rent_increase_rate / 100) ** year)
    total_mortgage = annual_mortgage * year
    savings = total_rent - total_mortgage
    data.append({'Year': year, 'Total Rent': total_rent, 'Total Mortgage': total_mortgage, 'Savings': savings})

df = pd.DataFrame(data)


sns.set_theme(style="whitegrid")

# Plot
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Total Rent', data=df, label='Total Rent')
sns.lineplot(x='Year', y='Total Mortgage', data=df, label='Total Mortgage')

plt.title('Comparison of Total Rent vs Total Mortgage Over Time')
plt.xlabel('Year')
plt.ylabel('Total Cost ($)')
plt.legend()
st.pyplot(plt)


plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Savings', data=df)

plt.title('Savings: Renting vs Owning Over Time')
plt.xlabel('Year')
plt.ylabel('Savings ($)')
plt.axhline(0, color='red', lw=2, ls='--')  # Reference line at 0
st.pyplot(plt)
