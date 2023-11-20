<!--

author:   Meredith Lee
email:    leemc@chop.edu
version: 1.1.0
current_version_description: Added clarifying language about `.pop()` method, added more thorough explanation of the correct answer to the second dictionary quiz question, explained that there is no requirement to memorize methods, and fixed quiz answer checking that was throwing an error for double quotes.
module_type: standard
docs_version: 3.0.0
language: en
narrator: UK English Female
mode: Textbook

title: Python Basics: Lists and Dictionaries

comment: Learn about collection objects, specifically lists and dictionaries, in Python.

long_description: Before using Python for data analysis, there are some basics to learn that will set the foundation for more advanced Python coding. This module will teach you about lists and dictionaries, two types of collection objects in Python. 

estimated_time_in_minutes: 15

@pre_reqs
Learners should be able to recognize functions, methods, and variables in Python.
@end

@learning_objectives

After completion of this module, learners will be able to:

- Create and edit lists
- Create and edit dictionaries

@end

good_first_module: false
collection: learn_to_code
sequence_name: python_basics
previous_sequential_module: python_basics_variables_functions_methods
coding_required: true
coding_level: basic
coding_language: python

@sets_you_up_for

- python_basics_loops_conditionals
- python_basics_exercise
- pandas_transform

@end

@depends_on_knowledge_available_in

- demystifying_python
- python_basics_variables_functions_methods

@end


@version_history
Previous versions: 

