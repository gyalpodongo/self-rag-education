#lecture9

##SLIDES

###slide 0
LAMBDA FUNCTIONS, 
TUPLES and LISTS
(download slides and . pyfiles to follow along)
6.100L Lecture 9
Ana Bell

###slide 1
FROM LAST TIME
defapply(criteria,n):
""" 
* criteria: function that takes in a number and returns a bool* n: an int
Returns how many ints from 0 to n (inclusive) match the 
criteria (i.e. return True when run with criteria) """
count = 0foriinrange(n+1):
ifcriteria(i ):
count += 1
returncount
defis_even(x):returnx%2==0
print(apply(is_even,10))
6.100L Lecture 9

###slide 2
FROM LAST TIME
defapply(criteria,n):
""" 
* criteria: function that takes in a number and returns a bool* n: an int
Returns how many ints from 0 to n (inclusive) match the 
criteria (i.e. return True when run with criteria) """
count = 0foriinrange(n+1):
ifcriteria(i ):
count += 1
returncount
defis_even(x):returnx%2==0
print(apply(is_even,10))
6.100L Lecture 9

###slide 3
ANONYMOUS FUNCTIONS
Sometimes don’t want to name functions, especially simple 
ones. This function is a good example:
defis_even(x):
returnx%2==0
Can use an anonymous procedure by using lambda
lambda creates a procedure/function object, but simply does 
not bind a name to it
6.100L Lecture 9lambdax: x%2 == 0
parameterBody of lambda
Note no return keyword

###slide 4
ANONYMOUS FUNCTIONS
Function call with a named function:
Function call with an anonymous function as parameter:
lambda function is one -time use . It can’t be reused because it 
has no name!
6.100L Lecture 9apply( lambdax: x%2 == 0 , 10 )apply( is_even , 10 )

###slide 5
YOU TRY IT!
What does this print?
def do_twice(n, fn):
return fn(fn(n))
print(do_twice(3, lambda x: x**2))
6.100L Lecture 9

###slide 6
YOU TRY IT!
What does this print?
def do_twice(n, fn):
return fn(fn(n))
print(do_twice(3, lambda x: x**2))
6.100L Lecture 9Global environment
do_twice function object

###slide 7
YOU TRY IT!
do_twice environment
n 3
fnlambda x: x**2What does this print?
def do_twice(n, fn):
return fn(fn(n))
print(do_twice(3, lambda x: x**2))
6.100L Lecture 9Global environment
do_twice function object

###slide 8
YOU TRY IT!
What does this print?
def do_twice(n, fn):
return fn(fn(n))
print(do_twice(3, lambda x: x**2))
6.100L Lecture 9Global environment
do_twice function objectdo_twice environment
n 3
fnlambda x: x**2lambda x: x**2
environment
x ???

###slide 9
YOU TRY IT!
What does this print?
def do_twice(n, fn):
return fn(fn(n))
print(do_twice(3, lambda x: x**2))
6.100L Lecture 9Global environment
do_twice function objectdo_twice environment
n 3
fnlambda x: x**2lambda x: x**2
environment
x ???
lambda x: x**2
environment
x 3

###slide 10
YOU TRY IT!
What does this print?
def do_twice(n, fn):
return fn(fn(n))
print(do_twice(3, lambda x: x**2))
6.100L Lecture 9Global environment
do_twice function objectdo_twice environment
n 3
fnlambda x: x**2lambda x: x**2
environment
x ???
lambda x: x**2
environment
x 3Returns 999

###slide 11
YOU TRY IT!
What does this print?
def do_twice(n, fn):
return fn(fn(n))
print(do_twice(3, lambda x: x**2))
6.100L Lecture 9Global environment
do_twice function objectdo_twice environment
n 3
fnlambda x: x**2lambda x: x**2
environment
x 9
Returns 81981

###slide 12
YOU TRY IT!
What does this print?
def do_twice(n, fn):
return fn(fn(n))
print(do_twice(3, lambda x: x**2))
6.100L Lecture 9Global environment
do_twice function object
PRINTS 81do_twice environment
n 3
fnlambda x: x**2
Returns 8181

###slide 13
TUPLES
6.100L Lecture 9

###slide 14
A NEW DATA TYPE
Have seen scalar types: int,float,bool
Have seen one compound type: string
Want to introduce more general compound data types
Indexed sequences of elements, which could themselves be compound 
structures
Tuples –immutable 
Lists –mutable 
Next lecture, will explore ideas of
Mutability
Aliasing
Cloning
6.100L Lecture 9

