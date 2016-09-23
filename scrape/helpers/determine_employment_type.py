def determine_employment_type(text):
    lower = text.lower()
    if "freelance" in lower:
        return "freelance"
    if "contract" in lower:
        return "contract"
    if "part-time" in lower:
        return "part-time"
    if "full" in lower or "permanent" in lower:
        return "full-time"