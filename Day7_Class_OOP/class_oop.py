class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._mileage = 0 # protected attribute
        self.__engine_status = "off" # private attribute
        
    def start_engine(self):
        self.__engine_status = "on"
        print("Engine started.")
        
    def stop_engine(self):
        self.__engine_status = "off"
        print("Engine stopped.")
        
    def drive(self, distance):
        self._mileage += distance
        
car = Car("Honda", "Civic", 2022)
car.start_engine()
car.drive(10)
car.stop_engine()
print(car._mileage) # access protected attribute
print(car.__engine_status) # AttributeError: 'Car' object has no attribute '__engine_status'. Did you mean: '_Car__engine_status'? 