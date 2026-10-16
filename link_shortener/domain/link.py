class Link:
    def __init__(self, link_id: int, url):
        if type(link_id) is not int:
            raise ValueError("Link ID should be an integer.")
        self.__link_id = link_id
        self.__url = url
        self.__updated_link = None 


    @property
    def link_id(self) -> int: #guarantees that it returns int 
        return self.__link_id

    @property
    def url(self) -> str:
        return self.__url
    
    @property
    def updated_link(self) -> str:
        return self.__updated_link

    def update_link(self, link) -> str:
        self.__updated_link = link
        return link
    