# HBnB Clone Project
This project is a clone of the popular online accommodation marketplace, Airbnb. 

The project includes a command-line interface (CLI) that allows users to interact with the system using simple commands. The CLI allows users to manage properties, bookings, users, and other aspects of the system.

## Command Interpreter
### Starting the Command interpreter
To start the command interpreter, run the console.py file using Python 3
Code: $ python3 console.py

### Using the command interpreter
The command interpreter uses a simple syntax for executing commands:
syntax: $ <command> <class> <id> <attributes>
where:
<command> is the action to be performed (e.g. create, read, update, delete, etc.)
<class> is the name of the class to be manipulated (e.g. User, Property, Booking, etc.)
<id> is the id of the object to be manipulated (optional)
<attributes> are the attributes of the object to be manipulated (optional)

### Examples:
#### Creating a new user:
($ create User name="John" email="john@example.com" password="password")
#### Show a booking:
($ show Booking 456)
