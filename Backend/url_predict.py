from fastapi import APIRouter
from pydantic import BaseModel
from feature_extractor import extract_features
import joblib
import pandas as pd

router = APIRouter()

# Load trained model
model = joblib.load("../models/phishing_model.pkl")


class URLInput(BaseModel):
    url: str


@router.post("/predict-url")
def predict_url(data: URLInput):

    features = extract_features(data.url)

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

    # Convert 10 extracted features into 30 features
    while len(features) < 30:
        features.append(0)

    # Safety check
    if len(features) != 30:
        return {
            "error": f"Expected 30 features but got {len(features)}"
        }

    df = pd.DataFrame([features], columns=feature_names)

    prediction = model.predict(df)
    probability = model.predict_proba(df)

    confidence = max(probability[0]) * 100

    if prediction[0] == 1:
        result = "🟢 Legitimate Website"
    else:
        result = "🔴 Phishing Website"

    return {
        "url": data.url,
        "prediction": result,
        "confidence": f"{confidence:.2f}%",
        "model": "Random Forest"
    }