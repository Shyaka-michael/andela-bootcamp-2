class Car(object):
    """This is the car class"""

    def __init__(self, name='General', model='GM', car_type='saloon'):
        self.car_type = car_type
        self.model = model
        self.name = name
        self.speed = 0
        if self.car_type != 'saloon':
            self.car_type == "trailer"

        self.num_of_doors = 4
        if (self.name == 'Porshe') or (self.name == 'Koenigsegg'):
            self.num_of_doors = 2

        self.num_of_wheels = 4
        if self.car_type == 'trailer':
            self.num_of_wheels = 8

    def drive(self, value):

        if self.car_type == 'trailer':
            self.speed = value * 11
        else:
            self.speed = 10 ** value
        return self

    def is_saloon(self):
        if self.car_type != "trailer":
            return True