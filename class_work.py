class Dad:
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)
    hair = "black"

class Mom:
    def __init__(self,name,  **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)
    eyes = "blue"

class Child(Dad, Mom):
    def __init__(self, name, **kwargs):
        self.name = name
        
        for key, value in kwargs.items():
            setattr(self, key, value)
