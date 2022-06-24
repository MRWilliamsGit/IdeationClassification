#Maria Williams
#6/24/22
#call API
#some code from https://betterprogramming.pub/how-to-make-http-requests-in-streamlit-app-f22a77fd1ed7

import streamlit
import requests
from google.cloud import automl

def fetch(session, url):
    try:
        result = session.get(url)
        return result.json()
    except Exception:
        return {}

def main():
    st.title("Ideation Classification")

    project_id = "IdeationClassification"
    model_id = "TCN88982376524283904"
    content = "Hello"

    prediction_client = automl.PredictionServiceClient()

    # Get the full path of the model.
    model_full_id = automl.AutoMlClient.model_path(project_id, "us-central1", model_id)

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
    main()