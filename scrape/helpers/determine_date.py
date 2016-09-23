from dateutil import parser
from datetime import date, timedelta
import re
from .determine_integer import determine_integer

def determine_date(text):
    lowercase_text = text.lower()
    if 'today' in lowercase_text:
        return date.today()
    if 'yesterday' in lowercase_text:
        return date.today() - timedelta(1)
    if 'ago' in lowercase_text:
        return date.today() - timedelta(determine_integer(lowercase_text))
    if 'expires' in lowercase_text:
        return None
    stripped_text = strip_useless_words(lowercase_text)
    return parser.parse(stripped_text)

def strip_useless_words(text):
    exceptions = 'jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec|january|february|march|april|june|july|august|september|october|november|december'
    regex = r'\b(?!' + exceptions + r')\b(\b[^\d\W]+\b)'
    return re.sub(regex, '', text)