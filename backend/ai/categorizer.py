def auto_categorize(title: str):
    text = title.lower()

    if any(word in text for word in ["pizza", "food", "burger", "restaurant"]):
        return "food"
    if any(word in text for word in ["uber", "lyft", "taxi", "ride"]):
        return "travel"
    if any(word in text for word in ["walmart", "amazon", "target"]):
        return "shopping"
    if any(word in text for word in ["electric", "wifi", "internet", "gas bill"]):
        return "utilities"
    if any(word in text for word in ["doctor", "pharmacy", "hospital"]):
        return "health"

    return "other"
