import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
plt.style.use('ggplot')

with st.sidebar:
    st.subheader('Muhammad Rizq Ramadhan')
    st.write('Bike Dataset Analysis')
    
with st.sidebar:
    add_radio = st.radio(
        "Dashboard:",
        ("Conditions vs Total User", 
        "Total User by Working Day", 
        "Highest and Lowest Total User by Hour")
    )

st.subheader(add_radio)

day = pd.read_csv('all_day.csv')
hour = pd.read_csv('all_hour.csv')

colors = ["#db0f0f", "#81878c", "#81878c", "#81878c", "#81878c"]


if add_radio == "Conditions vs Total User":
    ###TODO###
    # st.subheader("Relationship Between Season And Temperature For Total Users")
    user_v_season = round(day.groupby(by=['season']).agg({
        'temprature': 'mean',
        'feel_temprature': 'mean',
        'total_user': 'sum'
    }), 2).reset_index().sort_values(by='total_user', ascending=False)
        
    fig, ax = plt.subplots()
    
    ax.set_title("Season vs Total User", loc="center", fontsize=15)
    graph = sns.barplot(data=user_v_season, x='season', y='total_user', palette=colors)    
    for i in graph.containers:
        ax.bar_label(i, color='black', fmt='%d')
    st.pyplot(fig)
    
    ###TODO###
    
    fig, ax = plt.subplots()
    
    ax.set_title("Temprature In Each Season", loc="center", fontsize=15)
    graph = sns.barplot(data=user_v_season, x='season', y='temprature', palette=colors)    
    for i in graph.containers:
        ax.bar_label(i, color='black', fmt='%g')
    st.pyplot(fig)
    
    ###TODO###
    
    weather = round(day.groupby(['weather_sit']).agg({
        'temprature': 'mean',
        'feel_temprature': 'mean',
        'total_user': 'sum'
    }), 2).sort_values(by='temprature', ascending=False).reset_index()

    fig, ax = plt.subplots()
    
    ax.set_title("Weather Situation vs Total User", loc="center", fontsize=15)
    graph = sns.barplot(data=weather, x='weather_sit', y='total_user', palette = colors)
    for i in graph.containers:
        ax.bar_label(i, color='black', fmt='%d')
    st.pyplot(fig)
    
    ###TODO### 
    
    fig, ax = plt.subplots()
    
    ax.set_title("Temprature In Each Weather Situation", loc="center", fontsize=15)
    graph = sns.barplot(data=weather, x='weather_sit', y='temprature', palette = colors)
    for i in graph.containers:
        ax.bar_label(i, color='black', fmt='%g')
    st.pyplot(fig)
    
    ###TODO###
    
    hour_by = hour.groupby(by=['season','hour']).agg({
        'casual_user': 'sum',
        'registered_user': 'sum',
        'total_user': 'sum',
    }).reset_index()
    
    fig, ax = plt.subplots()
    ax.set_title("Hourly Bike Usage by Season", loc="center", fontsize=15)
    graph = sns.lineplot(data=hour_by, x='hour', y='total_user', hue='season')
    st.pyplot(fig)

elif add_radio == "Total User by Working Day":

    ###TODO###
    
    work_day = day.groupby(by=['working_day']).agg({
        'total_user': 'sum'
    }).sort_values(by='total_user', ascending=False).reset_index()
    
    fig, ax = plt.subplots()
    
    ax.set_title("Number of Total User by Working Day", loc="center", fontsize=15)
    graph = sns.barplot(data=work_day, x='working_day', y='total_user', ax=ax)
    for i in graph.containers:
        ax.bar_label(i, color='black', fmt='%d')
    
    st.pyplot(fig)
    
    ###TODO###
    
    work = day[day['working_day'] == 'yes'].groupby(by='week_day').agg({
        'total_user': 'sum'
    }).sort_values(by='total_user', ascending=False).reset_index()

    fig, ax = plt.subplots()
    
    ax.set_title("Number of Total User That Work by Week Day", loc="center", fontsize=15)
    graph = sns.barplot(data=work, x='week_day', y='total_user', palette=colors, ax=ax)
    for i in graph.containers:
        ax.bar_label(i, color='black', fmt='%d')
        
    st.pyplot(fig)
    
    
elif add_radio == "Highest and Lowest Total User by Hour":
    
    colors0 = ["#81878c", "#81878c", "#db0f0f", "#81878c", "#81878c"]
    colors1 = ["#db0f0f", "#81878c", "#81878c", "#81878c", "#81878c"]

    ###TODO### 
    
    hour_v_user = hour.groupby(by='hour').agg({
        'total_user': 'sum'
    }).reset_index()
        
    ###TODO###
    
    fig, ax = plt.subplots()
    
    ax.set_title('Highest total user by hour', loc="center", fontsize=15)
    graph = sns.barplot(data=hour_v_user.sort_values(by='total_user', ascending=False).head(),
                        x='hour', y='total_user', palette=colors0)
    for i in graph.containers:
        ax.bar_label(i, color='black', fmt='%d')
    st.pyplot(fig)
    
    ###TODO###
    
    fig, ax = plt.subplots()
    
    ax.set_title('Lowest total user by hour', loc="center", fontsize=15)
    graph = sns.barplot(data=hour_v_user.sort_values(by='total_user', ascending=True).head(),
                        x='hour', y='total_user', palette=colors1)
    for i in graph.containers:
        ax.bar_label(i, color='black', fmt='%d')
    st.pyplot(fig)