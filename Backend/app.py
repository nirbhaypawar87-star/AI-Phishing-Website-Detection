from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load trained model
model = joblib.load("../models/phishing_model.pkl")

# Input model
from typing import List

class WebsiteFeatures(BaseModel):
    features: List[int]

@app.get("/")
def home():
    return {"message": "AI Phishing Detection API"}

@app.post("/predict")
def predict(data: WebsiteFeatures):

    feature_names = [
        'having_IPhaving_IP_Address',
        'URLURL_Length',
        'Shortining_Service',
        'having_At_Symbol',
        'double_slash_redirecting',
        'Prefix_Suffix',
        'having_Sub_Domain',
        'SSLfinal_State',
        'Domain_registeration_length',
        'Favicon',
        'port',
        'HTTPS_token',
        'Request_URL',
        'URL_of_Anchor',
        'Links_in_tags',
        'SFH',
        'Submitting_to_email',
        'Abnormal_URL',
        'Redirect',
        'on_mouseover',
        'RightClick',
        'popUpWidnow',
        'Iframe',
        'age_of_domain',
        'DNSRecord',
        'web_traffic',
        'Page_Rank',
        'Google_Index',
        'Links_pointing_to_page',
        'Statistical_report'
    ]

    print(data.features)
    print(len(data.features))

    df = pd.DataFrame([data.features], columns=feature_names)

    prediction = model.predict(df)

    if prediction[0] == 1:
        result = "Legitimate Website"
    else:
        result = "Phishing Website"

    return {
        "prediction": result
    }