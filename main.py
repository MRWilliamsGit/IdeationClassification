#Maria Williams
#6/27/22

import streamlit as st
from google.cloud import aiplatform
from predict import class_this

def getpredict():
    
    #API call
    predictions = class_this(
        project="428284761450",
        endpoint_id="7889277404269510656",
        location="us-central1",
        content="It is a nice day"
    )

    for prediction in predictions:
        print(" prediction:", dict(prediction))

def main():
    st.title("Classifying Reddit Posts")
    text = st.text_area('Enter Text:')

    if st.button("Classify"):
        #get prediction
        predictions = class_this(
            project="428284761450",
            endpoint_id="7889277404269510656",
            location="us-central1",
            content=text
        )

        for prediction in predictions:
            p = dict(prediction)
            #st.write(" prediction:", p)
        #st.write(p["confidences"])

        #classify answer
        if p['confidences'][0]>p['confidences'][1]:
            st.success("This text does not pertain to suicide.")
        else:
            st.error("This text discusses suicide or displays possible suicidal ideation.")

if __name__ == "__main__":
       main() 
