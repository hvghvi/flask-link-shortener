import secrets
import string
BASE62 = string.ascii_letters + string.digits #generates base62 chars

class Codes:
    def __init__(self, original_url: str):
        self.original_url = original_url
        self.generated_code = None
        

    @property
    def original_url(self) -> str:
        return self._original_url

    @property
    def generated_code(self) -> str:
        return self.generated_code

    def generate_code(link):
        password = "".join(secrets.choice(BASE62) for _ in range(12))
