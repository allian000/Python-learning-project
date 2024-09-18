# Python learning project: Car Management System

This project is a Python-based system designed to manage the relationship between users and cars. The `CarManager` class manages multiple users and their associated cars, allowing the assignment, removal, and querying of car ownership.

> [!NOTE]
> This project is designed to practice Python programming skills and enhance my understanding of object-oriented programming (OOP). Additionally, I aim to gain a deeper insight into Python features, practice writing unit tests and test cases, and focus on writing comprehensive comments and project documentation. I hope this project will be helpful for those learning Python.

## Features

- **Car Management**: Create, assign, and remove cars for users.
- **User-Car Mapping**: Keep track of which user owns which cars.
- **Flexible Car Assignment**: Users can own multiple cars.
- **Owner Management**: Manage car ownership, ensuring that cars are only assigned to valid users.

## Classes

### Car

The `Car` class represents a car with attributes such as:

- `brand`: The brand of the car.
- `model`: The model of the car.
- `year`: The manufacturing year.
- `color`: The color of the car (default: "Nan").
- `doors`: The number of doors (default: "Nan").
- `used`: A boolean indicating if the car is used (default: False).
- `owner`: The owner of the car (can be set or removed).

#### Methods

- `__repr__`: Returns a string representation of the car.
- `__str__`: Returns a human-readable string of the car.
- `__eq__`: Compares two cars for equality.
- `__ne__`: Compares two cars for inequality.
- `owner`: A property to get and set the car's owner (must be a non-empty string or `None`).

### User

The `User` class represents a user with attributes:

- `name`: The name of the user.
- `car`: A car assigned to the user (optional).

### CarManager

The `CarManager` class manages the relationship between users and cars.

#### Methods

- `assign_car_to_user(user, car)`: Assigns a car to a user and updates the owner.
- `get_user_cars(user)`: Retrieves a list of cars assigned to the user.
- `get_car_owner(car)`: Returns the owner of a specific car.
- `remove_car_from_user(user, car)`: Removes a car from the user's list and clears ownership.

## Installation

To use this project, ensure you have Python installed on your machine. Clone this repository and navigate to the project folder:

```bash
git clone https://github.com/allian000/Python-learning-project.git
cd car-management-system
```

### Requirements

No additional libraries are required, as this project uses Python's standard library.

## Usage

You can run the system by using the `main.py` file. Here is an example of how to assign and manage cars for users:

```python
from car_manager import Car, User, CarManager

if __name__ == "__main__":
    # Create car objects
    car1 = Car(brand="Tesla", model="Model S", year="2024")
    car2 = Car(brand="Ford", model="Mustang", year="2020")
    
    # Create a user
    user1 = User(name="John")
    
    # Create a car manager
    car_manager = CarManager()
    
    # Assign cars to the user
    car_manager.assign_car_to_user(user1, car1)
    car_manager.assign_car_to_user(user1, car2)
    
    # Show the user's cars
    print(f"{user1.name} owns: {car_manager.get_user_cars(user1)}")
    
    # Remove a car
    car_manager.remove_car_from_user(user1, car1)
    print(f"After removing car1, {user1.name} owns: {car_manager.get_user_cars(user1)}")
```

## Running Unit Tests

Unit tests have been written to verify the functionality of the classes. You can run the tests using the following command:

```bash
python -m unittest discover -s tests
```

<!-- ## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. -->
