---
title: Input and Output
description: In this session we will be looking at Python and the filesystem and file structures, how and when they can be used within your Python programs.
prev_know: None
skills:
  - File IO
  - File Paths
  - Pathlib
  - File Extensions
  - File Formats
  - TXT File Format
  - JSON File Format
  - CSV File Format
  - TSV File Format
  - PNG File Format
  - JPG File Format
  - XLS File Format
  - XLSX File Format
  - XLSM File Format
  - ZIP File Format
  - TAR File Format
  - TAR.GZ File Format
date: 02/02/2021
mentors: 
  - TimSando
  - ghandic
links:
  - '[Coursera follow along course](https://www.coursera.org/learn/python-data?specialization=python#syllabus){target=_blank}'
  - '[Real Python - Working with Files](https://realpython.com/working-with-files-in-python/){target=_blank}'
  - '[Real Python - Pathlib](https://realpython.com/python-pathlib/){target=_blank}'
  - '[Real Python - JSON](https://realpython.com/python-json/){target=_blank}'

---

{{ course_summary(title, date, description=description, prev_know=prev_know, skills=skills, mentors=mentors, links=links) }}

## Facts for the session

- When most people refer to the file system, they are generally talking about 'the logical file system' which provides an API layer on which programs can perform certain operations, such as opening, reading, writing, etc. There are two other layers, namely the virtual file system and the physical file system. The virtual file system allows for multiple physical file systems and the physical file system is concerned with the physical way to write data to your hard drive. Luckily this is all abstracted away from us and we can just use the logical file system rather than telling a hard drive to move its arm to a certain point!

## Installing the necessary packages

```bash
pipenv install pandas Pillow xlrd
```

## Working with the file system in Python

### Searching the file system with `os`, `glob` and `pathlib`

We have some data stored in our 'data' folder and our Python scripts are stored in our 'scripts' folder. In `scripts/filesystem.py` we will go through different ways to search our file system as well as best practices for doing so.

The most common technique to search the file system is `os.listdir()` which lists the entries in directory that you give it

```python
import os

entries = os.listdir("../data/")
for entry in entries:
    print(entry)
```

Another way to search file systems is using a glob pattern which can act like a wildcard, for example to find all `.txt` files in a directory we can use a glob pattern of `*.txt`

```python
import glob

entries = glob.glob("../data/*")
for entry in entries:
    print(entry)
```

The way we will be using and is a general best practice since Python 3.5+ is `pathlib` which is an object oriented approach to working with the file system. It combines a lot of other python library functionalities into one package, eg `shutil`, `os`, `glob`

```python
from pathlib import Path

entries = Path.cwd().parent / "data"
for entry in entries.iterdir():
    print(entry.name)
```

### CRUD operations on the filesystem

#### Create

##### Creating directories

We can create a directory (or folder) in Python using the `pathlib` library

```python
from pathlib import Path

path = Path.cwd().parent / "data" / "sub_dir"
path.mkdir(exist_ok=True, parents=True)
```

##### Creating files

To create files we use the python inbuilt function `open` and we need to tell it which mode we want to open it with (read, write or append). This will open up a 'stream', we can then add in whatever data we want to that stream, then when we close it the file will be full of the data and available for other people/programs to see and use.

```python
file = open("demo.txt", mode="w")
file.write("Hello world")
file.close()
```

It is important to ensure we close the stream so it is the best practice to make use of Pythons 'context manager' approach where possible. It will ensure that the stream is closed after we have finished with it and we do not need to tell it to close.

```python
with open("demo.txt", mode="w") as file:
    file.write("Hello world")
```

#### Read

We can read the raw data of any file by using the python inbuilt function `open`, but this time setting the mode to 'read'

```python
with open("demo.txt", mode="r") as file:
    data = file.read()
print(data)
```

#### Update

We can update the raw data of any file by using the python inbuilt function `open`, depending on what kind of updating we want to do we can either open the file in read mode and then in write mode (this will overwrite any existing data and can be done by combining the above approaches) or we can open the file in append mode which will just add data to the end of the file.

```python
# Overwriting
with open("demo.txt", mode="r+") as file:
    data = file.read()
    data = data + "Added text"
    file.write(data)

# Appending
with open("demo.txt", mode="a") as file:
    file.write("Hello world")
```

#### Delete

##### Deleting directories

We can delete a directory using the pathlib library's `Path.rmdir()`, the folder must be empty though!

```python
from pathlib import Path

path = Path.cwd().parent / "data" / "sub_dir"
path.rmdir()
```

##### Deleting files

We can delete a file using the pathlib library's `Path.unlink()`

```python
from pathlib import Path

path = Path.cwd().parent / "data" / "demo.txt"
path.unlink(missing_ok=True)
```

## File structures

