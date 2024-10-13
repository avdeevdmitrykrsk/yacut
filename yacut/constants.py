from string import ascii_letters, digits, punctuation, whitespace

russian_uppercase = ''.join(chr(1040 + i) for i in range(32))
russian_lowercase = ''.join(chr(1072 + i) for i in range(32))
SHORT_ID_CHOICES = ascii_letters + digits
UNSUPPORTED_LETTERS = (
    punctuation + russian_uppercase + russian_lowercase + whitespace + ' '
)

# Lenghts
DEFAULT_SHORT_ID_LENGTH = 6
MAX_SHORT_ID_LENGTH = 16
MIN_ORIGINAL_LINK_LENGTH = 1
MAX_ORIGINAL_LINK_LENGTH = 256
MIN_CUSTOM_ID_LENGTH = 1
MAX_CUSTOM_ID_LENGTH = 16

CUSTOM_ID_REGEX_PATTERN = r'([a-zA-Z]+|\d+)'