###slide 15
TUPLES
Indexable ordered sequence of objects
Objects can be any type –int, string, tuple, tuple of tuples, …
Cannot change element values, immutable
te= ()
ts= (2,)
t = (2, " mit", 3)
t[0] evaluates to 2
(2,"mit",3) + (5,6) evaluates to a new tuple (2,"mit",3,5,6)
t[1:2] slice tuple, evaluates to ("mit",)
t[1:3] slice tuple, evaluates to ("mit",3)
len(t) evaluates to 3
max((3,5,0)) evaluates 5
t[1] = 4 gives error, can’t modify object
6.100L Lecture 9

###slide 16
INDICES AND SLICING
seq= (2,'a',4,(1,2))
print(len(seq)) 4
print(seq[3]) (1,2)
print(seq[-1]) (1,2)
print(seq[3][0]) 1
print(seq[4]) error
print(seq[1]) 'a'
print(seq[-2:] (4,(1,2))
print(seq[1:4:2] ('a',(1,2))
print(seq[:-1]) (2,'a',4)
print(seq[1:3]) ('a',4)
fore inseq: 2
print(e) a
4
(1,2)
6.100L Lecture 9index:    0      1      2        3

###slide 17
TUPLES
Conveniently used to swap variable values
x = 1           x = 1           x = 1
y = 2           y = 2           y = 2
x = y temp= x (x, y) = (y, x)
y = x x = y
y = temp
6.100L Lecture 9


###slide 18
TUPLES
Used to return more than one value from a function
defquotient_and_remainder(x, y):
q = x // y
r = x % yreturn(q, r)
both= quotient_and_remainder(10,3)
(quot, rem) = quotient_and_remainder(5,2)
6.100L Lecture 9


###slide 19
BIG  IDEA
Returning 
one object (a tuple) 
allows you to return multiple values
(tuple elements)
6.100L Lecture 9

###slide 20
YOU TRY IT!
Write a function that meets these specs:
Hint: remember how to check if a character is in a string? 
def char_counts(s):
""" s is a string of lowercase chars 
Return a tuple where the first element is the number of vowels in s and the second element 
is the number of consonants in s """
6.100L Lecture 9

###slide 21
VARIABLE NUMBER of 
ARGUMENTS
Python has some built- in functions that take variable number 
of arguments, e.g , min
Python allows a programmer to have same capability, 
using * notation
defmean(*args ):
tot = 0fora inargs: 
tot += a
returntot/len(args ) 
numbers is bound to a tuple of the supplied values
Example:
mean(1,2,3,4,5,6)
6.100L Lecture 9


###slide 22
LISTS
6.100L Lecture 9

###slide 23
LISTS
Indexable ordered sequence of objects
•Usually homogeneous (i.e., all integers, all strings, all lists)
•But can contain mixed types (not common)
Denoted by square brackets , []
Mutable , this means you can change values of specific 
elements of list
6.100L Lecture 9


###slide 24
INDICES and ORDERING
a_list= []
L = [2, 'a', 4, [1,2]]
[1,2]+[3,4] evaluates to [1,2,3,4] 
len(L) evaluates to 4
L[0] evaluates to 2
L[2]+1 evaluates to 5
L[3] evaluates to [1,2], another list!
L[4] gives an error 
i= 2
L[i-1] evaluates to 'a' since L[1]='a'
max([3,5,0]) evaluates 5 
6.100L Lecture 9

###slide 25
ITERATING OVER a LIST
6.100L Lecture 9Compute the sum of elements of a list
Common pattern
Function call list_sum2([8,3,5])
Loop variable itakes on values in the list in order! 8 then 3 then 5
To help you write code and debug, comment on what the loop var 
values are so you don’t get confused!deflist_sum1(L):
total = 0 foriinrange(len(L)): 
total += L[i ] 
return totaldeflist_sum2(L):total = 0 foriinL: 
total += i
return total
# iis 8 then 3 then 5

###slide 26
LISTS SUPPORT ITERATION
Because lists are ordered sequences of elements, they naturally 
interface with iterative functions
Add the elements of a list Add the length of elements of a list
6.100L Lecture 9deflist_sum(L):
total = 0 fore inL: 
total += e 
return(total)
list_sum([8,3,5]) 16deflen_sum(L):total = 0 fors inL: 
total += len(s) 
return(total)
len_sum([ 'ab', 'def', 'g']) 6


###slide 27
YOU TRY IT!
Write a function that meets these specs:
def sum_and_prod (L):
""" L is a list of numbers 
Return a tuple where the first value is the sum of all elements in L and the second value is the product of all elements in L """
6.100L Lecture 9

###slide 28
SUMMARY
Lambda functions are useful when you need a simple function 
once, and whose body can be written in one line
Tuples are indexable sequences of objects
Can’t change its elements, for ex. can’t add more objects to a tuple
Syntax is to use ()
Lists are indexable sequences of objects
Can change its elements. Will see this next time!
Syntax is to use []
Lists and tuples are very similar to strings in terms of 
Indexing, 
Slicing, 
Looping over elements
6.100L Lecture 9

##TRANSCRIPT

LAMBDA FUNCTIONS TUPLES and LISTS FROM LAST TIME ANONYMOUS FUNCTIONS Wha does this print? YOU TRY IT! A NEW DATA TYPE TUPLES INDICES AND SLICING ND SLICING VARIABLE NUMBER of ARGUMENTS LISTS INDICES and ORDERING ITERATING OVER a LIST LISTS SUPPORT ITERATION So today we're going to wrap up talking about functions by talking about these things called lambda functions as a way for us to create anonymous functions, and that'll pretty much finish our exploration into creating functions. And the last part of the lecture, we're going introduce new object types, tuples and lists. So let's. Remember what we did last time we ended with this example. We created a function. You guys wrote it for me, and then we kind of wrote it and debugged it together. But we created this function called Apply. So what was interesting about this function is that one of its parameters was R was a function and the other one was an integer. And that seemed a little strange at first, but not when we realized that functions in Python are actually just objects. And so they have a name, which means that anywhere where we use other kinds of objects, like integers, floats, we can use them as parameters to functions. We can use other functions as parameter parameters to functions as well. So here criteria, we had just used it as a variable name, assuming that the type of criteria is a function. According to this documentation, we assume that it takes in a number and returns a boolean. So we just wrote the body of the function, assuming that that is true. So right here is where we used this function named criteria. We assumed that it takes in an integer, so we passed in the loop variable ie as an integer and we assumed it returns a boolean. So we were able to use the return of criteria parentheses i just as a boolean inside my as my condition for this statement. Okay. So hopefully you got a chance to look through this example from last lecture. So that's the definition of this function that takes in another function as a parameter. And then the way we use the function is down here. So apply is us making our function call. And then the first parameter is the name of a function and the second parameters an integer. So the name of the function we're running is this object that we defined over here. Okay, hopefully this is just review. Now what's interesting about this example is that this is even function is pretty simple, right? It's it's basically a one liner. It doesn't do any computations inside the function body. It basically just takes in a value, an input and returns something. And so we didn't really need to create a function, a full fledged function definition, just to do this really simple task. And in fact, that's what a lambda function is. It's basically a way for us to create an anonymous function, a function that does something really simple, but we just don't give it a name. Okay. And so here is the function that we created with an actual definition up here. We can create an equivalent anonymous function that looks like this. So this is a much more concise way for us to create a really simple function that we only need to use one time. So here is I'm going to just map out sort of one by one, the important pieces of the lambda function. So the lambda keyword starts out the anonymous function, and it tells Python that we're creating this anonymous function. So Lambda is not the name of the function. It just tells Python we're going to create this function in one line that is nameless. X is going to be any parameters that we expect this function to take. So if we have more than one, we just separate them with commas. Colon is again the same, and then the body of the function, if you can write it in one liner, that's not too complicated. You can make a lambda function out of it. So here, notice we don't actually have a return keyword when we're creating the lambda function. We're just doing the operation that we wish to return the value from. Okay, so the x percent to equal zero is basically the body of my lambda function over here. Okay. So the key thing about lambda functions is that it allows you to create a really quick function object that you basically want to use only one time. And so we're not giving it a name. So let's look look at the code. So here is my apply function that we've seen before. Here is us. I showed you this last time. I created another definition for another simple function that takes in an integer and returns a boolean. In this case, this function just tells me whether that input is equal to five. And this is kind of where we left off last time we ran. Apply with this is five function. So that prints you know, apply with is five is one. There's only one integer between zero and ten where applying this returns true. Okay. Now with an anonymous function just to show you how we would write a lambda function for this is underscore five. It would look like this. So again we tell Python we're creating an anonymous function. It has just the one input x colon, no return and just the body of the function is going to be the thing that we would like to return x equal five. So again, this notice we're not actually passing in the name. There is no name for this anonymous function, but it works in the exact same way as if we had created this function over here. And just to sort of bring that out and I can run it again and you can see it apply with the function name is one right and obviously apply with this anonymous function also returns one. So just to bring the point home, I want to show you one other way to think of these anonymous functions. So here is me calling my is even function with a parameter eight. Now, in order for me to actually run it, run this line here, I had to have the function definition way up here. But again, it's a really simple function. If I only want to use it one time, I can create a lambda function. And this over here is equivalent to this function definition and function definition over here. So you can think of this line over here. So the part that I've highlighted as sort of creating the definition all in one line, not giving it a name. And then the parentheses here is us calling those lines of code for that function definition with that parameter eight. Okay. And so the usefulness of lambda functions is when you want to create these really quick functions that you don't want to reuse. Obviously, if we wanted to reuse this, the functionality of the is even. But we created it using a lambda function. We would have to basically copy this line and paste it all over again. Right. So we'd have to take this, copy it, paste it and give it another input. Okay. Because this lambda function does not actually create it in memory with a name. There's no way for us to access the body because it's it's nameless. Okay. So when we saw just to finish how we call lambda function. So basically when we called apply is even ten. The equivalent to calling that function name, but with a lambda function is basically putting in the entire body of the lambda function inside this other function call. Right. So here we're both defining and telling and then telling Python that this is my input to the function. Okay. So I know this is a you try it, but I thought that we would actually run through it together step by step in the next few slides. So let's try to understand what this is doing. I've got a function definition named do twice. It takes in one input, another input. But if we look at the body here, this F and that's the input is actually being called like a function inside the body. Right. So we can so we can immediately tell that f n is going to be a function when we actually make the call to do twice. And indeed, when we make the call to do twice down here and is mapped to three and the second parameter f n is mapped to this anonymous lambda function. Okay. So let's step through one little by little in the same manner that we learned last lecture. So creating actual environments whenever we see a function call mapping parameters, actual parameters to formal parameters and following through on what exactly happens within each function body. So when we first make the function call right or sorry, when we first run this program, if it has these sort of three lines of code inside it, Python creates our global environment. Inside the environment, we've got one function definition here. So this is going to be this function object. And then I've got the thing that actually kicks off my my, you know, my function calls my, my program. So I've got a print statement that will print the result of doing something. So the first thing I can see here is that I've got a function called to do twice. Right. So I'm going left or right. The first thing I can do and I have a function call is I create a new environment. Inside this environment of do twice. I have to see what it takes in. What are its formal parameters. There's one called NW and one called F, and so there's one parameter N and the other one F.N. And now I basically map one by one the parameter, the formal parameter to the actual parameter. So the N gets mapped to the three because that's the first parameter of do twice and the F and gets mapped to this function object here. Right. So the F end gets mapped to this lambda function here. Okay. That's exactly what I said. So we've done the mapping and now that we've done the mapping, we can do the body of do twice. So the body of do twice says return. And then I have to replace everywhere I see f n with this lambda function and everywhere I see n with this three. Well, FSN is going to be a function call, right? Whenever we see a function call, we need to create a function scope. So before I can do the return, before this do twice, can terminate, can return its value. It sees a function call. So when there's a function call, we need to create another scope. Right? Another environment. This environment belongs to the function call of lambda x colon x squared. Right now this function, of course doesn't have a name. Normally I would say, you know, this is the F environment or this is the G environment or the is even environment, but there's no name for this one. So I'm just going to write up here the body of that function. All right. Well, in this function, again, following sort of the rules one by one, what we need to do is figure out what are the parameters of this function. Well, there's one called X. So here's my parameter X and then I need to figure out what does this map to? Well, what it maps to is the parameter inside it. But the parameter inside it is f and parentheses end. Do we have a return value for this yet? No. Right, because this is another function call. So what ends up happening is this environment gets put on hold as well because we can't figure out what parameter this lambda function takes it, what is its value. So we create another scope. Another environment. And in this particular case, this one is going to belong to this. This inside bit here, if in parentheses at. So this lambda x x squared is going to be the exact same function again being called again. And in this particular environment, we need to map X to its input. So the input to x sorry to this lambda x x squared is going to be n well, this environment doesn't know about n, so we pop up one level this environment knows about and it's three. So it passes that value along down to this lambda lambda. So now that this inner sort of highlight yellow over here knows what it needs to do, it needs to take in this X and return X squared. So calculates nine and then returns nine to whoever called it. That nine gets replaced now as the input to this outer effort. Okay. So just to show you exactly what gets replaced, that entire function called there gets replaced with nine. All right. As soon as we've done the return, that environment goes away. And at this point, this call to Lambda X X squared can terminate as well, because it takes in the number nine and it returns nine squared. So this one returns 81. So this entire function call is 81. And as soon as it returns, that environment goes away. And now do twice can finally finish its job and return 81. It just basically passes this value along back up so that returns 81. So this entire do twice call is going to be 81. Why were your points land that way? Why would you choose? Oh, there were two of them. Because this outer end calls an inner AFN. So we. Yeah, okay. Okay. So that wraps up our discussion on functions. And there's a couple exercises in this. The Python file associated with this lecture with lambda functions just so you can give it a try with those. Yeah, well, apply was just a function that I wrote. So in this particular in this new example, I was just printing the result of calling that function. Yeah. So again, this kind of trace of what happens throughout the program is really, really useful. So if you can you know, if you have some time to to try to get that down, it will be very, very helpful as you trace through some programs. Okay. So that ends our discussion on functions. And really the only syntax we've introduced in the past couple of lectures were just about how to wrap code we've already been using in a function, right? So not much new syntax, but today we're going to introduce some new syntax along with the introduction of two new data types. One is called a tuple and the other one is called a list. So what are the data types we've seen so far? We've seen integers, floats, basically numbers. We've seen booleans as truth values. We've seen this non type type, which has one value none. And we actually also saw the string data type, right? We could think of the string data type as sort of a compound data type, like a sequence of single characters. And in fact, we were using that string in that way because we were able to index into the string to grab the character at index zero, sort of slice the substring, right to get the length of the string. Today we're going to introduce two more compound data types. So these things called tuples and these things called lists. And throughout the lecture, you should really think about how it's very, very similar to the strings, the strings that we see we've already seen. So a lot of the operations I'm actually going to skip, aside from sort of the syntax of how we denote a tuple or a list, really, the operations that we do with tuples and lists are going to be exactly the same as the ones that we did with strings, right? So if you understand indexing and slicing and getting the length of the string, all that stuff, you'll understand how to do that for tuples and lists. All right, so tuples are index index.html ordered sequences of objects. That's kind of a lot. So we can break that down. So first of all, it's a sequence of objects, just like a string was a sequence of single characters. A tuple is going to be a sequence of not just characters, but any kind of object. Ordered sequence means that there will be an order to this sequence. So there's going to be an object at the first position in my tuple, an object at the second position in my tuple and so on. Just like there was a character at the first position character, the second position and so on. And index double ordered sequence means that we can index into this object so we can grab the element at index zero, grab the element X one and so on and so on. So how do we create these tools? I should note that some people call them tuples because they're just kind of like an end tuple kind of thing. So you can call them tuples or tuples however you'd like. All right. So how do we create these these these tuple objects? Well, we can create a tuple object that's empty using just open and close parentheses. So we could create strings using just sort of the open and close quotation marks. We create an empty tuple by doing open and close parentheses. Now, this is different than functions, right? We this is a little bit similar or might be bit confusing because we use parentheses to make function calls. But notice it's just the parentheses by themselves, right? There's no function name, nothing preceding the parentheses. So to Python, it's not going to be confusing when you just do this. You can create a tuple with one element in it by putting open close parentheses that element that you want to add to your tuple and then a comma right after it. Now the commies there to. Differentiate a tuple with one element from sort of using parentheses as precedence over an operation. So just as an example, if I create a is equal to five like this, right? I'm using parentheses around an integer, but the type of a is still an integer. I'm basically just using the parentheses to say I want to do this five before doing anything else. Which is a little strange to do. And right the value of a is five. But if I do B is equal to the tuple for comma. This tells Python that this is now a sequence of objects, but there's just one object in my sequence. So the type of B is a tuple, not an integer. Right? And if I say ask what beers you can see it's it's four comma, right in parentheses. So it's an object. It's a tuple with one object in it. Okay. So to create a tuple with many objects in it, we basically put in parentheses all the objects I want to add in my tuple separated by commas. So here I've got my first element in my tuple integer to second element in the tuple the string of my t and the third element in my tuple being the integer three. And notice we can mix and match now objects of different types within my tuple object. So here I've got integers and strings and in integers I can even add floats and booleans and whatever object types I'd like. I can make them elements to my tuple, which is pretty cool. Right? Different than strings in that respect. But still, you know. In in. In order within my tuple. And so the rest of this is actually operations that we've already seen on strings. So I'm not going to go through them in too much detail. We can use the square bracket to index into the two balls or to grab the element at a particular index. Again, indexing starts from zero. We can use the plus operator to concatenate two tuples together to create one larger tuple with all those elements in a row. We can slice down here, we can get the length of the tuple which tells us how many elements are in it. So three elements we can use the max min, some things like that to grab the maximum element and minimum element sum all the elements of my tuple and things like that. Notice that here I've got parentheses for the max function call and then another set of parentheses here to denote that I have one tuple object. I'd like to grab the max. And then the last bit here is something that we're going to see that's different with lists in the in next lecture. Not today, but basically you might think that once you create this tuple object in memory, right, that has to omit three as it's three elements in it. You can go into memory and modify one of the elements. Right. Like if I don't want the middle one to be a string, I want it to be a common integer. You might think that you should be able to change it. You can with lists as we'll see in the next lecture. But you cannot do this with tuples. Just like once we created sort of an integer five inside memory. We can't go into memory and tell Python to change this five to a six. It's just not allowed. Or once we created a string ABC memory, you can't go into memory and change the string. You can certainly create new objects that are based on this string, but you can't go in and modify that object once it's created. So once you've made your sequence of tuples, you cannot go in and change it. So yeah. Question So like you just rewrote like t equals and I thought the difference it would be here if you wrote t equals and then something different so you can't laugh at one thing. Yeah, that's a good question. So. So the variable T, so the name T and the object it's bound to are two different things. So the object it's bound to will still sit in memory. We're just going to lose the binding from it. So that t initially points to this one. But then if you say T equals something else later on, this one still stays there, but that t is going to point to this new thing. So the object itself is still in memory. We've just lost the binding to it. And that's something we did sort of way back in the first early lectures where we kind of rebound variables. Yeah. So it's the same. Yeah, it's the same idea. One interesting thing that we can do now with tuples that we couldn't with strings. Is to have elements of a tuple, be another tuple. Okay. And that's what this example is going to showcase. So here I've got an integer two as my first element. My second element is the string a, my third element is my integer four, and my fourth element is a tuple object that just happens to have two elements inside it. But this tuple object that I'm referencing by a C q seek only has four elements in it. It just so happens that the last one is a tuple, but that I'm not going to dive further down to figure out if I have tuples that have sub tuples that have sub tables and so on. Only top level. I care about how many elements I have. And so when I print the length of its it's going to be four, right? Because I have one, two, three, and then this last object is just one object that takes up one slot. It happens to have elements with up within it. And so the rest of these are basically what we've seen with strings, except for this one here. If we were to index into the last element here of C one, comma two. Well this is another tuple, right. So it should follow that I can then take that tuple and further index into it. And so that's what this line here is doing when when we read an expression, we go left to right. So basically seek at index three grabs for me the one comma two and then if I further index into one comma two at index zero, I'm going to grab the the number one. All right. So I'm basically chaining all these indices, indexing operations together. And then this is again, very similar to what we've seen from strings. So it's just slicing instead of indexing into the into the tuple. I'm not going to go through it today, but I encourage you to type them in and type in some other things as you might have done with the strings. One thing that I do want to mention is that we can iterate over a tuple just like we could iterate over a string. I don't mean over indices, but I mean over the elements directly. So when we iterate it over a string directly, we were able to grab in our loop variable the characters at each index. Right. Similarly, we can iterate over a two port to grab the elements at each index directly. So here I've got four e in sync is going to make my loop variable e take on each element of the tuple directly. Not the index, but each element. So as I'm looping through, each will first have a value too, then it'll have a value a, then it'll have a value for. And lastly, it'll have this value one, comma two. And so if I just print that out directly, you'll see these values printed out. So very, very similar to some of the operations we've done with strings. The only difference is we just now have to be careful that our tuples can have elements that are other tuples or basically any object in Python. So what do we use to pose for? Well, there was this one example we did way back at the beginning of of this of six 100 ele where we tried to swap variables and we basically said that this way. Did it work because we overrode the variable, right? We overrode the variable and then we were able to get back to the value that was over it. So our solution was to create this temporary variable to save the value before we overrode it, then overwrite the variable, and then use the temporary variable to grab back that saved value. Well, it turns out two polls actually allow us to do these three lines of code in one line of code here. So we can say x, comma y equals y, comma x. So this is an assignment. And it's allowed because the left hand side is basically a set of variables. It's in sequence and the right hand side gets evaluated first, as we would an assignment statement. So y gets the value too, because that's what it is up here and x gets the value one. So Y is two, x is one over here on the right hand side and then Python one at a time matches the values on the right to the values on the left right, separated by commas. So basically what we have here is X is equal to two, Y is equal to one. And then the values have been rebound. So very, very, very useful, very good use of tuples here. Now this idea can actually be taken one step further and we can use tuples to return more than one value from a function. Now I know in the past couple lectures I said basically, you can't return more than one thing from a function. The function returns only one thing as soon as it sees a return statement. It takes the value associated with that return and returns it back to whoever called it. But tuples are one object. They just so happen to have elements that can have different values. Right? You can have a tuple with ten elements in it. You can have a tuple with two elements in it. Using a tuple we can actually return one object the tuple itself. It just so happens to have a whole bunch of values that my function might calculate. Right? And so by way of the tuple, I'm actually able to return a whole bunch of different values through this one object tuple. And so in this particular example, I have a function that calculates the quotient and the remainder when X is divided by Y. Uh. Yeah. So the function itself takes in the uses integer division to find the quotient and uses the remainder operator to find the remainder. And then it returns that Q calculation. Right some number and that our calculation another number as elements to a tuple and python returns this one tuple object using using this this line here returning this object. And so when I make this function call to quotient and remainder ten comma three, it's going to go in, it's going to calculate the quotient to be three, the remainder to be one, and it's going to return one, object three, comma one. And then that gets assigned to this variable, both that I named, both in this particular case. If I wanted to access the quotient part of both, I would do both square brackets zero and the remainder part of both would be both square bracket one. Right accessing the zeroth element and the first element of the return. Now if I wanted to explicitly save the quotient and remainder as variables after they got returned, I can actually do the trick we saw on the previous slide. Right. The trick we saw in the previous slide was X come alive equals some other tuple. Well, that's what I'm doing here. I'm making a function called the quotient remainder five, comma two. That's going to return to common one. And then I'm going to have, quote, karma rum equals two comma one. So Python one, one at a time is going to map the quote to two and the REM to one. And so what that means for us in terms of the code is we can then do whatever we'd like in the remaining part of the code code, assuming that quote and REM are just regular variables. So here I'm just showing that you can print them out in these print statements. Right. So here I have quotient is two and remainder is one as these two lines of code here. Okay. So the big idea of tuples is the reason why we use them is you can use you can use them to return more than one value via this one tuple object from a function. And so in this way we can have a function that does a whole bunch of calculations, returns this one object that might contain all of these different values as the elements to this tuple object. So let's have you work on this for a couple of minutes. Right. A function that meets the specification. So I've got it's called char counts, I've got an input that is a string s lowercase characters assume it's just got vowels and consonants return for me a tuple where the first element in the tuple is how many vowels are in s and the second element of the tuple is how many consonants are in this, right? So it should be pretty straightforward. A hint I have here, if you don't remember that will make your life easier, is try to remember how to check if a character is in a string. So using the special in keyword, right? We saw an example of this probably back when we learned about strings. So you can try to write your code around 965 ish and then we can write it together. All right. So how would you approach this problem? So what's the first step here? Yeah. Yep. We can make a string that contains all the vowels. Vowels equals i0u and lowercase. Yep. Vice. Next. Yeah. Yeah. Um, cars in that list. Then we could have been traveling. Yep. Yep. Vowels plus equals one. And else we know it's not a vowel. So we'll keep consonants count plus equals one. So this is the consonant count and this is the vowels count. What is char in this case, though? Yeah, exactly. We have to loop. So for char and S. So we need to look at every character inside us. And this is where now that we're dealing with, you know, things that that are just that might be non integers in my four loops we can write little notes for ourselves. That's something like char is, you know, A, then B, then C or something like that to remind us that char is not sort of the index, but it's an actual thing. And then what? Else we need to do. Yeah. We can initiate zero. We can use the trick where you do see karma equals zero zero or we can just do it on separate lines. Oh, good. And then lastly, this does the work for us. But the function needs to have something to show for it. Yeah. After the loop, we'll return. The tuple c copy. Oh, sorry. We can't see properly. And if we run it. It matches what we expected. So one, three and zero five. And you can imagine adding a couple more test cases, maybe something with an empty string that should return zero zero and maybe something with all vowels which should return some number, comma zero. Okay. So one other thing we can do with with tuples is to create these functions that take a variable number of arguments is in as a parameter. So remember when we define functions, we basically tell Python how many parameter we expect it to take. Right. But it's possible to have some functions, for example, Max or min, that can take in two parameters here and notice there's no extra parentheses. Or we can just add as many numbers as we'd like. And it will still work to take the max of all of these sets of numbers. And again, we didn't make this inner thing a tuple, although it works even with the tuple as an object. But our goal here is to try to write a function that can take in a variable number of arguments. Right? Either two or three or ten or 20, and it should still work. And the way we do that is using a parameter that's defined using the star notation. So as soon as you create a function and its parameter is star and then the name of your input, Python basically takes that input and assigns it to a tuple behind the scenes so you don't have to. Okay. And so in this particular case, we're not use not writing our own max or min or some we're writing our own mean function. And this main function will take in a variable number of arguments. Right? And it's going to figure out the mean of all of these values the way it does. That is pretty simple. Now that we know that we can just treat args as a tuple of a bunch of numbers. So we just loop through all of the elements in args, we add up this running total. And at the end we return the total divided by how many arguments were given. So return total divided by the length of the arcs. And then when we make a function call to the function, we just row mean here args will take in. Sorry, args will become a tuple. That's all of the parameters inside there. And so here is that example, which means that we can use our function to get the mean of one, two, three, four, five, six. But we can use the exact same function to get the mean of 609, for example. So first case, I have six parameters as my input, but in the second case I've got only three parameters as my input. And that little star in my arguments, it allows me to to do this. Now I did write a version of this mean for you guys down here where I'm assuming that mean doesn't have the doesn't have the star. So assuming that ARGs is a tuple itself and in that case you would have to call the mean function by explicitly passing in only one argument that is a tuple. So this extra set of parentheses makes my argument the tuple. So you want to take a closer look at that if you're interested. So I want to introduce lists today and a lot of the slides here are basically copy and paste from the tuple slides. The only difference in these slides that I have regarding lists is the way we define a list. So in terms of defining a list or defining a tuple, we were using parentheses. But to define a list we use open, close, square brackets. But otherwise a lot of the operations are exactly the same as little as tuples and as strings. We're not going to look at what it means for two for lists to be mutable. This lecture. But next lecture will be all about mutability. Okay. But today, I just want to give you a sense of what a list is. So as I said, this is copy and paste from the tuple slide. When I create a list I just use open and close brackets. This creates a list for me with no elements within it, creating a list with one element. And it doesn't need that extra comma because there's no confusion with Operation Precedence with square brackets, right? So there's no need for that. But otherwise everything else here is exactly the same as with tuples. We're just using square brackets instead of parentheses. Okay, so remember strings and tuples. It's the same. What I do want to mention and talk a little bit about now that we've introduced to polls and lists, is the idea of having our loops iterate over elements of tuples and lists directly. And I'm going to basically write these slides in the context of lists, but the exact same thing is applicable to tuples as well. So. Here is an example of us wanting to find the sum of the elements in the list. The coat on the left is a little bit hard to pass, right. We've got a loop variable going through range length and and then I have to keep my running total, but I have to index into the list at that index here. And it's really hard to tell what's going on at a quick glance. And so luckily for us, right the way that we were able to iterate over string characters directly, we can iterate over tuple and list elements directly. So the right hand side here is exactly. This is code that does exactly the same thing as the one on the left, except that our loop variable I in this particular case will take on the values of my list directly. Okay. And so if we take that code. Yes. And I guess we call this version more python because it's a lot easier to read. So if we take that code and wrap it around the function to make this piece of code be something that we can reuse in a whole bunch of places to grab the sum of all the elements of a list. Right. We can do that. So here I've taken the code that does the work. I've plopped it inside this function. I've named list some. I've taken a list as a parameter and instead of printing the total, I'm returning the total. Right. So very useful function now. This loop variable, I will take on the values eight than three than five if that's the list I called this function with. Right. So a lot nicer than iterate iterating over the index and then indexing into the list with the square brackets at that index. What I do want to mention is something sort of when you're writing code and this is something that I sort of used to do when I first started out, is to write a little comment for yourself right underneath the for loop. Now, I know it's it's a little tedious, but it does help you keep track of especially if you're now that we're iterating over tuples or over lists, over string elements directly or even over the indices. It helps you keep track of what this loop variable is. Value is going to be right, and then you don't have to keep track of it in your mind. It's on paper and you can use your mind to keep track of other things. So if you just write a little comment for yourself there, it helps you debug along the way. So once we have these, once we iterate over list elements directly, it makes code that we write really easy to read. So here the code on the left is going to iterate over the elements directly and get the running total. But we can make a really small change to the input list. Let's say our input list no longer takes in just numbers, but it can take in strings. We can make one small change to our loop, to our loop body. Our loop variable still iterates over all the elements in the list. L And then if we write the note for ourselves, that. S is going to be a B, then def, then g. If we wanted to write code that grabbed the sum of all of the lengths of the list. The total plus equals E on the left hand side becomes total plus equal length of S on the right hand side. So length of x one at a time will take on the value two because AB has length two and then three because DF has length three and then one because G has length one. Right. So the code looks very similar, but they have different functionalities depending on what we want to do. Okay. We don't have time to go through this. You try it, but definitely try it on your own at home. It's very useful. Plus a whole bunch of other functions that I've put in this python file for you to get a lot of experience with tuples. Endless. Okay. 
