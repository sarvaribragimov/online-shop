from django.db import models
from django.core.exceptions import ValidationError

# validators for checking review description


def validate_desc(value):
    # TODO move to forms.py
    # list of bad words
    bad_words = ["yomon","bad"]
    # check if bad words in review description
    if any(word in value for word in bad_words):
        raise ValidationError("Bad words in review description")


