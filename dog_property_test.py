class Dog:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed

    @property
    name(self):
        """The name property"""
        return self._name

    @name.setter
    def name(self, value):
        """Name must be a string between 1 and 25 characters in length"""
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            raise ValueError(
                "Name must be a string between 1 and 25 characters.")

    @property
    def breed(self):
        """The breed property"""
        return self._breed

    @breed.setter
    def breed(self, value):
        """Breed must be one of the approved choices"""
        approved_breeds = ["Corgi", "Beagle", "Poodle"]
        if value in approved_breeds:
            self._breed = value
        else:
            raise ValueError(
                "Breed must be one of the approved choices: Corgi, Beagle, Poodle")
