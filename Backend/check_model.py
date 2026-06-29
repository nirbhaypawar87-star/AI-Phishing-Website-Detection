import joblib

model = joblib.load("../models/phishing_model.pkl")

print("Number of features:", model.n_features_in_)

try:
    print("\nFeature names:")
    print(model.feature_names_in_)
except AttributeError:
    print("Feature names are not available.")