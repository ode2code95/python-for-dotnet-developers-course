import abc


class Car(abc.ABC):

    def __init__(self, model_name: str, engine_type: str, cylinders: int, base_price: float):
        self.base_price: float = base_price
        self.cylinders: int = cylinders
        self.model_name: str = model_name
        self.__engine_type: str = engine_type

    def drive(self):
        print(f"Car: The {self.model_name} goes vroom!")

    # get-only property
    @property
    def is_electric(self):
        return self.__engine_type == 'electric'

    @abc.abstractmethod
    def refuel(self):
        pass

    def __str__(self):
        return f'{type(self).__name__}: Model: {self.model_name}, Price: {self.base_price:,.0f}'

    def __repr__(self):
        return self.__str__()
