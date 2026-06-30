from feature_extractor import extract_features

url = "http://bit.ly/login-account"

features = extract_features(url)

print("Features:", features)
print("Total:", len(features))