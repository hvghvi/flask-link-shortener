class Link:
    def __init__(self, link_id: int):
        if type(link_id) is not int:
            raise ValueError("Link ID should be an integer.")
        self.__link_id = link_id


    @property
    def link_id(link_id):
        return self.__link_id

    