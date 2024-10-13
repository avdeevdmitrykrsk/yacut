from string import ascii_letters, digits, punctuation, whitespace

russian_uppercase = ''.join(chr(1040 + i) for i in range(32))
russian_lowercase = ''.join(chr(1072 + i) for i in range(32))
SHORT_ID_CHOICES = ascii_letters + digits
DEFAULT_SHORT_ID_LENGTH = 6
MAX_SHORT_ID_LENGTH = 16
UNSUPPORTED_LETTERS = (
    punctuation + russian_uppercase + russian_lowercase + whitespace + ' '
)
