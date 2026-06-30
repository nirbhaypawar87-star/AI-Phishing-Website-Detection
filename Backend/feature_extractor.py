from urllib.parse import urlparse
import re


def extract_features(url):

    features = []

    parsed = urlparse(url)
    hostname = parsed.hostname if parsed.hostname else ""

    # 1. IP Address
    if re.match(r"^\d+\.\d+\.\d+\.\d+$", hostname):
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

    # 4. @ Symbol
    features.append(-1 if "@" in url else 1)

    # 5. Double Slash Redirect
    if url.rfind("//") > 7:
        features.append(-1)
    else:
        features.append(1)

    # 6. Prefix-Suffix
    features.append(-1 if "-" in hostname else 1)

    # 7. HTTPS
    features.append(1 if parsed.scheme == "https" else -1)

    # 8. Number of Dots
    dots = hostname.count(".")
    if dots <= 2:
        features.append(1)
    elif dots == 3:
        features.append(0)
    else:
        features.append(-1)

    # 9. Number of Digits
    digits = sum(c.isdigit() for c in url)
    if digits < 5:
        features.append(1)
    else:
        features.append(-1)

    # 10. Suspicious Keywords
    keywords = [
        "login",
        "verify",
        "secure",
        "bank",
        "update",
        "account",
        "password"
    ]

    if any(word in url.lower() for word in keywords):
        features.append(-1)
    else:
        features.append(1)

    return features