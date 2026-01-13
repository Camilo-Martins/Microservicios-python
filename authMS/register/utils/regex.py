import re

STORE_NAME_REGEX = re.compile(r'^[A-Za-z-ÖØ-öø-ÿ0-9 ]+$')
EMAIL_REGEX = re.compile(r'^[^\s@]+@[^\s@]+\.[^\s@]+$')
PASSWORD_REGEX= re.compile(r'^[^\s\u0000-\u001F\u007F]+$')