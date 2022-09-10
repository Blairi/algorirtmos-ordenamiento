class Car:
    id = None
    model = None

    def __init__(self, id, model) -> None:
        self.id = id
        self.model = model

    def __str__(self) -> str:
        return f"id: {self.id}\nmodel: {self.model}"
    
    def getId(self) -> str:
        return self.id

    def getModel(self) -> str:
        return self.model
