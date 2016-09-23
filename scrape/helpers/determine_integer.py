import re

def determine_integer(text):
    replaced = re.sub("[^0-9]", "", text)
    return int(replaced) if len(replaced) > 0 else None