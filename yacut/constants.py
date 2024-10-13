from string import ascii_letters, digits, punctuation

PREFIX = 'http://'
SHORT_ID_CHOICES = ascii_letters + digits
DEFAULT_SHORT_ID_LENGTH = 6
MAX_SHORT_ID_LENGTH = 16
UNSUPPORTED_LETTERS = punctuation + 'абвгдежзийклмнопрстуфхцчшщъыьэюя '
