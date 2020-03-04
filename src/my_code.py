"""
Files stored in `src` should contain your driving code. In your case, this will be your Python Text Classifier.
Wrapping the code in some kind of function will enable you to call it from `main.py` when you import it.
This will let you process data coming from your Flask UI.
"""


def my_code(text_string):
    """
    :param text_string: A string, which this function will convert to uppercase.
    :return str:
    """
    return text_string.upper()
