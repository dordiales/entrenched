class SlotFullError(Exception):
    def __init__(self, message="Game slot already occupied"):
        self.message = message
        super().__init__(self.message)
