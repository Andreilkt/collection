class CoffeeMug:
    def __init__(self, filledMilliliters):
        self._filledMilliliters = filledMilliliters
        self._inscription = None

    @property
    def filledMilliliters(self):
        return self._filledMilliliters

    @filledMilliliters.setter
    def filledMilliliters(self, value):
        self._filledMilliliters = value

    @property
    def inscription(self):
        return self._inscription

    @inscription.setter
    def inscription(self, value):
        if len(value) > self.maxInscriptionLen:
            raise InscriptionError("Inscription is too long")
        self._inscription = value

    class InscriptionError(Exception):
        pass

    # Descriptor to limit inscription length
    class InscriptionValidator:
        MaxInscriptionLen = 50

        def __get__(self, obj, obj_type):
            return self.MaxInscriptionLen
