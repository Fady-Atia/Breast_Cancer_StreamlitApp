import streamlit as st 
import pandas as pd 
import pickle
import numpy as np  
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler 
def clean_data():
        data=pd.read_csv("C:/Users/fadys/Desktop/streamlit/multipage_cancer_app/model/data/breast-cancer.csv")
        data.drop(["id","diagnosis"],axis=1,inplace=True) 
        #print(data.head())
        return data 
def sidebars(data) :
        st.sidebar.header(" Measurements (predictors) ")
        inputs=[]
        for col in data.columns :
                 i=st.sidebar.slider(label=col ,min_value=float(0),max_value=float(data[col].max()),value=data[col].mean())
                 inputs.append(i)
        return inputs          
def model(input_data):
                model=pickle.load(open("C:/Users/fadys/Desktop/streamlit/multipage_cancer_app/model/model.pkl","rb"))
                scaler=pickle.load(open("C:/Users/fadys/Desktop/streamlit/multipage_cancer_app/model/scaler.pkl","rb"))
                cleaned_data=clean_data()
                scaler.fit(cleaned_data)
                scaled_data=scaler.transform(input_data)
                predicted=model.predict(scaled_data)
                st.subheader("state of patient:")
                if predicted[0]==1 :
                       
                        st.markdown('<span style="background-color:blue; color: white;">Benign😊</span>', unsafe_allow_html=True)
                        st.markdown('<span style="background-color: gray; color:white;"> Not have a cancer</span>', unsafe_allow_html=True)
                else:
                        
                        st.markdown('<span style="background-color: red; color: white;">**Malignant**😢</span>', unsafe_allow_html=True)
                        st.markdown('<span style="background-color: gray; color:white;">Have a cancer</span>', unsafe_allow_html=True)

                st.write("probability of being benign",model.predict_proba(scaled_data)[0][1])
                st.write("probability of being malignant",model.predict_proba(scaled_data)[0][0]) 
                st.write("This app can assist medical professionals in making a diagnosis but should not be used as a subsitute for a professionals diagnosis ")       

def radar_graph(input_data):
        scaler2=MinMaxScaler()
        data2=clean_data()
        input_scaled=scaler2.fit(data2)
        input_scaled=scaler2.transform(input_data)

        categories = ['Radius','Texture','Perimeter',
                      'Area', 'smoothness','compactness',
                      'Concavity','Concave points','symmetry',
                      'Fractal_dimension']      

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
                       r=list(input_scaled[0][0:10]),
                       theta=categories,
                       fill='toself',
                       name='Mean'
                                       ))
        fig.add_trace(go.Scatterpolar(
                        r=list(input_scaled [0][10:20]),
                        theta=categories,
                        fill='toself',
                        name='Standarized'
                                        ))
        fig.add_trace(go.Scatterpolar(
                       r=list(input_scaled[0][20:30]),
                       theta=categories,
                       fill='toself',
                       name='Worst'
                                       ))

        fig.update_layout( 
        polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0,1]
        )),
        showlegend=True
                          )
        return fig 



def main():
       
        st.set_page_config(page_title="Breast cancer",page_icon='☠️'
                            ,layout="wide",initial_sidebar_state="expanded")
        data=clean_data() 
        

        st.title("# Breast Cancer Diagonises **ML** App detection ")

        input=sidebars(data)
        st.subheader("Input Data")
        S=pd.DataFrame(data=np.array(input).reshape(1,-1),columns=data.columns)
        #st.write(np.array(input).reshape(1,-1))
        st.write(S)  
        input_data=np.array(input).reshape(1,-1)
        #st.write(input_data)
        col1,col2=st.columns([4,1])
        with col1 :
                showed_rader=radar_graph(input_data)
                st.plotly_chart(showed_rader)

                
                
        with col2:
              
              model(input_data)
                           
        


if __name__=="__main__":
        main()        