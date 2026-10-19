import secrets
import string

from link_shortener.domain.link import Link

BASE62 = string.ascii_letters + string.digits  # generates base62 chars


class Codes:
    def __init__(self, original_url: Link):
        if not isinstance(original_url, Link):
            raise TypeError("original_url must be a Link instance")

        self.__original_url = original_url
        self.__generated_code = None

    @property
    def original_url(self) -> Link:
        return self.__original_url

    @property
    def generated_code(self):
        return self.__generated_code

    def generate_code(self, link=None):
        if link is not None:
            if not isinstance(link, Link):
                raise TypeError("link must be a Link instance")
            self.__original_url = link

        password = "".join(secrets.choice(BASE62) for _ in range(12))
        self.__generated_code = password
        return self.__generated_code

