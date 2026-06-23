
class GotCharacter:
    def __init__(self: "GotCharacter", first_name: str, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """Class of the Stark family. Or when bad things happen to good people."""
    def __init__(self: "Stark", first_name: str = None, is_alive: bool = True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self: "Stark") -> None:
        print(self.house_words)

    def die(self: "Stark") -> None:
        self.is_alive = False