[1.0.1](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/279f48bab219dd4622888a6301b7ca5b48880370/python_basics_lists_dictionaries/python_basics_lists_dictionaries.md#1): Initial version
@end

import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros.md
import: https://raw.githubusercontent.com/arcus/education_modules/main/_module_templates/macros_python.md

-->

# Python Basics: Lists and Dictionaries

@overview

## Lesson Preparation

@sage

@lesson_prep_python_sage

## Collection Objects in Python

How information is stored and organized is an important part of programming. Python has specific data types called **collections** that store and organize information in different ways. This module will discuss two of the most common and useful types of collections: lists and dictionaries. 

<div class = "learn-more">
<b style="color: rgb(var(--color-highlight));">Learning connection</b><br>

There are a couple of other collections, called [tuples](https://www.geeksforgeeks.org/python-tuples/) and [sets](https://www.geeksforgeeks.org/sets-in-python/); you can read more about those on your own if you're interested. 

</div>


## Lists

**Lists** in Python are objects that contain a collection of multiple items. They are surrounded by square brackets `[ ]` and the items in the list are separated by commas:

@sage
<div class="python_link">
<lia-keep>
<script type="text/x-sage">

produce = ["tomato", "squash", "apple", "cucumber", "peach", "spinach"]
print(produce)

</script>
</lia-keep>
</div>

There are a few important characteristics of lists:

* Lists can have duplicate values. An example might be the list `[3, 1, 4, 1, 5, 9]`, where the number 1 appears twice.

* List items don't all have to be of the same type (you can have a mix of strings and numbers, for example, or even a list of lists). `[3.14, "pi", False, ["number", "string", "boolean"]]` is an example of a list that contains a float, a string, a boolean value, and a list as its elements.

* Lists are **ordered**: List items remain in the position that they are entered into the list, and you can access any item by its position, or **index**.

    <div class = "important">
    <b style="color: rgb(var(--color-highlight));">Important note</b><br>

    An **index** in Python refers to a value's position in a sequence. The sequence can be a collection object like a list or even a string (which you can think of as a sequence of characters). The important thing to remember is that in Python, **indices start at 0**. This means that the index of the first item in a sequence is `0`! This is not always the case in other programming languages.

    To access an item by its index, you use **subsetting notation**, `sequence[index]`. To get the first letter of the string "Hello" (strings can be thought of as a sequence of characters), for example, you would use the code `"Hello"[0]`. Notice that this is another use of square brackets!

    </div>

* Lists are **changeable**; you can add, remove, and edit items in a list. You can use list [methods](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/python_basics_variables_functions_methods/python_basics_variables_functions_methods.md#6) to do this.

### List methods

Because Python lists are changeable, you'll need to know a few ways to change them! First, let's build our `produce` list again. 

@sage
<div class="python_link">
<lia-keep>
<script type="text/x-sage">

produce = ["tomato", "squash", "apple", "cucumber", "peach", "spinach"]
print(produce)

</script>
</lia-keep>
</div>

Below are a few of the most commonly-used list methods, but not the only ones; you can read more about list methods in the [Python documentation about lists](https://docs.python.org/3/tutorial/datastructures.html).
 
* **`.pop()`** removes a specific element by **index** and *returns that element*. Run the code below to see the output of `produce.pop(0)`.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    print(produce.pop(0))

    </script>
    </lia-keep>
    </div>

    The element at index `0` (the first position in the list) has now been removed from `produce`:

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    print(produce)

    </script>
    </lia-keep>
    </div>

* **`.remove()`** removes a specific element by **value**.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    produce.remove("apple")
print(produce)

    </script>
    </lia-keep>
    </div>

    Note that the `.remove()` method, unlike `.pop()`, does not itself return any output. If you want to see what happens if you run `print(produce.remove('apple'))`, try changing the code block above (be sure to re-run all of the code blocks above it!).

  
    <div class = "options">
    <b style="color: rgb(var(--color-highlight));">Another option</b><br>

    Another option for removing an element from a list by its index is **`del`**. The syntax for using `del` will be a little different, because it is a [**keyword**](https://realpython.com/python-keywords/), not a list method. It is useful because it allows you to delete list elements in a **slice**. Slicing uses subsetting notation to indicate where the slice begins and ends. The first index listed is **inclusive**, or included in the slice; this is followed by a colon; the second index listed is **exclusive**, or excluded from the slice; finally, these numbers are surrounded by square brackets.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    del produce[1:3]
print(produce)

    </script>
    </lia-keep>
    </div>

    </div>


* **`.clear()`** removes everything from the list.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    produce.clear()
print(produce)

    </script>
    </lia-keep>
    </div>

* **`.append()`** adds an element to the end of a list.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    produce.append("pear")
print(produce)

    </script>
    </lia-keep>
    </div>

* **`.insert()`** adds an element to a specific position.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    produce.insert(0, "kale")
print(produce)

    </script>
    </lia-keep>
    </div>

* **`.extend()`** adds another list to your list (or another iterable object, but don't worry about that for now).

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">
    berries= ["strawberry", "blueberry", "raspberries"]
produce.extend(berries)
print(produce)

    </script>
    </lia-keep>
    </div>


You'll notice that with each step, our list `produce` has been permanently changed-- in order to "start over" with the original list, we simply need to re-run the first code chunk.

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

The code cells above are linked, meaning that all of the cells "remember" the code that has been run previously (as they would be in a [notebook](https://liascript.github.io/course/?https://raw.githubusercontent.com/arcus/education_modules/main/demystifying_python/demystifying_python.md#jupyter-notebooks)). Because of this, if you run them out of order, you can get unexpected results or even errors! If things aren't working like they should, re-run the first code cell on the page or hit your refresh button.

</div>

### Quiz: Lists

1. Which of the following is FALSE about lists? Select all that apply.

    [( )] Lists are changeable; items can be added, removed, or replaced after the list is created.
    [( )] Lists can be assigned to variables.
    [( )] Lists can contain a mix of data types.
    [(X)] Lists are unordered; you cannot access an item in the list by its position.
    ***
    <div class = "answer">

    Lists are changeable, can be stored in variables for later use (even though we didn't explicitly discuss it, the list on the previous page was assigned to the variable `produce`), can contain a mix of data types, and they are **ordered**, meaning that items remain in the position that they were put into the list. You can access or edit list items by value **or** position (also called the **index**).

    </div>
    ***

2. Given the following list of numbers, what is the **index** of the number **15**?

    `[2, 14, 9, 101, 15, 37]`

    [( )] 5
    [(X)] 4
    [( )] 15
    [( )] 6
    ***
    <div class = "answer">

    Indexing in Python begins with **0**, not 1, and so the index of 15, which is the fifth item in the list, is **4**.  

    </div>
    ***

## Dictionaries

Another kind of collection object in Python is a **dictionary**. Dictionaries are similar to lists in some ways, in that they are ordered (in recent versions of Python; in older versions, dictionaries are unordered) and changeable. However, there are some important distinctions:

* Dictionaries are collections of **key-value pairs**. For example if you had a dictionary of demographic information for an individual, the **keys** might be the type of information stored (address, telephone number, etc.) and the **values** would be the actual values of those data (123 Puppydog Lane, 987-654-3210).

* They do not allow duplicate key-value pairs.

* Dictionaries use curly brackets `{ }` (unlike lists, which use square brackets `[ ]`). These curly brackets can also be called **braces**.

Let's build an example dictionary:

@sage
<div class="python_link">
<lia-keep>
<script type="text/x-sage">

contact_info = {"address" : "123 Puppydog Lane",
                "telephone" : "987-654-3210",
                "email" : "myname@email.com"}
print(contact_info)

</script>
</lia-keep>
</div>

### Dictionary methods

@sage
<div class="python_link">
<lia-keep>
<script type="text/x-sage">

contact_info = {"address" : "123 Puppydog Lane",
                "telephone" : "987-654-3210",
                "email" : "myname@email.com"}
print(contact_info)

</script>
</lia-keep>
</div>

Like lists, dictionaries have some useful methods you can use to access or alter their data:

* **`.keys()`** returns a list of the dictionary's keys.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    print(contact_info.keys())

    </script>
    </lia-keep>
    </div>

* **`.values()`** returns a list of the dictionary's values.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    print(contact_info.values())

    </script>
    </lia-keep>
    </div>

* **`.items()`** returns a list of the dictionary's key-value pairs as tuples (an object that holds multiple values, similar to a list, except that they are *unchangeable*). This may seem not very useful at first glance, but since different collection objects have different properties, there could be circumstances in which it is more useful to have the data in a different kind of object.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    print(contact_info.items())

    </script>
    </lia-keep>
    </div>

* **`.pop()`** works similarly for dictionaries as it does for lists, except that it removes an element by its key.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    print(contact_info.pop("email"))
print(contact_info)

    </script>
    </lia-keep>
    </div>

    <div class = "help">
    <b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

    Note that this change is permanent! If you want to keep the original dictionary as-is, you should make a copy of the dictionary (using the `.copy()` method and assigning the copy to a new variable), and then using `.pop()` on the copy:

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    contact_info_copy = contact_info.copy()
contact_info_copy.pop("telephone")
print(contact_info)
print(contact_info_copy)

    </script>
    </lia-keep>
    </div>

    In this example though, all you need to do to restore the dictionary to its original form is re-run the first code cell or refresh the page.
    </div>

* There isn't a method to add items to a dictionary, but it can be done! You can give the dictionary a new key and assign a value to it (notice that we're using square bracket notation again, like we did for lists). This is another example of a permanent change to our dictionary.

    @sage
    <div class="python_link">
    <lia-keep>
    <script type="text/x-sage">

    contact_info["work_email"] = "myname@company.com"
print(contact_info)

    </script>
    </lia-keep>
    </div>

  You can also use the same syntax with an existing key to assign a new value (note that the new value will **replace** the previous value).

<div class = "help">
<b style="color: rgb(var(--color-highlight));">Troubleshooting help</b><br>

You might have noticed by now that we have used square brackets in a few different contexts, and it can be difficult to keep straight! Here are the three uses you need to know for this module:

1. Creating lists: You use square brackets to create a list object (either an empty list or one that has items in it).

2. Accessing items in a collection: This is the subsetting notation that we talked about earlier, and it used to retrieve an item in a list or a dictionary. You do this by using the index in a list and by the key in a dictionary. 

3. Adding items to a dictionary. 

</div>

<div class = "care">
<b style="color: rgb(var(--color-highlight));">A little encouragement...</b><br>

We've just gone through quite a few useful list and dictionary methods, and you might be concerned about remembering them all! There's no need to memorize them all right now-- it's likely that you'll start to remember them as you use them more, but in the meantime, refer back to this module whenever you need to. 

</div>


### Quiz: Dictionaries

1. True or False: Duplicate key-value pairs are allowed in dictionaries.

    [( )] True
    [(X)] False
    ***
    <div class = "answer">

    While **values** can be repeated in a dictionary, each **key** must be unique. However, you can have multiple values for a key by putting those values in a list.

    </div>
    ***

2. How would you access all of the countries (the "keys") in the dictionary below? 

     `capital_cities = {"Afghanistan" : "Kabul", "Albania" : "Tirana", "Algeria" : "Algiers", "Andorra" : "Andorra la Vella"}`

    [[capital_cities.keys()]]
    <script>
  let input = "@'input".trim();
  input == "capital_cities.keys()";
</script>
    ***
    <div class = "answer">

    To return the keys of a dictionary, you use the `.keys()` dictionary method on the `capital_cities` dictionary. So the correct answer is `capital_cities.keys()`.

    </div>
    ***

3. How would you add the the country of Angola and its capital city of Luanda to the dictionary below?

    `capital_cities = {"Afghanistan" : "Kabul", "Albania" : "Tirana", "Algeria" : "Algiers", "Andorra" : "Andorra la Vella"}`

    [[capital_cities["Angola"] = "Luanda"]]
    <script>
    let input = "@'input".replace(/\s/g, "");
    input == 'capital_cities["Angola"]="Luanda"' || input == "capital_cities['Angola']='Luanda'";
    </script>
    ***
    <div class = "answer">

    To add a new key-value pair to a dictionary, we use subsetting notation.

    </div>
    ***


## Additional Resources

* There are many helpful resources on [python.org](https://www.python.org/), including a [Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide) and [FAQs](https://docs.python.org/3/faq/).

* Python docs also has [more detailed information about using lists, dictionaries, and other data structures](https://docs.python.org/3/tutorial/datastructures.html). 

## Feedback

@feedback