import streamlit as st
import os
from google.cloud import aiplatform
from predict import class_this
from getpost import getPost

def Classify(text):
        
    #call model through API
    predictions = class_this(
        project="428284761450",
        endpoint_id="7889277404269510656",
        location="us-central1",
        content=text
        )

    #get prediction
    for prediction in predictions:
        p = dict(prediction)
    
    if p['confidences'][0]>p['confidences'][1]:
        st.success("This text does not pertain to suicide.")
    else:
        st.error("This text discusses suicide or displays possible suicidal ideation.")

def main():
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\maria\OneDrive\Documents\School Summer 2022\IdeationClassification\ideationclassification-d09633ba31d7.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=st.secrets.gc_serviceaccount
    st.title("Classifying Reddit Posts")
    st.write("This form interacts with an AI model which was trained to identify text as pertaining to suicide or demonstrating suicidal ideation.")
    #st.write ("This model was trained on Reddit posts, but should be able to function with any text.")
    #st.write("Please enter text in the field below, or select one of the population options.")

    box = st.radio('', ('Enter Text', 'Populate Dream Reddit Post', 'Populate Suicide Reddit Post'))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    
    if box == "Populate Dream Reddit Post":
        fill_text = getPost('Dreams')
        st.text_area('', fill_text)
        text = fill_text
    elif box == "Populate Suicide Reddit Post":
        fill_text = getPost('SuicideWatch')
        st.text_area('', fill_text)
        text = fill_text
    else:
        text = st.text_area('')

    if st.button("Classify"):
        if text != '':
            Classify(text)
        else:
            st.error("Please provide text to classify.")

if __name__ == "__main__":
       main() 
