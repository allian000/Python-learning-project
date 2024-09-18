import unittest

class Car:
    """
    A class used to represent a Car.

    Attributes:
    -----------
    brand : str
        The brand of the car
    model : str
        The model of the car
    year : str
        The manufacturing year of the car
    color : str
        The color of the car (default "Nan")
    doors : str
        The number of doors of the car (default "Nan")
    used : bool
        Whether the car is used or not (default False)
    owner : str
        The owner of the car
    """

    def __init__(self, brand: str, model: str, year: str, color: str = "Nan", doors: str = "Nan", used: bool = False):
        """
        Parameters:
        -----------
        brand : str, The brand of the car
        model : str, The model of the car
        year : str, The manufacturing year of the car
        color : str, optional, The color of the car (default "Nan")
        doors : str, optional, The number of doors of the car (default "Nan")
        used : bool, optional, Whether the car is used or not (default False)
        owner : str, optional, The owner of the car
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.doors = doors
        self.used = used
        self._owner = None

    def __repr__(self):
        '''
        Returns a string representation of the object
        '''
        return f"Brand:{self.brand}, Model:{self.model}, Year:{self.year}, Color:{self.color}, Doors:{self.doors}, Used:{self.used}, Owner:{self.owner}"

    def __str__(self):
        '''
        Returns a string representation of the object
        '''
        return f"Brand:{self.brand}, Model:{self.model}, Year:{self.year}, Color:{self.color}, Doors:{self.doors}, Used:{self.used}, Owner:{self.owner}"

    def __eq__(self, other):
        '''
        Returns True if the objects are equal, False otherwise
        '''
        return self.brand == other.brand and self.model == other.model and self.year == other.year and self.color == other.color and self.doors == other.doors and self.used == other.used

    def __ne__(self, other):
        '''
        Returns True if the objects are not equal, False otherwise
        '''
        return not self == other
    
    @property
    def owner(self):
        """
        Returns the owner of the car object
        """
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of the car object. Allows None to reset the owner.
        """
        if owner is None or (isinstance(owner, str) and owner):
            self._owner = owner
        else:
            raise ValueError("Owner should be a non-empty string or None")


class User:
    """
    A class used to represent a User.
    
    Attributes:
    -----------
    name : str
        The name of the user
    car : Car
        The car object assigned to the user
    """
    def __init__(self, name: str, car: Car=None):
        """
        Parameters:
        -----------
        name : str, The name of the user
        car : Car, optional, The car object assigned to the user
        """
        self.name = name
        self.car = car
        

class CarManager:
    """
    A class that manages the relationship between Users and Cars.
    
    Attributes:
    -----------
    user_car_map : dict
        A dictionary that maps a user's name to a list of car objects
    """

    def __init__(self):
        """
        Initializes an empty user-car mapping.
        """
        self.user_car_map = {}

    def assign_car_to_user(self, user: User, car: Car):
        """
        Assign a car to a user and manage the owner relationship.
        If the user already has cars, append to the list.
        """
        if user.name not in self.user_car_map:
            self.user_car_map[user.name] = []
        self.user_car_map[user.name].append(car)
        car.owner = user.name

    def get_user_cars(self, user: User):
        """
        Retrieve all cars assigned to the user.
        """
        return self.user_car_map.get(user.name, [])

    def get_car_owner(self, car: 'Car'):
        """
        Retrieve the owner of a car.
        """
        for user_name, car_list in self.user_car_map.items():
            if car in car_list:
                return user_name
        return None

    def remove_car_from_user(self, user: User, car: Car):
        """
        Remove a specific car from the user's list of cars.
        """
        if user.name in self.user_car_map:
            if car in self.user_car_map[user.name]:
                self.user_car_map[user.name].remove(car)
                car.owner = None
            if not self.user_car_map[user.name]:
                del self.user_car_map[user.name]


class TestCar(unittest.TestCase):

    def test_car_initialization(self):
        car = Car(brand="Tesla", model="Model S", year="2024",
                  color="Red", doors="4", used=False)
        self.assertEqual(car.brand, "Tesla")
        self.assertEqual(car.model, "Model S")
        self.assertEqual(car.year, "2024")
        self.assertEqual(car.color, "Red")
        self.assertEqual(car.doors, "4")
        self.assertFalse(car.used)
        self.assertIsNone(car.owner)

    def test_owner_setter(self):
        car = Car(brand="Tesla", model="Model S", year="2024")
        car.owner = "John"
        self.assertEqual(car.owner, "John")
        with self.assertRaises(ValueError):
            car.owner = 123  # Invalid type
        with self.assertRaises(ValueError):
            car.owner = ""  # Empty string


class TestCarManager(unittest.TestCase):

    def setUp(self):
        self.car_manager = CarManager()
        self.user = User(name="John")
        self.car1 = Car(brand="Tesla", model="Model S", year="2024")
        self.car2 = Car(brand="Ford", model="Mustang", year="2020")

    def test_assign_car_to_user(self):
        self.car_manager.assign_car_to_user(self.user, self.car1)
        self.assertEqual(self.car1.owner, "John")
        self.assertIn(self.car1, self.car_manager.get_user_cars(self.user))

    def test_remove_car_from_user(self):
        self.car_manager.assign_car_to_user(self.user, self.car1)
        self.car_manager.remove_car_from_user(self.user, self.car1)
        self.assertIsNone(self.car1.owner)
        self.assertNotIn(self.car1, self.car_manager.get_user_cars(self.user))

    def test_get_user_cars(self):
        self.car_manager.assign_car_to_user(self.user, self.car1)
        self.car_manager.assign_car_to_user(self.user, self.car2)
        user_cars = self.car_manager.get_user_cars(self.user)
        self.assertEqual(len(user_cars), 2)
        self.assertIn(self.car1, user_cars)
        self.assertIn(self.car2, user_cars)

    def test_get_car_owner(self):
        self.car_manager.assign_car_to_user(self.user, self.car1)
        self.assertEqual(self.car_manager.get_car_owner(self.car1), "John")
        self.assertIsNone(self.car_manager.get_car_owner(
            self.car2))  # car2 has no owner


if __name__ == "__main__":
    unittest.main()

    # car1 = Car(brand="Tesla", model="Model S", year="2024")
    # car2 = Car(brand="Ford", model="Mustang", year="2020")
    # user1 = User(name="John")

    # car_manager = CarManager()
    
    # # 分配兩輛車給 John
    # car_manager.assign_car_to_user(user1, car1)
    # car_manager.assign_car_to_user(user1, car2)

    # # 顯示 John 擁有的所有車輛
    # print(f"{user1.name} owns: {car_manager.get_user_cars(user1)}")

    # # 從 John 的車清單中移除一輛車
    # car_manager.remove_car_from_user(user1, car1)
    # print(f"After removing car1, {user1.name} owns: {car_manager.get_user_cars(user1)}")
    # print(f"Car1's owner after removal: {car1.owner}")