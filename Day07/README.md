## Overview

Day 7 introduces Object-Oriented Programming (OOP), a fundamental programming paradigm that is essential for robotics development. OOP provides a structured way to write code by organizing functionality into reusable objects and classes. This approach is particularly important in robotics because it allows you to model real-world entities (robots, sensors, actuators) as software objects, making code more modular, maintainable, and scalable. Understanding OOP concepts is crucial for writing ROS (Robot Operating System) nodes and creating complex robotics applications.

---

## What is Object-Oriented Programming (OOP)?

**Simple Definition:**

Object-Oriented Programming is a structured programming approach that organizes code into objects and classes, making it easier to model real-world entities and relationships.

**Why OOP for Robotics?**

- **Modularity:** Break complex systems into manageable components
- **Reusability:** Use the same code multiple times without repetition
- **Maintainability:** Easier to update and debug organized code
- **Scalability:** Handle complex robotic systems efficiently
- **Real-World Modeling:** Directly represent robots, sensors, and actuators as code objects
- **ROS Integration:** ROS heavily uses OOP concepts in its architecture

**Core OOP Principle:**

Instead of writing independent functions and variables, OOP bundles related data and functions together into objects, creating a more intuitive and organized code structure.

---

## Core OOP Concepts

### 1. Classes

**What is a Class?**

A **class** is a blueprint or template for creating objects. It defines the structure (attributes) and behavior (methods) that objects created from it will have.

**Simple Definition:**
- Blueprint or template for objects
- Defines what data an object will hold
- Defines what actions an object can perform
- Reusable structure for multiple objects

**Class Analogy:**

Think of a class as a cookie cutter. The cookie cutter is the blueprint (class), and each cookie made from it is a unique object (instance).

**Class Structure:**

```python
class ClassName:
    # Attributes (data)
    # Methods (functions)
    pass
```

**Basic Class Example:**

```python
# Define a class for a robot
class Robot:
    # Attributes
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed  # cm/s
        self.is_moving = False
    
    # Methods (behaviors)
    def move_forward(self):
        self.is_moving = True
        print(f"{self.name} is moving forward at {self.speed} cm/s")
    
    def stop(self):
        self.is_moving = False
        print(f"{self.name} has stopped")
```

**Components of a Class:**

| Component | Purpose | Example |
|-----------|---------|---------|
| **Class Name** | Identifier for the class | `class MobileRobot:` |
| **Attributes** | Data stored in the class | `self.speed = 50` |
| **Methods** | Functions within the class | `def move_forward(self):` |
| **Constructor (__init__)** | Initialize object when created | `def __init__(self, name):` |
| **self** | Reference to current object | Used in all methods |

**Why Classes Matter in Robotics:**

```python
# Without classes (procedural approach - harder to manage)
robot1_name = "TurtleBot"
robot1_speed = 50
robot1_is_moving = False

robot2_name = "DiffBot"
robot2_speed = 70
robot2_is_moving = False

# With classes (object-oriented approach - organized and scalable)
class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.is_moving = False

robot1 = Robot("TurtleBot", 50)
robot2 = Robot("DiffBot", 70)
```

---

### 2. Objects

**What is an Object?**

An **object** is an instance of a class. While a class is a blueprint, an object is a concrete realization of that blueprint with specific values and state.

**Simple Definition:**
- Instance of a class
- Actual entity created from the class blueprint
- Has specific attribute values
- Can perform actions defined by the class

**Creating Objects:**

```python
# Create objects from the Robot class
robot1 = Robot("TurtleBot", 50)
robot2 = Robot("DiffBot", 70)
robot3 = Robot("Clearpath Warthog", 100)
```

**Object Analogy:**

- **Class:** The blueprint for a car
- **Object:** An actual car with license plate, color, and year
- **Instance:** Each car is a unique instance with different values

**Accessing Object Attributes and Methods:**

```python
# Access attributes
print(robot1.name)  # Output: TurtleBot
print(robot1.speed)  # Output: 50

# Call methods
robot1.move_forward()  # Output: TurtleBot is moving forward at 50 cm/s
robot1.stop()  # Output: TurtleBot has stopped
```

**Practical Robotics Example:**

