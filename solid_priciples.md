
1. **Single Responsibility Principle (SRP):**

The Single Responsibility Principle states that a class should have only one reason to change. In other words, it should have only one responsibility. Let's consider an example where a class violates SRP and then refactor it to adhere to the principle.

```python
# Violating SRP
class Customer:
    def __init__(self, name):
        self.name = name
    
    def save_to_database(self):
        # Code to save customer to the database
        pass
    
    def send_notification(self):
        # Code to send notification to the customer
        pass
```

In this example, the `Customer` class handles both saving to the database and sending notifications. Let's refactor it to follow SRP:

```python
# Adhering to SRP
class Customer:
    def __init__(self, name):
        self.name = name

class CustomerRepository:
    def save(self, customer):
        # Code to save customer to the database
        pass

class NotificationService:
    def send_notification(self, customer):
        # Code to send notification to the customer
        pass
```

2. **Open/Closed Principle (OCP):**

The Open/Closed Principle states that software entities should be open for extension but closed for modification. Let's consider an example of a shape calculation system.

```python
# Violating OCP
class AreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return 3.14 * shape.radius ** 2
```

In this example, if we want to add a new shape (e.g., Triangle), we would need to modify the `AreaCalculator` class. Let's refactor it to adhere to OCP:

```python
# Adhering to OCP
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

class AreaCalculator:
    def calculate_area(self, shape):
        return shape.calculate_area()
```

Now, adding a new shape involves creating a new class that inherits from `Shape` and implements the `calculate_area` method, without modifying existing code.

In the next response, I'll continue with the examples for Liskov Substitution Principle, Interface Segregation Principle, and Dependency Inversion Principle.

Of course! Let's continue with examples for the remaining SOLID principles:

3. **Liskov Substitution Principle (LSP):**

The Liskov Substitution Principle states that objects of a derived class should be able to replace objects of the base class without affecting the correctness of the program. Let's look at an example involving geometric shapes.

```python
# Violating LSP
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
```

In this example, a `Square` class inherits from `Rectangle`, but it violates the Liskov Substitution Principle because a square's width and height cannot be independently set as in a rectangle.

```python
# Adhering to LSP
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2
```

Here, both `Rectangle` and `Square` are implementing the `Shape` interface, and their behavior respects the Liskov Substitution Principle.

4. **Interface Segregation Principle (ISP):**

The Interface Segregation Principle states that clients should not be forced to depend on interfaces they do not use. Let's consider an example involving devices with different capabilities.

```python
# Violating ISP
class Device(ABC):
    @abstractmethod
    def print_document(self, document):
        pass
    
    @abstractmethod
    def fax_document(self, document):
        pass
    
    @abstractmethod
    def scan_document(self, document):
        pass

class MultiFunctionPrinter(Device):
    def print_document(self, document):
        pass
    
    def fax_document(self, document):
        pass
    
    def scan_document(self, document):
        pass
```

In this example, not all devices need all three functionalities. Let's refactor it to follow ISP:

```python
# Adhering to ISP
class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax_document(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass

class MultiFunctionPrinter(Printer, Fax, Scanner):
    def print_document(self, document):
        pass
    
    def fax_document(self, document):
        pass
    
    def scan_document(self, document):
        pass
```

By splitting the interfaces, we allow clients to depend only on the functionalities they need.

5. **Dependency Inversion Principle (DIP):**

The Dependency Inversion Principle suggests that high-level modules should not depend on low-level modules, but both should depend on abstractions. Let's see an example involving a notification system.

```python
# Violating DIP
class EmailNotifier:
    def send_email(self, recipient, message):
        pass

class NotificationService:
    def __init__(self):
        self.email_notifier = EmailNotifier()

    def send_notification(self, recipient, message):
        self.email_notifier.send_email(recipient, message)
```

In this example, the `NotificationService` directly depends on `EmailNotifier`, violating the DIP. Let's refactor it:

```python
# Adhering to DIP
class Notifier(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass

class EmailNotifier(Notifier):
    def send(self, recipient, message):
        pass

class NotificationService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def send_notification(self, recipient, message):
        self.notifier.send(recipient, message)
```

By passing an instance of `Notifier` to `NotificationService`, we've adhered to the Dependency Inversion Principle. The high-level `NotificationService` now depends on the abstraction `Notifier`, allowing for easy substitution of notification mechanisms.

These examples showcase how the SOLID principles can guide the design and structure of your code, leading to more maintainable, extensible, and robust software systems.

Adhering to the SOLID principles can lead to software that is easier to understand, maintain, and extend. They promote good design practices, reduce code smells, and help prevent common pitfalls that can arise in the software development process. However, it's important to note that these principles are not strict rules that must be followed in all cases; rather, they provide guidelines and best practices that can be adapted to the specific needs and context of a project.