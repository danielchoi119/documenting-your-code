import random
import string

from typing import Iterable, Optional


def generate_password(chars: int, punctuation: bool, invalid_chars: Optional[Iterable[str]]=None) -> str:
    """
    Generates a password randomly.

    Args:
        chars (int):  number of characters you want in the password
        punctuation (bool): True if you want to include the punctuation
        invalid_chars (Optional[Iterable[str]]): characters that you do not want in the password. Defaults to None

    Returns:
        str: a random password with length = chars
    """
    valid_chars = string.ascii_letters + string.digits

    if punctuation:
        valid_chars += string.punctuation

    # for each invalid character, we will replace it with an empty string to remove that character.
    for invalid_char in invalid_chars:
        valid_chars = valid_chars.replace(invalid_char, "")

    # choose k number of characters randomly from valid_chars
    password_chars = random.choices(valid_chars, k=chars)

    # since password_chars is a list, we will join it using generator comprehension.
    password = "".join(char for char in password_chars)

    return password
