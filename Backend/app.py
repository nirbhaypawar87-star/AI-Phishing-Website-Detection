from url_predict import router as url_router
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib
import pandas as pd

from feature_extractor import extract_features

app = FastAPI(title="AI Phishing Website Detection API")
app.include_router(url_router)

# Load trained model
model = joblib.load("../models/phishing_model.pkl")


# ===========================
# Request Models
# ===========================

class WebsiteFeatures(BaseModel):
    features: List[int]


class URLInput(BaseModel):
    url: str


# ===========================
# Home Endpoint
# ===========================

@app.get("/")
def home():
    return {
        "message": "AI Phishing Website Detection API is Running!"
    }


# ===========================
# Prediction using 30 Features
# ===========================

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

    if len(data.features) != len(feature_names):
        return {
            "error": f"Expected {len(feature_names)} features but got {len(data.features)}"
        }

    df = pd.DataFrame([data.features], columns=feature_names)

    prediction = model.predict(df)

    if prediction[0] == 1:
        result = "Legitimate Website"
    else:
        result = "Phishing Website"

    return {
        "prediction": result
    }


# ===========================
# Prediction using URL
# ===========================

@app.post("/predict_url")
def predict_url(data: URLInput):

    features = extract_features(data.url)

    return {
        "url": data.url,
        "features": features,
        "total_features": len(features),
        "message": "Feature extraction successful"
    }