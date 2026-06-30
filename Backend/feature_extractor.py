from urllib.parse import urlparse


def extract_features(url):

    features = []

    # 1. IP Address
    hostname = urlparse(url).hostname

    if hostname and hostname.replace(".", "").isdigit():
        features.append(-1)
    else:
        features.append(1)

    # 2. URL Length
    if len(url) < 54:
        features.append(1)
    elif len(url) <= 75:
        features.append(0)
    else:
        features.append(-1)

    # 3. URL Shortener
    shorteners = [
        "bit.ly",
        "tinyurl.com",
        "goo.gl",
        "t.co",
        "ow.ly",
        "is.gd",
        "buff.ly"
    ]

    if any(short in url for short in shorteners):
        features.append(-1)
    else:
        features.append(1)

    return features