```python
class MobileRobot:
    def __init__(self, name, speed, wheel_diameter):
        # Attributes
        self.name = name
        self.speed = speed  # cm/s
        self.wheel_diameter = wheel_diameter  # cm
        self.position = (0, 0)
        self.direction = 0  # degrees
        self.is_moving = False
    
    def move_forward(self, distance):
        self.is_moving = True
        print(f"{self.name} moving {distance}cm forward at {self.speed} cm/s")
        self.position = (self.position[0] + distance, self.position[1])
    
    def turn(self, angle):
        print(f"{self.name} turning {angle} degrees")
        self.direction = (self.direction + angle) % 360
    
    def stop(self):
        self.is_moving = False
        print(f"{self.name} stopped at position {self.position}")
    
    def get_status(self):
        return f"{self.name} - Position: {self.position}, Direction: {self.direction}°"

# Create robot objects
turtlebot = MobileRobot("TurtleBot3", 50, 7.0)
roomba = MobileRobot("Roomba", 30, 8.5)

# Use the objects
turtlebot.move_forward(100)
turtlebot.turn(90)
turtlebot.move_forward(50)
print(turtlebot.get_status())

roomba.move_forward(200)
roomba.turn(45)
print(roomba.get_status())
```

**Why Objects Matter in Robotics:**

- **Represent Real Entities:** Each robot can be an object with its own state
- **Multiple Instances:** Control multiple robots without code duplication
- **Unique States:** Each object maintains its own independent data
- **Easy to Extend:** Add more robots or sensors as needed

---

## Key OOP Concepts Explained

### **Attributes (Properties)**

Data stored within an object that describes its state.

```python
class RoboticArm:
    def __init__(self):
        self.joint1_angle = 0  # Attribute
        self.joint2_angle = 0  # Attribute
        self.gripper_open = True  # Attribute
```

### **Methods (Behaviors)**

Functions within a class that describe what the object can do.

```python
class RoboticArm:
    def rotate_joint1(self, angle):
        self.joint1_angle = angle
        print(f"Joint 1 rotated to {angle} degrees")
    
    def close_gripper(self):
        self.gripper_open = False
        print("Gripper closed")
```

### **Constructor (__init__)**

Special method called when creating an object to initialize its attributes.

```python
class Sensor:
    def __init__(self, sensor_id, sensor_type):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.reading = 0

# When creating an object, __init__ is automatically called
sensor = Sensor(1, "Ultrasonic")
```

### **self Parameter**

Reference to the current object within a method.

```python
class Motor:
    def __init__(self, rpm):
        self.rpm = rpm  # self refers to the specific motor object
    
    def set_speed(self, new_rpm):
        self.rpm = new_rpm  # Updates this specific motor's speed
```

---

## Practical Robotics Application

**Complete Robot System Using OOP:**

```python
class DistanceSensor:
    def __init__(self, pin, max_range=400):
        self.pin = pin
        self.max_range = max_range
        self.distance = 0
    
    def read_distance(self):
        # Simulated sensor reading
        self.distance = 150  # cm
        return self.distance

class Motor:
    def __init__(self, motor_id, rpm=100):
        self.motor_id = motor_id
        self.rpm = rpm
        self.is_running = False
    
    def run(self):
        self.is_running = True
        print(f"Motor {self.motor_id} running at {self.rpm} RPM")
    
    def stop(self):
        self.is_running = False
        print(f"Motor {self.motor_id} stopped")

class ObstacleAvoidanceRobot:
    def __init__(self, name):
        self.name = name
        self.front_sensor = DistanceSensor(pin=5, max_range=400)
        self.left_motor = Motor(motor_id=1, rpm=150)
        self.right_motor = Motor(motor_id=2, rpm=150)
    
    def move_forward(self):
        self.left_motor.run()
        self.right_motor.run()
        print(f"{self.name} moving forward")
    
    def turn_right(self):
        self.left_motor.run()
        self.right_motor.stop()
        print(f"{self.name} turning right")
    
    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
        print(f"{self.name} stopped")
    
    def avoid_obstacles(self):
        while True:
            distance = self.front_sensor.read_distance()
            
            if distance > 50:
                self.move_forward()
            else:
                print(f"Obstacle detected at {distance} cm")
                self.turn_right()

# Create and use the robot
my_robot = ObstacleAvoidanceRobot("ObstacleBot")
my_robot.move_forward()
my_robot.avoid_obstacles()
```