Now we are ready to look at file structures, this is just the contents of a file which will be a series of characters or bytes. The key to reading them is to understand the structure of the information. A file extension on its own means nothing, it is the content of the file that determines how to understand it. An extension is just a way to hint how it should be loaded.

### Unstructured text - .txt

`.txt` files are generally used to symbolize that they have unstructured text inside of them and that programs opening them do not need to do any additional steps other than display the raw file contents.

```txt
Do not stand at my grave and weep
I am not there; I do not sleep.
I am a thousand winds that blow,
I am the diamond glints on snow,
I am the sun on ripened grain,
I am the gentle autumn rain.
When you awaken in the morning's hush
I am the swift uplifting rush
Of quiet birds in circled flight.
I am the soft stars that shine at night.
Do not stand at my grave and cry,
I am not there; I did not die.
```

In Python we could open up this file just using the `open("path.txt", mode="r")` and read it in as a string.

```python
from pathlib import Path

path = Path.cwd().parent / "data" / "demo.txt"

with open(path, mode="r") as file:
    data = file.read()
print(data)
```

### Structured data - .json, .csv, .tsv

#### JSON

JSON stands for javascript object notation and is one of the most common file formats on the internet. We can think of this file format as just a Python dictionary as it is more or less the same syntax.

```json
{
    "IDE": "Insight Driven Enterprise",
    "I&D": "Insights and Data",
    "P&O": "People and Organization",
    "APAC": "Asia Pacific"
}
```

In Python we could open up this file and read it into a Python dictionary using the standard library `json`

```python
import json
from pathlib import Path

path = Path.cwd().parent / "data" / "demo.json"

with open(path, mode="r") as file:
    data = json.load(file)
print(data)
```

#### CSV and TSV

`.csv` and `.tsv` stand for comma-separated-value and tab-separated-value, which means the structure of these files will be such that the columns of the data will be separated either by comma's or by tabs

```csv
Name,Age
Bob,22
Harry Jo, 55
```

```tsv
Name    Age
Bob 22
Harry Jo    55
```

These can either be opened using pandas `pd.read_csv()` or by parsing the data yourself, in general it will be faster to use pandas so we will show how to do that.

```python
from pathlib import Path

import pandas as pd

path_csv = Path.cwd().parent / "data" / "demo.csv"
path_tsv = Path.cwd().parent / "data" / "demo.tsv"


data_csv = pd.read_csv(path_csv)
data_tsv = pd.read_csv(path_tsv, sep='\t')

print(data_csv)
print(data_tsv)
```

### Images - .png, .jpg

Images are generally stored as `.jpg` or `.png` and these have a very specific way of being written and is beyond the scope of this course to look into how they are encoded and decoded. However, we can learn how to open them in Python! We can make use of the Pillow library (also called PIL), the Python Image Library.

> Note the main two differences between JPG and PNG are that PNG's can have transparency (or an alpha channel) and that JPG will compress an image to make a smaller file size at the cost of quality. Howvwer PNG will not

```python
from pathlib import Path

from PIL import Image

path_jpg = Path.cwd().parent / "data" / "demo.jpg"
path_png = Path.cwd().parent / "data" / "demo.png"

img_jpg = Image.open(path_jpg)
img_png = Image.open(path_png)
```

### HTML

