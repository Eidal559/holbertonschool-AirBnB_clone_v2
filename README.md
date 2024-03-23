# HBNB - The Console
![logo Image](image/hbnb_logo.jpg "An example image stored in the repository")


## Description

The HBNB project embarks on recreating the AirBnB experience through a clone web application. This repository focuses on the backend portion, specifically on developing a command-line console that serves as an interface for data management. The console enables CRUD operations—Create, Read, Update, Delete—on objects and ensures data persistence through JSON serialization.

## Table of Contents

- [HBNB - The Console](#hbnb---the-console)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Repository Contents](#repository-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Console Commands](#console-commands)
    - [Examples](#examples)
  - [Testing](#testing)
  - [Contributors](#contributors)
  - [License](#license)

## Repository Contents

| File/Directory        | Location           | Description                                                            |
|-----------------------|--------------------|------------------------------------------------------------------------|
| `AUTHORS`             | Root               | A file listing individuals who have contributed to the project.       |
| `/models`             | Root               | Directory containing classes used throughout the project.             |
| `base_model.py`       | `/models`          | Defines the BaseModel class, the foundational class for all other models. |
| `/engine`             | `/models`          | Directory housing the storage mechanisms.                             |
| `file_storage.py`     | `/models/engine`   | Manages serialization and deserialization of objects to and from JSON.|
| `db_storage.py`       | `/models/engine`   | Handles MySQL database storage operations.                            |
| `/tests`              | Root               | Contains unit tests for all classes and storage engines.              |
| `console.py`          | Root               | The command-line interface for the project.                           |

## Installation

Follow these steps to get a copy of the project up and running on your local machine for development and testing purposes:

1. Clone the repository:
    ```bash
    git clone https://github.com/Eidal559/holbertonschool-AirBnB_clone_v2.git
    ```

2. Navigate into the cloned repository directory:
    ```bash
    cd  /holbertonschool-AirBnB_clone_v2/
    ```

## Usage

### Console Commands

After launching the console, you can use the following commands:

- `create`: Creates a new instance of BaseModel, saves it to the JSON file, and prints the id.
- `show`: Prints the string representation of an instance based on class name and id.
- `destroy`: Deletes an instance based on class name and id.
- `all`: Prints all string representation of instances based or not on the class name.
- `update`: Updates an instance based on class name and id by adding or updating an attribute.

### Examples

- 1. Creating a new BaseModel instance:
    ```bash
    (hbnb) create BaseModel
    ```
    ```bash
    (hbnb) create BaseModel
    9e2f4018-36b3-41de-b703-74e58fbe2c13
    ```

- 2. Showing an existing BaseModel instance:
    ```bash
    (hbnb) show BaseModel 9e2f4018-36b3-41de-b703-74e58fbe2c13
    ```
    ```bash
    (hbnb) show BaseModel 9e2f4018-36b3-41de-b703-74e58fbe2c13
    [BaseModel] (9e2f4018-36b3-41de-b703-74e58fbe2c13) 
    {'id': '9e2f4018-36b3-41de-b703-74e58fbe2c13', 'created_at': datetime.datetime(2024, 3, 22, 19, 7, 15, 988895), 
    'updated_at': datetime.datetime(2024, 3, 22, 19, 7, 15, 988905)}
    ```
- 3. Updating an attribute of an instance:
    ```bash
    (hbnb) update BaseModel 1234-1234-1234 email "hbnb@holbertonschool.com"
    ```
- 4. Destroy an existing BaseModel instance: 
    ```shell
    (hbnb) destroy BaseModel 9e2f4018-36b3-41de-b703-74e58fbe2c13
    (hbnb) show BaseModel 9e2f4018-36b3-41de-b703-74e58fbe2c13
    ** no instance found **
    ```

## Alternative Syntax

### Example 0: Show all User objects

**Usage**: `<class_name>.all()`

```shell
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2024, 3, 22, 19, 7, 15, 988895), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2024, 3, 22, 19, 7, 15, 988895)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2024, 3, 22, 19, 7, 15, 988895), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2024, 3, 22, 19, 7, 15, 988895)}"]
```

### Example 1: Destroy a User

**Usage**: `<class_name>.destroy(<_id>)`

```shell
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb) 
(hbnb) User.all()
["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2024, 3, 22, 19, 7, 15, 988895), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2024, 3, 22, 19, 7, 15, 988895)}"]
```
### Example 2: Update User (by attribute)

**Usage**: `<class_name>.update(<_id>, <attribute_name>, <attribute_value>)`

```shell
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", "name", "Todd the Toad")
(hbnb) 
(hbnb) User.all()
["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2024, 3, 22, 19, 7, 15, 988895), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2024, 3, 22, 19, 7, 15, 988895)}"]
```
### Example 3: Update User (by dictionary)

**Usage**: `<class_name>.update(<_id>, <dictionary_of_attributes>)`

```shell
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb) 
(hbnb) User.all()
["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2024, 3, 22, 19, 7, 15, 988895), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2024, 3, 22, 19, 7, 15, 988895)}"]
```

## Testing

Execute the following command in the root directory to run the unit tests:

```bash
python3 -m unittest discover tests
