# Day-6-to-10
## Thoughts and Actions 
So it took me about two weeks to complete lessons 6 to 10. I've learned and struggled a lot, and I honestly am thinking of going back to re-do the projects (this time without help) before I start on the capstone project that is associated with Day 11. 

This journey of learning the basics python is taking much longer than I thought. I honestly believed that I could do a lesson a day HAHA. I'm kind of glad that I'm learning this at my own pace, I feel like if I was taking a class at a university, for example, I definitely would not have been able to grasp the concepts, let alone have the time to re-attempt a project. 

There are a few things that I am thinking about during this journey. The big, obviously, is doubt. Am I learning at a good pace? Am I even learning anything in general? Will I be able to make use of what I learn here? Why is everything so hard, and why am I not able to understand basic things? To be honest, I'm having a hard time making connections, but I also believe that with time I should be able to read a task and think of a few ways to solve it. 

So this repository is going to serve as my notes from the past few lessons, as well as something to look back on as I progress in my journey to learn how to code in python. 

## Lessons learned from Day 6 to 10
- Functions: basically a title for a block of code that you can call on.
  ``` javascript
  def my_function():
    print("Hello")
    print("bye")
  ```
   - calling a function can look like this:
     ```javascript
     my_function()
     ```
- Loops
   - for loops - to iterate over a certain amount of items. Requires a sequence usually a list, tuple, dictionary, etc.
   - while loops - While loop is used to repeatedly execute a block of statements while a condition is true.
   - example of a while loop:
        ``` javascript
        number_of_hurdles = 6
        while number_of_hurdles > 0:
          jumping()
          number_of_hurdles -= 1
          print(number_of_hurdles)
        ```
- Functions with Input
    - usually inside the parenthesis.
    - for example, the input here would be "name":
         ``` javascript
         def greet_with_name(name):
           print(f"How are you, {name}")
           print (f"all good, right, {name}?")
           print(f"well, {name}, at least its friday")
         ```
    - positional vs. keyword arguments
    - example:
         ``` javascript
         def greet_with(name, location):
             print(f"hello, {name}")
             print(f"what is it like in {location}?")
         positional = greet_with("adeline", "los angeles")
         keyword = greet_with(location = "San Diego", name = "adeline")
         ```
- dictionaries: It's a data structure that allows us to associate a key to a value and pair the two pieces of data together.
    - format is this = {key:value,}
         ``` javascript
         programming_dictionary = {
        "Bug": "An error in a program that prevents the program from running as expected.",
        "Function": "A piece of code that you can easily call over and over again.",
         #good practice to end with comma
         }
         ```
     - you can call a value like this:  
        ``` javascript
        print(programming_dictionary["Bug"])
        ```
     - You can add onto the dictionary like this:
        ``` javascript
        programming_dictionary["Loop"] = "The action of doing something over and over again."
        ```
     - wipe an existing dictionary:
       ``` javascript
          programming_dictionary = {}
       ```
     - edit an item in a dictionary:
       ``` javascript
        programming_dictionary["Bug"] = "A moth in your computer"
       ```
     - loop through a dictionary
       ``` javascript
       for key in programming_dictionary: 
            print(key) #prints the words of the dictionary (the key)
            print(programming_dictionary[key]) #prints the value of the key
       ```
- Nested Lists and Dictionaries: mix and match data types!
     - nesting a list in a dictionary:
       ```javascript
       travel_log = {
           "France": ["Paris", "Lille", "Dijon"]
       }
       ```
       - retrieve "Lille" like this:
       ``` javascript
       print(travel_log["France"][1])
       ```
     - nested_list:
       ``` javascript
       nested_list = ["A", "B", ["C", "D"]]
       ```
       - to get "D"
         ``` javascript
         print(nested_list[2][1])
         ```
     - Another example, to retrieve "Tokyo":
       ``` javascript
       travel_log1 = {
          "China": {
          "num_times_visited": 8,
          "cities_visited": ["Beijing", "Shanghai", "Chongqing"],
        },
           "Japan": {
           "num_times_visited": 3,
           "cities_visited": ["Osaka", "Kyoto", "Tokyo"],
        },
       }
       print(travel_log1["Japan"]["cities_visited"][2]) #tokyo
        ```
- Fuctions with Outputs: usually with return ()
   - difference between return(output) and print?
   - return statement = used to give back a value from a function, it replaces the part of the code where the function was called. Usually have to store it in a variable
     ``` javascript
     def format_name(f_name, l_name):
        formatted_f_name = f_name.title()
        formatted_l_name = l_name.title()
        return f"{formatted_f_name} {formatted_l_name}"
     formatted_string = format_name("adELine", "soV")  #can also straight up print this
     print(formatted_string)
     ```
   - you could have multiple return values:
     ``` javascript
     def canBuyAlcohol(age):
        if age >= 18:
          return True
        else:
          return False
     ```
   - or you can write return with out anything afterwards - tells the function to exit. 
- Docstrings:  to write multiline comments that document your code.
   - can use it just below the definition of a function and that text will be displayed when you hover over a function call.
   - syntax is """ abc """
   - e.g.:
     ``` javascript
     def my_function(num):
         """Multiplies a number by itself."""
         return num * num
    ```
       