HTML stands for Hyper Text Markup Language and is used throughout the world inside browsers to display information, HTML has 'tags' which are used to symbolize what that object should be. For instance the tag `<p></p>` is a paragraph tag. There all sorts of tags that can be used, here is a [full list](https://www.w3schools.com/TAGS/default.ASP). The main thing to note here is the tree (or parent child) like structure. You have nestings similar to a JSON but with tags instead of nested dictionaries. Also tags can contain attributes themselves whereas that isn't possible to distinguish in JSON files.

The main library we use for parsing HTML in Python is BeautifulSoup. However, we also generate HTML using another library called Jinja2.

#### Jinja2

First lets look at generating HTML in Python. We can do this using a template, much like we do in string formatting. However, Jinja is a much more powerful and extensible tool for this purpose.

```bash
pipenv install Jinja2
```

```python
from pathlib import Path

from jinja2 import FileSystemLoader, Environment, Template

path = Path.cwd().parent / "data" / "templates"

jinja_env = Environment(loader=FileSystemLoader(path))

template = jinja_env.get_template("demo.html")
formatted_html = template.render(name="Andy Challis")
print(formatted_html)
```

#### BeautifulSoup

Now we can look at parsing HTML, to do this we will use a library called BeautifulSoup

```bash
pipenv install bs4
```

```python
from pathlib import Path

from bs4 import BeautifulSoup

html_path = Path.cwd().parent / "data" / "demo.html"

with open(html_path, mode="r") as file:
    html_file = file.read()

soup = BeautifulSoup(html_file)

title = soup.find("title")
print(title)
print(title.text)

html = soup.find("html")
print(html)
print(html["lang"])
```


### Excel - .xls, .xlsx, .xslm

Excel files and microsoft files in general use proprietary software to create them. However, we can use some Python libraries to manipulate the data if we don't care about making use of the extra functionality from excel such as the formulas. Note that it will process most formulas within the file when reading but when we write an excel file it will not have the formulae. There are ways to get around this but this is beyond the scope of this topic (added for further reading at the bottom)

```python
import pandas as pd

from pathlib import Path

path = Path.cwd().parent / "data" / "demo.xlsx"

data = pd.read_excel(path)
print(data)
```

### Compressed files - .zip, .tar, .tar.gz

Compression works by applying a 'compression scheme' to files and folders by examining the contents and creating essentially a lookup table to replace frequently used sections and replacing them with something smaller. When we decompress we just remap those changes back to get the original file.

Here is a dummy example to show how compression works

```python
from collections import Counter

def compress(s):
    words = s.split()
    freq = Counter(words)
    replacements = {k:str(i) for i, (k, v) in enumerate(freq.most_common())}
    new_words = []
    for word in words:
        new_words.append(replacements[word])
    rev_replacements = {value:key for key, value in replacements.items()}
    return " ".join(new_words), rev_replacements

def decompress(s, replacements):
    words = s.split()
    new_words = []
    for word in words:
        new_words.append(replacements[word])
    return " ".join(new_words)


string = """Do not stand at my grave and weep
I am not there; I do not sleep.
I am a thousand winds that blow,
I am the diamond glints on snow,
I am the sun on ripened grain,
I am the gentle autumn rain.
When you awaken in the morning's hush
I am the swift uplifting rush
Of quiet birds in circled flight.
I am the soft stars that shine at night.
Do not stand at my grave and cry,
I am not there; I did not die."""


compressed, compression_dict = compress(string)
print(compressed)

decompressed = decompress(compressed, compression_dict)
print(decompressed)
```

Now obviously this is a very basic compression scheme and not something we would implement in the real world. Instead we will make use of the `.zip`and `.gz` compression algorithms. We will also be able to tar a folder which will allow us to compress an entire folder and not just a file. Note that zip will do this all in once solution but `gz` or gunzip will need tarring first.

#### zip files

```python
from zipfile import ZipFile
from pathlib import Path

folder = Path.cwd().parent / "data"
zip_path = folder / "demo.zip"

# Writing a zip
with ZipFile(zip_path, 'w') as file:
    file.write(folder / "demo.txt")
    file.write(folder / "demo.csv")

# Reading a zip
with ZipFile(zip_path, 'r') as file:
    data = {name: file.read(name) for name in file.namelist()}
print(data)
```

#### tar.gz files

```python
import tarfile
from pathlib import Path

folder = Path.cwd().parent / "data"
zip_path = folder / "demo.tar.gz"

# Writing a tar.gz
with tarfile.open(zip_path, "w:gz") as tar:
    tar.add(folder / "demo.txt")
    tar.add(folder / "demo.csv")

# Reading a tar.gz
with tarfile.open(zip_path, "r:gz") as tar:
    data = {file.name: tar.extractfile(file).read() for file in tar.getmembers()}
```

### Extra requested content

#### Looping through hundreds of files and updating them

For this example we will create 100 `.csv`'s with 10 random names, save them all out into a folder to make our example dataset. Then we will update all of the files to add an extra column 'address' and save the file back out.

We will use the faker library to create fake data

```bash
pipenv install pandas Faker
```

Part 1 is to generate the data, lets call this python script `datagen.py`

```python
from pathlib import Path

import pandas as pd
from faker import Factory

faker = Factory.create()

# Make the folder if it doesnt exist
folder = Path.cwd().parent / "data" / "csv_demo_data"
folder.mkdir(exist_ok=True, parents=True)

# Make 100 csv file paths
file_paths = [folder / f"demo-{i}.csv" for i in range(100)]

# Loop through all file paths and generate and save the data
for file_path in file_paths:
    # Make dummy data
    nrows = 10
    data = pd.DataFrame({"id": range(1, nrows + 1)})
    # Add random names
    data["full name"] = data["id"].map(lambda _: faker.name())
    # Save data
    data.to_csv(file_path, index=False)
```

Part 2 is to load in the files and update the data, lets call this script `update_data.py`

```python
from pathlib import Path

import pandas as pd
from faker import Factory

faker = Factory.create()

# Folder containing the CVS's
folder = Path.cwd().parent / "data" / "csv_demo_data"

# Get the 100 csv file paths
file_paths = folder.glob("*.csv")

# Loop through all file paths and generate and save the data
for file_path in file_paths:
    # Load the data
    data = pd.read_csv(file_path)
    # Add random addresses
    data["address"] = data["id"].map(lambda _: faker.address().replace("\n", " "))
    # Save data
    data.to_csv(file_path, index=False)

```
