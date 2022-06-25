#Maria Williams
#6/24/22
#call API

import streamlit
import requests
from google.cloud import automl
import json
import os
from predict import get_prediction

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =r"C:\Users\maria\OneDrive\Documents\School Summer 2022\IdeationClassification\ideationclassification-d09633ba31d7.json"
t = "C:/Users/maria/OneDrive/Documents/School Summer 2022/IdeationClassification/sampledata/non-sui-loss.txt"
m = "projects/428284761450/locations/us-central1/models/TCN88982376524283904"


print(get_prediction(t, m))