---

## Additional OOP Concepts (Introduction)

### **Inheritance**

Create new classes based on existing classes.

```python
class Robot:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"I am {self.name}")

class MobileRobot(Robot):  # Inherits from Robot
    def move(self):
        print(f"{self.name} is moving")

mobile = MobileRobot("TurtleBot")
mobile.introduce()  # Uses inherited method
mobile.move()  # Uses own method
```

### **Encapsulation**

Hide internal details and expose only necessary interfaces.

```python
class Motor:
    def __init__(self):
        self._rpm = 0  # Private attribute (convention)
    
    def set_speed(self, rpm):
        if rpm <= 300:
            self._rpm = rpm
        else:
            print("Speed too high!")
```

---

## Benefits of OOP for Robotics

| Benefit | Example |
|---------|---------|
| **Modularity** | Each robot component (motor, sensor) is a separate class |
| **Reusability** | Use the same Motor class for multiple motors |
| **Maintainability** | Update one class affects all instances |
| **Scalability** | Easy to add new robot types or components |
| **Organization** | Related code grouped logically |
| **ROS Compatibility** | ROS nodes are typically written using OOP |

---

## Key Takeaways

✓ Classes are blueprints that define the structure and behavior of objects

✓ Objects are instances of classes with specific attribute values

✓ Attributes store data describing an object's state

✓ Methods are functions that define what an object can do

✓ The __init__ constructor initializes object attributes

✓ self refers to the current object within methods

✓ OOP makes code more organized, modular, and maintainable

✓ Objects can be created from the same class with different values

✓ Each object maintains its own independent state

✓ OOP is essential for writing complex robotics systems and ROS nodes

✓ Inheritance and encapsulation extend OOP capabilities (covered later)

---

## What's Next?

In the coming days, you'll learn:

- Advanced OOP concepts (inheritance, encapsulation, polymorphism)
- Functions and modules in Python
- Working with libraries and frameworks
- Computer vision fundamentals
- Sensor integration and data processing
- Robot Operating System (ROS/ROS2)
- Real-world robotics projects

---

## Community Engagement

### Connect & Learn Together

| Platform | Link |
|----------|------|
| **Discord** | [https://discord.gg/vq2YS99hDn](https://discord.gg/vq2YS99hDn) |
| **WhatsApp** | [https://chat.whatsapp.com/EZktubsqxvCIGFomiOd0dZ](https://chat.whatsapp.com/EZktubsqxvCIGFomiOd0dZ) |
| **LinkedIn** | [https://linkedin.com/in/aryan-jagushte-07385321b](https://linkedin.com/in/aryan-jagushte-07385321b) |
| **GitHub** | [https://github.com/aryanjagushte/50-Days-of-Robotics](https://github.com/aryanjagushte/50-Days-of-Robotics) |

### Tips for Success

- Fork the GitHub repository to access the complete timetable and resources
- Post your progress on LinkedIn with hashtag **#50DaysOfRobotics**
- Don't hesitate to ask questions in the Discord or WhatsApp communities
- Practice creating simple classes for robot components
- Design classes for different robot types
- Experiment with creating multiple objects from the same class
- Model real robots as Python classes
- Combine OOP with Day 6 concepts (variables, conditionals, loops)
- Start thinking about how you'd structure a complete robot system

---

## References & Resources

- **Video:** [Day 7 - Object-Oriented Programming in Python](https://www.youtube.com/watch?v=z_Er9yal_BU)
- **Repository:** [50-Days-of-Robotics GitHub](https://github.com/aryanjagushte/50-Days-of-Robotics)
- **Additional Learning:**
  - [Python OOP Documentation](https://docs.python.org/3/tutorial/classes.html)
  - [Real Python OOP Guide](https://realpython.com/python3-object-oriented-programming/)
  - ROS Python Client Libraries
  - Design patterns in robotics
  - Advanced inheritance and polymorphism

---

## Remember

*"Grow, learn, and explore together!"* — Aryan Jagushte

Master OOP concepts as they form the foundation for all advanced robotics programming and ROS development. Practice designing classes that represent real robot components and systems. The more you practice structuring your code with classes, the easier it will be to build complex robotic systems. See you in Day 8!

