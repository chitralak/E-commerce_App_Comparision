import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Fast Delivery Agent Reviews.csv")
st.title("Ecommerce App Comparision")
#st.dataframe(df.head())
#st.dataframe(df.isnull().sum())
#st.write(df['Agent Name'].unique())
#st.write(df['Order Accuracy'].unique())
#User input

Agent = st.multiselect("Select the Apps", df['Agent Name'].unique())
metric=st.selectbox("Select a comparision Metric",["Rating","Delivery Time(min)","Order Accuracy"])
Chart_type=st.selectbox("Select Chart Type",["Bar Chart","Pie Chart"])
if len(Agent)>0:
        if metric=="Rating":
            cols=st.columns(len(Agent))
            for i, app in enumerate(Agent):
                app_data=df[df['Agent Name']==app]
                avg_rating=round(app_data['Rating'].mean(),2)
                cols[i].metric(label="{} Rating".format(app),value = avg_rating)
        elif metric=="Delivery Time(min)":
             cols=st.columns(len(Agent))
             for i, app in enumerate(Agent):
                app_data=df[df['Agent Name']==app]
                delivery_time = round(app_data['Delivery Time (min)'].mean(),2)
                cols[i].metric("Delivery Time",value = delivery_time)
        elif metric=="Order Accuracy":
            cols=st.columns(len(Agent))
            for i, app in enumerate(Agent):
                app_data=df[df['Agent Name']==app]
                order_accuracy =round((app_data['Order Accuracy']=="Correct").mean()*100,2)
                cols[i].metric("Order Accuracy",value = order_accuracy)
       
else:
    st.write("please select atleast one app to compare")
data=[]
for app in Agent:
    a=df[df['Agent Name']==app]
    if metric=="Rating":
        value=a['Rating'].mean()
    elif metric=="Delivery Time(min)":
        value=a['Delivery Time (min)'].mean()
    elif metric=="Order Accuracy":
        value=(a['Order Accuracy']=="Correct").mean()*100
    data.append({'App':app,'Value':round(value,2)})

    #convert to new dataframe
    chart_df=pd.DataFrame(data)
    #Bar Chart
    if Chart_type=="Bar Chart":
        st.bar_chart(data=chart_df.set_index('App'))
    elif Chart_type=="Pie Chart":
        plt.figure(figsize=(6,6))
        plt.pie(chart_df['Value'],labels=chart_df['App'],autopct='%1.1f%%')
        plt.title("{} Comparision".format(metric))
        st.pyplot(plt)








