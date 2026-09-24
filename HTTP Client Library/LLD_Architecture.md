
# LLD Architecture

## 1. Login and Registration Module

- A common dictionary will act as a simple database. It will store usernames as keys and passwords as values.
- This module will use inheritance. The `Login` class will explicitly inherit from the `Register` class.
- Abstract methods are not required because both registration and login need to be implemented. Therefore, using an abstract base class is not helpful here.
- Through inheritance, we can check whether a user attempting to log in is already present in the set of registered users.
- A set stores unique values, which helps ensure that usernames are unique.

### Username Uniqueness Check

- When a user chooses **Register**, the application will check whether the username already exists as a key.
- If the username already exists, an error message will be displayed.
- This functionality will be implemented using `switch` statements.
- The lookup takes $O(1)$ time on average because dictionaries use hashing to find keys quickly.

### Password and User Files

- Passwords will always be stored using `.lower()`.
- A file will be created when a user registers.
- For every new user, a separate file will be created to store their history, logs, and shared information.
- If a user logs in and their file already exists, new logs will continue to be added to that file.
- The files will be named using the username, such as `username.txt`. After login, the application can find the logged-in user's file by using their username.

## 2. Request Module

- A class named `SendRequest` will be responsible only for sending requests.
- Another class will contain methods such as `GET`, `POST`, `PUT`, and `DELETE`. These methods can access the `SendRequest` class.
- Single inheritance will be used in this module.
- Sockets will be used to initiate and close requests.
- The remaining networking work will be handled by the operating system's TCP stack.

### Supported Methods

- `GET`
- `POST`
- `PUT`
- `DELETE`

The user will choose a method and enter a URL. The URL will be passed as a string, and the output from the selected method will be displayed in both the file and the terminal.

File handling will be a new part of the project, including creating and writing to files.

## 3. Main Module

`Main.py` will import the classes from the other files. It will call the components in sequence and control the overall process.

## 4. Importing Classes

Classes will be imported using the following syntax:

```python
from file_name import ClassName
```

## 5. Learning Objectives

This project will help us understand how object-oriented programming works collaboratively across a project. It will also provide practice with built-in data structures.

The main topics covered will be:

- File methods and file handling
- Error handling
- Object-oriented programming
- Modular and reusable code
- The use of the same structure when learning frameworks
- The purpose and use of `__slots__`

Object-oriented programming is not only about writing classes. It is about creating modular code, adding features without breaking the entire project, finding and updating specific parts of the code, and choosing the right tools for each situation.
