#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df_2020 = pd.read_csv('2020input8.csv', header=None, delim_whitespace=True, names=['Left Edge', 'Right Edge', 'Number of Students'])
df_2024 = pd.read_csv('2024input8.csv', header=None, names=['Grades'])

#To find the mean of grouped data-2020 exams
# Calculate the centers of the intervals for 2020 exams
centers_2020 = (df_2020['Left Edge'] + df_2020['Right Edge']) / 2

# Calculates the weighted sum
weighted_sum = (centers_2020 * df_2020['Number of Students']).sum()

# Calculates the total frequency
total_frequency = df_2020['Number of Students'].sum()

# Calculates mean 
mean_2020  = weighted_sum / total_frequency

#To find standard deviation of grouped data-2020 exams
# Calculate the  variance
variance_2020 = ((df_2020['Number of Students'] * (centers_2020 - mean_2020)**2).sum()) / df_2020['Number of Students'].sum() - 1

#Calculate Standard deviation
std_dev_2020=np.sqrt(variance_2020)

# mean and standard deviation for 2024 distributions
mean_2024 = np.mean(df_2024['Grades'])
std_dev_2024 = np.std(df_2024['Grades'], ddof=1)

# Plots the histogram for 2020 exam data
plt.figure(figsize=(10, 6))
plt.hist( df_2020['Left Edge'], bins=df_2020["Right Edge"],weights=df_2020["Number of Students"] , color='skyblue',edgecolor="black", label='2020 Exam',density=True)

# Plots the histogram for 2024 exam data
plt.hist(df_2024['Grades'], bins='auto', alpha=0.5, color='orange',edgecolor="blue", label='2024 Exam',density=True)

# To Calculate value V for 2020 exam
N = df_2020["Number of Students"].sum()
percentile_value = (90 * N )/100

cumulative_freq = df_2020['Number of Students'].cumsum()

# Find the index of the value closest to 270
index_closest = (cumulative_freq - percentile_value).abs().idxmin()

# Get the value approximately equal to 270
index_value = cumulative_freq.iloc[index_closest]

M_90 = cumulative_freq.iloc[index_closest - 1]
class_at_index = df_2020.iloc[index_closest]

R_90 = class_at_index['Right Edge'] #Right edge of index class
L_90 = class_at_index['Left Edge'] # Left edge of index class
F_90 = class_at_index["Number of Students"] # Frequecy of index class
C_90 = R_90-L_90 #width of index class

V = P_90 = L_90 + (percentile_value - M_90) * C_90/F_90 #Calculates the V value

# Print mean, standard deviation, and V
plt.text(0.95, 0.95, f"Mean 2020: {mean_2020:.2f}\nStd Dev 2020: {std_dev_2020:.2f}\nMean 2024: {mean_2024:.2f}\nStd Dev 2024: {std_dev_2024:.2f}\nV: {V:.2f}\nStudent ID: {23030678}", transform=plt.gca().transAxes, ha='right', va='top', bbox=dict(facecolor='white', alpha=0.5))

# Add labels and title
plt.xlabel('Grades')
plt.ylabel('Distribution')
plt.title('Distribution of Students\' Grades')
plt.legend(loc="upper left")
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.xticks(centers_2020, rotation=45)
plt.tight_layout()

# Show the plot
plt.show()


# In[ ]:




