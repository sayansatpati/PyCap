# Tasks

## "Sprint" 1

### Task 1

**Make a function called `extract_age` that extracts the age from a string and converts it to an integer**

!!! summary "Expected usage"
    ```python
    extract_age("5 years old")  # Should return 5 as integer
    extract_age("1 year old")  # Should return 1 as integer
    ```

??? example "Sample solution"
    ```python
    def extract_age(age_description):
        trimmed = age_description.replace(" years old", "").replace(" year old", "")
        return int(trimmed)
    ```

### Task 2

**Make a function called `extract_meal_names` that extracts meal names from a list of dictionaries**

!!! summary "Expected usage"
    ```python
    extract_meal_names([{"name": "pizza", "calories": 999.23}])  # Should return ["pizza"]
    extract_meal_names([{"name": "pizza", "calories": 999.23}, {"name": "apples", "calories": 50}])  # Should return ["pizza", "apples"]
    ```

??? example "Sample solution"
    ```python
    def extract_meal_names(meals):
        meal_names = []
        for meal in meals:
            meal_names.append(meal["name"])
        return meal_names
    ```


### Task 3

**Extend `extract_meal_names` to only return unique meal names and they should be sorted alphabetically**

!!! summary "Expected usage"
    ```python
    extract_meal_names([{"name": "pizza", "calories": 999.23}])  # Should return ["pizza"]
    extract_meal_names([{"name": "pizza", "calories": 999.23}, {"name": "apples", "calories": 50}])  # Should return ["pizza", "apples"]
    extract_meal_names([{"name": "pizza", "calories": 999.23}, {"name": "apples", "calories": 50}, {"name": "apples", "calories": 50}])  # Should return ["pizza", "apples"]
    ```

??? example "Sample solution"
    ```python
    def extract_meal_names(meals):
        meal_names = set()
        for meal in meals:
            meal_names.add(meal["name"])
        return sorted(list(meal_names))
    ```

### Task 4

**Make a function called `extract_calorie_intake` that finds the total calorie intake**

!!! summary "Expected usage"
    ```python
    extract_calorie_intake([{"name": "pizza", "calories": 999.23}])  # Should return 999.23
    extract_calorie_intake([{"name": "pizza", "calories": 999.23}, {"name": "apples", "calories": 50}])  # Should return 1049.23
    extract_calorie_intake([{"name": "pizza", "calories": 999.23}, {"name": "apples", "calories": 50}, {"name": "apples", "calories": 50}])  # Should return 1099.23
    extract_calorie_intake([{"name": "apples", "calories": 50}, {"name": "celery", "calories": -50}])  # Should return 0
    ```

??? example "Sample solution"
    ```python
    def extract_calorie_intake(meals):
        total_intake = 0
        for meal in meals:
            total_intake = total_intake + meal["calories"]
        return total_intake
    ```

### Task 5

**Make a function called `flatten_person` that flattens the given information into the expected format**

!!! summary "Expected usage"
    ```python
    # Given
    person = {
        "name": "Andrew",
        "age": "5 years old",
        "meals": [
            {"name": "pizza", "calories": 999.23},
            {"name": "apples", "calories": 50},
            {"name": "apples", "calories": 50},
        ],
        "happy": True,
        "location": {"city": "Melbourne", "coords": (1000, 3002)},
        "optional_nickname": "Andy",
    }

    flatten_person(person)

    # Should return
    {
        "name": "Andrew",
        "age": 5,
        "meals": "apples, pizza",
        "calorie_intake": 1099.23,
        "happy": True,
        "latitude": 1000,
        "longitude": 3002,
        "nickname": "Andy",
    }
    
    ```

??? example "Sample solution"
    ```python
    def flatten_person(person):
        return {
            "name": person["name"],
            "age": extract_age(person["age"]),
            "meals": ", ".join(extract_meal_names(person["meals"])),
            "calorie_intake": extract_calorie_intake(person["meals"]),
            "happy": person["happy"],
            "latitude": person["location"]["coords"][0],
            "longitude": person["location"]["coords"][1],
            "nickname": person.get("optional_nickname", ""),
        }
    ```

### Task 6

**Make a function called `flatten_people` that flattens a list of people, but only uses them if they are happy**

!!! summary "Expected usage"
    ```python
    # Given
    people = [
        {
            "name": "Andrew",
            "age": "5 years old",
            "meals": [
                {"name": "pizza", "calories": 999.23},
                {"name": "apples", "calories": 50},
                {"name": "apples", "calories": 50},
            ],
            "happy": True,
            "location": {"city": "Melbourne", "coords": (1000, 3002)},
            "optional_nickname": "Andy",
        },
        {
            "name": "Jane",
            "age": "1 year old",
            "meals": [
                {"name": "celery", "calories": -50},
                {"name": "apples", "calories": 50},
                {"name": "apples", "calories": 50},
            ],
            "happy": False,
            "location": {"city": "New York", "coords": (3009, 10)},
            "optional_nickname": "Jan",
        },
    ]

    flatten_people(people)

    # Should return
    [
        {
            "name": "Andrew",
            "age": 5,
            "meals": "apples, pizza",
            "calorie_intake": 1099.23,
            "happy": True,
            "latitude": 1000,
            "longitude": 3002,
            "nickname": "Andy",
        }
    ]
    ```

??? example "Sample solution"
    ```python
    def flatten_people(people):
        happy_people = []
        for person in people:
            if person["happy"]:
                happy_people.append(flatten_person(person))
        return happy_people
    ```

## "Sprint" 2

### Task 7

**Build a python data model class called `Person` that defines the information we will be receiving**

!!! summary "Expected usage"
    ```python
    [
        {
            "name": "Andrew",
            "age" "5 years old",
            "meals": [
                {"name": "pizza", "calories": 999.23},
                {"name": "apples", "calories": 50},
                {"name": "apples", "calories": 50}
            ],
            "happy": true,
            "location": {
                "city": "Melbourne",
                "coords": (1000,3002)
            },
            "optional_nickname": "Andy"
        }
    ]
    ```

??? example "Sample solution"
    ```python
    from dataclasses import dataclass
    from typing import Optional, List, Tuple

    @dataclass
    class Meal:
        name: str
        calories: float


    @dataclass
    class Location:
        city: str
        coords: Tuple[float, float]


    @dataclass
    class Person:
        name: str
        age: str
        meals: List[Meal]
        happy: bool
        location: Location
        optional_nickname: Optional[str]

    Person(
        **{
            "name": "Andrew",
            "age": "5 years old",
            "meals": [
                {"name": "pizza", "calories": 999.23},
                {"name": "apples", "calories": 50},
                {"name": "apples", "calories": 50},
            ],
            "happy": True,
            "location": {"city": "Melbourne", "coords": (1000, 3002)},
            "optional_nickname": "Andy",
        }
    )
    ```

### Task 8

**Refactor your code to use multiple modules to tidy up**

### Task 9

**Read in a JSON file with data to process and run it through your `flatten_people` function**

??? example "Sample solution"
    ```python
    import json

    with open("data.json", "r") as f:
        people = json.load(f)

    flatten_people(people)
    ```

### Task 10

**Write out the information you have processed through `flatten_people` function into a CSV file**

??? example "Sample solution"
    ```python
    import json

    import pandas as pd

    with open("data.json", "r") as f:
        people = json.load(f)

    flattened = flatten_people(people)
    data = pd.DataFrame(flattened)
    data.to_csv("flattened_people.csv")

    ```

## "Sprint" 3

### Task 11

**Add type annotations to your user defined functions**

### Task 12

**Add docstrings and inline comments to your user defined functions**

### Task 13

**Create a README.md defining how to use your ETL program**

### Task 14

**Create unit tests for your user defined functions with edge cases and ensure 100% coverage**

### Task 15

**Ensure your code is well formatted and passes standard linting rules**

## "Sprint" 4

### Task 16

**Build your program into a commandline application using `typer` or `pick`**

### Task 17

**Add in error handling so that users that misuse your program get some feedback on how they can correct their mistakes**

### Task 18

**Iterate on unit tests to uplift your coverage back to 100%**

## "Sprint" 5

### Task 19

**Add version control to your project by making it into a git repository**

### Task 20

**Push your application to GitHub so that you can work collaboratively with others on the project**
