class Driver():
    _all = []
    _count = len(_all) or 0

    def __init__(self, name, car_make, car_model):
        self._name = name
        self._car_make = car_make
        self._car_model = car_model
        Driver._all.append(self)
        Driver._count = len(Driver._all)

    @property
    def name(self):
        return self._name
    # @name.setter
    # def name(self, name):
    #     self._name = name

    @property
    def car_make(self):
        return self._car_make

    @property
    def car_model(self):
        return self._car_model

    @classmethod
    def fleet_size(cls):
        return Driver._count

    @classmethod
    def driver_names(cls):
        return list(map(lambda driver:driver.name,Driver._all))

    @classmethod
    def fleet_makes(cls):
        return list(map(lambda driver:driver.car_make,Driver._all))

    @classmethod
    def fleet_models(cls):
        return list(map(lambda driver:driver.car_model,Driver._all))

    @classmethod
    def fleet_makes_count(cls):
        hist = {}
        for make in Driver.fleet_makes():
            if make in hist:
                hist[make] += 1
            else:
                hist[make] = 1
        return hist

    @classmethod
    def fleet_models_count(cls):
        hist = {}
        for make in Driver.fleet_models():
            if make in hist:
                hist[make] += 1
            else:
                hist[make] = 1
        return hist


    @classmethod
    def percent_of_fleet(cls, car_make):
        all_makes = len(Driver.fleet_makes())
        selected_make = Driver.fleet_makes_count()[car_make]
        percentage = selected_make/all_makes
        return str(round(percentage*100,3))+'%'
