#Maria Williams
#6/24/22
#call API

from googleapiclient import discovery
from googleapiclient import errors
import streamlit as st
import requests as r
from google.cloud import automl
import os

def main():
    #st.title("Ideation Classification")

    project_id = "ideationclassification"
    model_id = "TCN88982376524283904"
    content = "Hello"

    prediction_client = automl.PredictionServiceClient()

    # Get the full path of the model.
    model_full_id = automl.AutoMlClient.model_path(project_id, "us-central1", model_id)
    print(model_full_id)

    # Supported mime_types: 'text/plain', 'text/html'
    # https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#textsnippet
    text_snippet = automl.TextSnippet(content=content, mime_type="text/plain")
    payload = automl.ExamplePayload(text_snippet=text_snippet)

    response = prediction_client.predict(name=model_full_id, payload=payload)

    for annotation_payload in response.payload:
        print(u"Predicted class name: {}".format(annotation_payload.display_name))
        print(
            u"Predicted class score: {}".format(annotation_payload.classification.score)
        )

if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] =r"C:\Users\maria\OneDrive\Documents\School Summer 2022\IdeationClassification\ideationclassification-d09633ba31d7.json"
    main()