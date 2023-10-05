import streamlit as st
import json
from PIL import Image 
from streamlit_lottie import st_lottie
import sys 
import path


dir=path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)
st.set_page_config(page_title="BreastCancer",page_icon="☠️",layout="wide",initial_sidebar_state="expanded")
image=Image.open("multipage_cancer_app/final logo.jpg")

def load_lottiefile(filepath:str):
    with open(filepath,"r")as f:
        return json.load(f)
def main():
        st.sidebar.success("Select a page above ")

        col1,col2=st.columns([4,1])
        with col1 :
             st.title("Welcome :blue[to] _my_ :blue[_ML_] _App_ 👋")
             st.subheader("Breast Cancer Detection ") 
             
             
             st.image(image)
            
             
             
        with col2 :
              logo=load_lottiefile("multipage_cancer_app/logo.json")
              st_lottie(logo,height=100) 
               
              st.subheader("How to use the app:")
              st.markdown(''':green[The aim of this application is to be very easy for the user and can be used by anyone who does not have any knowledge of machine learning, so only when you change the measurements in the sidebar will the result of the patient's condition appear.
 ]''')
    
             #st.markdown('<span style="background-color:black; color:green;">**Goal of this app to be very easy for the user to can be used for any one who do not have any knowledge about machine learning so only when you change the measurements which in the sidebar you will git the output if the patient have a breast cancer or not** </span>', unsafe_allow_html=True)
             #lottie=load_lottiefile("multipage_cancer_app/lap.json")
             #st_lottie(lottie)
if __name__=="__main__":
    main()
