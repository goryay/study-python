# Description

### This repository will contain assignments from the python study book. As the assignments are studied and solved, they will be added here. Not all assignments will be added here, but only the ones I think are necessary. Also in one assignment, several assignments can be combined, as a continuation of one of the assignments.

# Chapter two

[This](https://github.com/goryay/study-python/tree/main/chap_2) shows how to work with variables, simple data types, and
strings. Namely: `f-string`, case change (`lower()`, `upper()`, `title()`), hyphenation (`"\n"`), tabulation (`"\t"`)
and whitespace removal (`rstrip()`, `lstrip()`, `strip()`).

# Chapter three

[In this chapter](https://github.com/goryay/study-python/tree/main/chap_3) was working with lists. Namely, working with
list idexes, deleting, adding and modifying a list, sorting, list lengths.

# Chapter four

[In this chapter](https://github.com/goryay/study-python/tree/main/chap_4) we studied working with lists and tuples.
The for loop, for going through the list and outputting the list data. Also, creating a numeric list (`range()`),
slices(`list([::])`).
Tuples are like lists, they differ only in the fact that they cannot be changed and remain unchanged throughout the life
of the program. If you want to change a tuple, you must assign a new value to the variable where the tuple is stored.

# Chapter five

[In chapter five](https://github.com/goryay/study-python/tree/main/chap_5), we talk about the `if` statement. This
operator is used to check the current state of the program and choose further actions depending on the result of the
check. The center of this expression lays down the result, which is logical true `True` and logical false `False` -
checking the conditions. The equality operator `==`, inequality operator `!=`, and possible mathematical
comparisons `>, <, >=, <=` are also used to check conditions. Logical AND `and` and OR `or` are used to check several
conditions.
If you need to perform different actions depending on whether a condition is true or false, the `if-else` syntax is
used. Sometimes it is necessary to check several possible situations, for this purpose `if-elif-else` is used.

# Chapter six

[Chapter six](https://github.com/goryay/study-python/tree/main/chap_6) is about dictionaries - the key-value
`a = {"color": "red"}`. This data structure is designed to combine
related information. Sometimes it happens that you want to create an empty dictionary `a = {}`, and to add to the
dictionary you need to do the following:

```
a['color'] = 'red'
```

to delete you need to do the following:

```
del a['color']
```

You can also implement a list in the dictionary:

```
a = {
    'color': 'red'
    'alphabet': ['a', 'b', 'c'].
}
```

# Chapter seven

[Chapter 7](https://github.com/goryay/study-python/tree/main/chap_7) talks about the while loop and data entry.

Input `input()` is used to get input data and work with it in the program.

The `while` loop allows you to execute the program until a certain condition remains true.

# Chapter eight

[Chapter eight is devoted to functions](https://github.com/goryay/study-python/tree/main/chap_8) `def`, a named block of
code to accomplish one specific task. To perform a task, you must call the function responsible for that task.

# Chapter nine

[Chapter nine](https://github.com/goryay/study-python/tree/main/chap_9) is about classes. **Object-oriented programming
** is one of the most effective methodologies for creating software products. In **OOP**, there are **classes** *that
describe objects or situations*, and **objects** are created based on these descriptions. Creating an object based on a
class *is creating an instance of the class*.

# Chapter ten

[Chapter Ten](https://github.com/goryay/study-python/tree/main/chap_10). Files and Exceptions. Analyzing large files,
error handling. **Exceptions** - *a special object that is created to manage errors that occur during program
execution*.

# Chapter eleven

[Testing](https://github.com/goryay/study-python/tree/main/chap_11) (`pytest`) - shows that the code will work
correctly. Ensures that the program will not break when adding new code.

```
py -m pip install --upgrade pip
```

# Chapters 12, 13 and 14

Chapters [12](https://github.com/goryay/study-python/tree/main/chap_12), [13](https://github.com/goryay/study-python/tree/main/chap_13)
and [14](https://github.com/goryay/study-python/tree/main/chap_14) show how to use the Pygame package to write
a 2D game [Alien Invasion](https://github.com/goryay/study-python/tree/main/alien_invasion) in which the player must
shoot down alien ships that increase in speed and difficulty
as they fall.

```angular2html
py -m pip install --user pygame
```

# Chapter 15

[Chapter 15](https://github.com/goryay/study-python/tree/main/chap_15) will show you how to visualize data . We will
generate data and create practical, beautiful visualizations of
that data using the packages Matplotlib and Plotly.

```angular2html
py -m pip install --user matplotlib
```

# Chapter 16

[In Chapter 16](https://github.com/goryay/study-python/tree/main/chap_16), we will work with data from network sources
and pass it to a visualization package to create weather data
plots and global seismic activity maps.

# Chapter 17

[Chapter 17](https://github.com/goryay/study-python/tree/main/chap_17) will show how to write a program to automatically
download and visualize data.

```angular2html
py -m pip install --usr requests
```

# Chapters 18, 19 and 20

Chapters [18](https://github.com/goryay/study-python/tree/main/chap_18), [19](https://github.com/goryay/study-python/tree/main/chap_19),
and [20](https://github.com/goryay/study-python/tree/main/chap_20) will show how to write a web application using the
Django package to maintain a web diary on
arbitrary topics. Create an account with a username and password, enter a topic and take notes, deploy the application
to a remote server.

**Creating a virtual environment**

```angular2html
py -m venv ll_env
```

**Activating the virtual environment**

```angular2html
source ll_env/bin/activate
```

**Terminating the virtual environment**

```angular2html
deactivate
```

**Installing Django**

```angular2html
pip install --upgrade pip
pip install django
```

**Creating a project in Django**

```angular2html
django-admin startproject ll_project
ls ll_project
```

**Creating a database**

```angular2html
python manage.py migrate
```

**Launching a project**

```angular2html
python manage.py runserver
```