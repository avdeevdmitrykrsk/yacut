from string import ascii_letters, digits, punctuation, whitespace

# Strings
russian_uppercase = ''.join(chr(1040 + i) for i in range(32))
russian_lowercase = ''.join(chr(1072 + i) for i in range(32))
SHORT_ID_CHOICES = ascii_letters + digits
UNSUPPORTED_LETTERS = (
    punctuation + russian_uppercase + russian_lowercase + whitespace + ' '
)

# Messages
MSG_CANT_MAKE_ID = 'Подходящий short_id не был создан, попробуйте еще раз'
MSG_EMPTY_REQUEST_BODY = 'Отсутствует тело запроса'
MSG_EXPECTED_FIELD_NOT_FOUND_URL = '"url" является обязательным полем!'
MSG_INVALID_SHORT_ID_NAME = 'Указано недопустимое имя для короткой ссылки'
MSG_SHORT_ID_ALREADY_EXIST = (
    'Предложенный вариант короткой ссылки уже существует.'
)
MSG_SHORT_ID_NOT_FOUND = 'Указанный id не найден'
MSG_FIELD_REQUIRED = 'Обязательное поле'

# Info
INFO_FORM_ENTER_LONG_LINK = 'Введите длинную ссылку'
INFO_FORM_YOUR_LONG_LINK_OPTION = 'Ваш вариант короткой ссылки'
INFO_FORM_MAKE = 'Создать'

# HTTP status codes
HTTP_OK = 200
HTTP_CREATED = 201
HTTP_BAD_REQUEST = 400
HTTP_NOT_FOUND = 404

# Lenghts
DEFAULT_SHORT_ID_LENGTH = 6
MAX_SHORT_ID_LENGTH = 16
MIN_ORIGINAL_LINK_LENGTH = 1
MAX_ORIGINAL_LINK_LENGTH = 256
MIN_CUSTOM_ID_LENGTH = 1
MAX_CUSTOM_ID_LENGTH = 16

ATTEMPTS_STEP = 1
DEFAULT_ATTEMPTS_COUNT = 0
MAX_NUMBER_OF_ATTEMPTS = 100_000_000
CUSTOM_ID_REGEX_PATTERN = r'(\S[a-zA-Z]+|\d+)'
