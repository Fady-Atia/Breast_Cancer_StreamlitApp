import streamlit as st 
from streamlit_lottie import st_lottie
import json
import pandas as pd 
import plotly.express as px
def lottie(path:str):
    with open(path,"r") as f :
        return json.load(f)
       
       
def main():
           hi=lottie("multipage_cancer_app/hi.json")
           st.set_page_config(page_title="Breast cancer",layout="wide",initial_sidebar_state="expanded",page_icon="🔍")
           with st.container() :
                        col1,col2=st.columns(2)
                        with col1 :
                             st.write("<span style='font-size: 24px;'>:blue[Hi ,I am Fady] 👋</span>", unsafe_allow_html=True) 
                             st.write("<span style='font-size: 29px;'>A Machine Learning Engineer From Cairo </span>", unsafe_allow_html=True)
                             st.write("**I am passionate about the field of artificial intelligence, especially machine learning and deep learning**")
                             st.write("**and excited to link this with practical applications**") 
                             st.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                        with col2 :
                            st_lottie(hi,height=200,width=300)
    
           st.subheader("**Defination of Breast cancer:** ")
           st.write('''Breast cancer is the most common cancer amongst women in the world. It accounts for 
                  25 of all cancer cases, and affected over 2.1 Million people in 2015
                   alone. It starts when cells in the breast begin to grow out of control.
                   These cells usually form tumors that can be seen via X-ray or felt as lumps in the breast area''')
           st.subheader("**About Dataset** :")
           st.write("- I used a real dataset from kaggle and applied preproceesing on it")
           st.write("- the challenge is to classify tumors into malignant (cancerous) or benign(non-cancerous) ")
           st.write("- I used Logistic Regression as a model,It gave me an accuracy rate of 97%. ")
           data=pd.read_csv("multipage_cancer_app/model/data/breast-cancer.csv")
           st.subheader("sample of data :")
           st.write(data.sample(5))
           hist_chart=px.histogram(data_frame=data,x='diagnosis',color='diagnosis',color_discrete_sequence=['#a865c9','#f6abb6'])
           st.plotly_chart(hist_chart)
           st.subheader("About app and Who can use this App ? ")
           st.write("- A breast cancer detection applications are not a substitute for regular mammograms or other breast cancer screenings. However, they can be a useful supplement to traditional breast cancer screening methods." )
           st.write("- This application is used in laboratories and hospitals to assist the doctor in diagnosis")
           st.write("- It can also be used by women who are already diagnosed with breast cancer to monitor their condition and track their progress." )          
                  



                      
if __name__=="__main__":
    main()
