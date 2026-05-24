import re
from bs4 import BeautifulSoup


def clean_html(raw_html):
    """
    Remove HTML tags and return clean text.
    """

    soup = BeautifulSoup(raw_html, "html.parser")

    return soup.get_text(separator=" ", strip=True)


def normalize_whitespace(text):
    """
    Remove extra spaces, tabs, and newlines.
    """

    return re.sub(r"\s+", " ", text).strip()


def extract_keywords(text):
    """
    Simple keyword extraction for regulatory topics.
    """

    keywords = []

    regulatory_terms = [
        "aml",
        "compliance",
        "crypto",
        "risk",
        "sanctions",
        "fraud",
        "kyc",
        "governance",
        "fca",
        "sec",
        "esma"
    ]

    text_lower = text.lower()

    for term in regulatory_terms:
        if term in text_lower:
            keywords.append(term)

    return keywords


def classify_risk(text):
    """
    Basic risk classification based on keywords.
    """

    text_lower = text.lower()

    high_risk_terms = [
        "fraud",
        "sanctions",
        "money laundering",
        "terrorist financing"
    ]

    medium_risk_terms = [
        "compliance",
        "risk",
        "governance",
        "kyc"
    ]

    for term in high_risk_terms:
        if term in text_lower:
            return "High"

    for term in medium_risk_terms:
        if term in text_lower:
            return "Medium"

    return "Low"


def parse_regulation(raw_data):
    """
    Parse and structure scraped regulation data.
    """

    raw_title = raw_data.get("title", "")
    raw_content = raw_data.get("content", "")

    cleaned_title = clean_html(raw_title)
    cleaned_content = clean_html(raw_content)

    cleaned_title = normalize_whitespace(cleaned_title)
    cleaned_content = normalize_whitespace(cleaned_content)

    keywords = extract_keywords(
        cleaned_title + " " + cleaned_content
    )

    risk_level = classify_risk(cleaned_content)

    parsed_data = {
        "title": cleaned_title,
        "content": cleaned_content,
        "keywords": keywords,
        "risk_level": risk_level
    }

    return parsed_data