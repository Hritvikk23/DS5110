#!/usr/bin/env python
# coding: utf-8

# # Coffee Cart Sales Analysis

# In[1]:

import os
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("data/raw/coffee_sales.csv")
df.head()


# In[3]:


df["revenue"] = df["quantity"] * df["unit_price"]
df.head()


# ### Daily revenue

# In[4]:


daily = df.groupby("date")["revenue"].sum()
avg_daily = daily.mean()
print(f"{daily}")


# ### Average Daily Revenue

# In[5]:


print(f"Average daily revenue: ${avg_daily:.2f}")


# ### Compare revenue: random 50/50 split of the days

# In[6]:


shuffled = df.sample(frac=1, random_state=50)
half = len(shuffled) // 2
group_a = shuffled.iloc[:half]
group_b = shuffled.iloc[half:]
print(f"Group A mean revenue: {group_a['revenue'].mean():.2f}")
print(f"Group B mean revenue: {group_b['revenue'].mean():.2f}")


# ### Revenue by product

# In[7]:


by_product = df.groupby("product")["revenue"].sum()
by_product.plot(kind="bar")
plt.ylabel("Total revenue ($)")
plt.title("Revenue by product")

os.makedirs("output", exist_ok=True)
plt.savefig("output/revenue_by_product.png")
plt.show()


# ### Takeaway
# Latte brings in the most total revenue this month.
