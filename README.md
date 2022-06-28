# IdeationClassification
This project demonstrates how a Google Vertex AI model could effectively learn to identify text as pertaining to suicide.

### Data
The model was trained on Reddit posts that were self-identified as pertaining to suicide, as well as Reddit posts from additional subreddits to represent the negative class. This data was originally sourced by [Nikhileswar Komati](https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch?resource=download), though only 1,982 records were used from the 232,074 records collected.

### Modeling
The model was trained by Vertex AI's AutoMl for NLP process to acheive 97% Precision.

### Deployment
A simple app was created for public access to the model. It can recieve free text, or draw a recent Reddit post to analyze.
To access: https://mrwilliamsgit-ideationclassification-main-71oty9.streamlitapp.com/

### CICD Pipleline
This project follows CICD best practices: Any changes pushed to Github are verified by GitHub actions before being written. Once written, the app automatically updates with the latest version from GitHub.



