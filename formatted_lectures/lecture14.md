#lecture14

##SLIDES

###slide 0
DICTIONARIES
(download slides and . pyfiles to follow along)
6.100L Lecture 14
Ana Bell

###slide 1
HOW TO STORE 
STUDENT INFO
Suppose we want to store and use grade information for 
a set of students
Could store using separate lists for each kind of information
names =  ['Ana', 'John', 'Matt', 'Katy']
grades = ['A+' ,  'B'  ,   'A' ,   'A' ]microquizzes = ...
psets= ...
Info stored across lists at same index , each index refers to 
information for a different person
Indirectly access information by finding location in lists 
corresponding to a person, then extract
6.100L Lecture 14


###slide 2
HOW TO ACCESS 
STUDENT INFO
defget_grade(student, name_list, grade_list):
i= name_list.index (student)
grade = grade_list[ i]
return(student, grade)
Messy if have a lot of different info of which to keep track, 
e.g., a separate list for microquiz scores, for pset scores, etc.
Must maintain many lists and pass them as arguments
Must always index using integers
Must remember to change multiple lists, when adding or 
updating information
6.100L Lecture 14


###slide 3
HOW TO STORE AND 
ACCESS STUDENT INFO
Alternative might be to use a list of lists
eric = ['eric', [' ps', [8, 4, 5]], [ 'mq', [6, 7]]]
ana = ['ana', [' ps', [10, 10, 10]], [' mq', [9, 10]]]
john = ['john', [' ps', [7, 6, 5]], [' mq', [8, 5]]]
grades = [eric, ana, john]
Then could access by searching lists, but code is still messy
defget_grades(who, what, data):
forstud indata:
ifstud[0] == who:
forinfo instud[1:]:
ifinfo[0] == what:
returnwho, info
print(get_grades( 'eric', 'mq', grades))
print(get_grades( 'ana', 'ps', grades))
6.100L Lecture 14


###slide 4
A BETTER AND CLEANER WAY –
A DICTIONARY
Nice to use one data structure , no separate lists
Nice to index item of interest directly
A Python dictionary has entries that map a key:value
A list A dictionary
Elem 1
Elem 2
Elem 3
Elem 4
…Key 1
Key 2
Key 3
Key 4
…Val 1
Val 2
Val 3
Val 4
…0
1
2
3
…
6.100L Lecture 14

###slide 5
BIG  IDEA
Dict value refers to the 
value associated with a 
key. 
This terminology is may sometimes be confused with the regular value of some variable. 
6.100L Lecture 14

###slide 6
A PYTHON DICTIONARY
Store pairs of data as an entry
•key (any immutable object)
•str, int, float, bool, tuple, etc
•value (any data object)
•Any above plus lists and other dicts !
my_dict = {}
d = {4:16}
grades = {'Ana':'B', 'Matt':'A ', 'John':'B', ' Katy':'A '}Key 1
Key 2
Key 3
…Val 1
Val 2
Val 3
…
key1    val1
6.100L Lecture 14key2      val2 key3     val3 key4      val4'Ana'
'Matt'
'John'
'Katy''B'
'A'
'B'
'A'

###slide 7
DICTIONARY LOOKUP
Similar to indexing into a list
Looks up the key
Returns the value associated with 
the key
If key isn’t found, get an error
There is no simple expression to 
get a key back given some value !
6.100L Lecture 14grades = {'Ana':'B', 'Matt':'A ', 'John':'B', ' Katy':'A '}
grades['John'] evaluates to 'B'
grades['Grace'] gives a KeyErrorKey 1
Key 2
Key 3
…Val 1
Val 2
Val 3
…'Ana'
'Matt'
'John'
'Katy''B'
'A'
'B'
'A'Key 
'John'
Value associated with key 'John'

###slide 8
YOU TRY IT!
Write a function according to this spec
def find_grades(grades, students):
""" grades is a dictmapping student names (str) to grades (str)
students is a list of student names 
Returns a list containing the grades for students (in same order) """
# for example
d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
print(find_grades (d, ['Matt', 'Katy'])) # returns ['C', 'A']
6.100L Lecture 14

###slide 9
BIG  IDEA
Getting a dict value is 
just a matter of indexing 
with a key.
No. Need. To. Loop
6.100L Lecture 14

###slide 10
DICTIONARY 
OPERATIONS
grades = {'Ana':'B', 'Matt':'A ', 'John':'B', ' Katy':'A '}
Add an entry
grades['Grace'] = 'A' 
Change entry
grades['Grace'] = 'C' 
Delete entry
del(grades['Ana'])
6.100L Lecture 14'Grace' 'A''Ana'
'Matt'
'John'
'Katy''B'
'A'
'B'
'A'
'C'

###slide 11
DICTIONARY 
OPERATIONS
grades = {'Ana':'B', 'Matt':'A ', 'John':'B', ' Katy':'A '}
Test if key in dictionary
'John' ingrades returnsTrue
'Daniel' ingrades returnsFalse
'B' ingrades returnsFalse
6.100L Lecture 14'Ana'
'Matt'
'John'
'Katy''B'
'A'
'B'
'A'

###slide 12
YOU TRY IT!
Write a function according to these specs
def find_in_L( Ld, k):
""" Ldis a list of dicts
k is an int
Returns True if k is a key in any dicts of Ldand False otherwise """
# for example
d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}
print(find_in_L([d1, d2, d3], 2)  # returns True
print(find_in_L([d1, d2, d3], 25)  # returns False
6.100L Lecture 14

###slide 13
DICTIONARY 
OPERATIONS
Can iterate over dictionaries but 
assume there is no guaranteed order
grades = {'Ana':'B', 'Matt':'A ', 'John':'B', ' Katy':'A '}
Get an iterable that acts like a tuple of all keys
grades.keys()   returns dict_keys(['Ana', 'Matt', 'John', 'Katy'])
list(grades.keys()) returns ['Ana', 'Matt', 'John', 'Katy']
Get an iterable that acts like a tuple of all dict values 
grades.values() returns dict_values(['B', 'A', 'B', 'A'])
list(grades.values()) returns ['B', 'A', 'B', 'A']
6.100L Lecture 14'Ana'
'Matt'
'John'
'Katy''B'
'A'
'B'
'A'

###slide 14
DICTIONARY OPERATIONS
most useful way to iterate over 
dict entries (both keys and vals!)
Can iterate over dictionaries but
assume there is no guaranteed order
grades = {'Ana':'B', 'Matt':'A ', 'John':'B', ' Katy':'A '}
Get an iterable that acts like a tuple of all items
grades.items() 
returns dict_items([('Ana', 'B'), ('Matt', 'A'), ('John', 'B'), ('Katy', 'A')])
list(grades.items ())
returns [('Ana', 'B'), ('Matt', 'A'), ('John', 'B'), ('Katy', 'A')]
Typical use is to iterate over key,value tuple
fork,vingrades.items():
print(f"key{k} has value {v}")
6.100L Lecture 14'Ana'
'Matt'
'John'
'Katy''B'
'A'
'B'
'A'

###slide 15
YOU TRY IT!
Write a function that meets this spec
def count_matches(d):
""" d is a dict
Returns how many entries in d have the key equal to its value """
# for exampled = {1:2, 3:4, 5:6}
print(count_matches(d))   # prints 0
d = {1:2, 'a':'a', 5:5}
print(count_matches(d))   # prints 2
6.100L Lecture 14

###slide 16
DICTIONARY KEYS & VALUES
Dictionaries are mutable objects (aliasing/cloning rules apply)
Use = sign to make an alias
Use d.copy () to make a copy
Assume there is no order to keys or values!
Dict values 
•Any type (immutable and mutable )
•Dictionary values can be lists, even other dictionaries!
•Can be duplicates
Keys
•Must be unique 
•Immutable type (int, float, string, tuple,bool)
•Actually need an object that is hashable , but think of as immutable as all 
immutable types are hashable
•Be careful using float type as a key
6.100L Lecture 14


###slide 17
WHY IMMUTABLE/HASHABLE 
KEYS?
A dictionary is stored in memory in a special way
Next slides show an example
Step 1: A function is run on the dict key 
The function maps any object to an int
E.g. map “a” to 1, “b” to 2, etc , so “ab” could map to 3
The int corresponds to a position in a block of memory addresses
Step 2: At that memory address, store the dict value
To do a lookup using a key, run the same function
If the object is immutable/ hashable then you get the same int back
If the object is changed then the function gives back a different int!
6.100L Lecture 14


###slide 18
A n a
E r ic
J o h nC
A
B1 + 14 + 1 = 16
16%16 = 0
5 + 18 + 9 + 3 = 3535%16 = 3
10 + 15 + 8 + 14 = 4747%16 = 15Memory block (like a list)
0
1
2
3Ana:C
Eric:A
John :B
6.100L Lecture 14Hash function:
1) Sum the letters
2) Take mod 16 (to fit in a memory block with 16 entries)
4
5
6
7
8
9
10
11
12
13
14
15[K, a, t, e] B11 + 1 + 20 + 5 = 37
37%16 = 5[K,a,t,e ]:B

###slide 19
Memory block (like a list)
0
1
2
3Ana:C
Eric:A
6.100L Lecture 14Hash function:
1) Sum the letters
2) Take mod 16 (to fit in a memory block with 16 entries)
Kate changes her name to Cate. Same 
person, different name. Look up her 
grade?
4
5
6
7
8
9
10
11
12
13
14
15[C, a, t, e]3 + 1 + 20 + 5 = 29
29%16 = 13[K,a,t,e ]:B
??? Not here!
John :B


###slide 20
Key 2 Val 2A PYTHON DICTIONARY for 
STUDENT GRADES
Separate students are 
separate dict entries
Entries are separated using a commaKey 1 Val 1
6.100L Lecture 14grades = { 'Ana':{'mq':[5,4,4], ' ps': [10,9,9], 'fin': 'B'},
'Bob':{'mq':[6,7,8], ' ps': [8,9,10], 'fin': 'A'}}

###slide 21
Key 2 Val 2 'Bob' 'mq'[6,7,8]
'ps'[8,9,10]
'fin''A'A PYTHON DICTIONARY for 
STUDENT GRADES
Each dict entry maps a key 
to a value
The mapping is done with 
a : character
grades maps str:dictKey 1 Val 1
6.100L Lecture 14'Ana'
grades = { 'Ana':{'mq':[5,4,4], ' ps': [10,9,9], 'fin': 'B'},
'Bob':{'mq':[6,7,8], ' ps': [8,9,10], 'fin': 'A'}}'mq'[5,4,4]
'ps'[10,9,9]
'fin''B'

###slide 22
Key 1 Val 1 'Bob' 'mq'[6,7,8]
'ps'[8,9,10]
'fin''A'A PYTHON DICTIONARY for 
STUDENT GRADES
The values of grades are 
dicts
Each value maps a 
str:list
str:strKey 1 Val 1
6.100L Lecture 14'Ana'
grades = { 'Ana':{'mq':[5,4,4], ' ps': [10,9,9], 'fin': 'B'},
'Bob':{'mq':[6,7,8], ' ps': [8,9,10], 'fin': 'A'}}'mq'[5,4,4]
'ps'[10,9,9]
'fin''B'

###slide 23
Key 1 Val 1 'Bob' 'mq'[6,7,8]
'ps'[8,9,10]
'fin''A'A PYTHON DICTIONARY for 
STUDENT GRADES
The values of grades are 
dicts
Each value maps a 
str:list
str:strKey 1
6.100L Lecture 14'Ana'
grades = { 'Ana':{'mq':[5,4,4], ' ps': [10,9,9], 'fin': 'B'},
'Bob':{'mq':[6,7,8], ' ps': [8,9,10], 'fin': 'A'}}'mq'[5,4,4]
'ps'[10,9,9]
'fin''B'
grades['Ana' ]['mq'][0] returns5

###slide 24
YOU TRY IT!
my_d={'Ana':{'mq':[10], 'ps':[10,10]}, 
'Bob':{'ps':[7,8], 'mq':[8]},
'Eric':{' mq':[3], 'ps':[0]}      }
defget_average(data, what):
all_data = []
forstud indata.keys():
INSERT LINE HERE
returnsum(all_data)/ len(all_data)
6.100L Lecture 14Given the dictmy_d, and the outline of a function to compute an average, which line should 
be inserted where indicated so that get_average( my_d, 'mq') computes average 
for all ' mq' entries? i.e. find average of all mqscores for all students.
A)all_data = all_data + data[stud][what]
B)all_data.append(data[stud][what])
C)all_data = all_data + data[stud[what]]
D)all_data.append(data[stud[what]])

###slide 25
list vs dict
6.100L Lecture 14Ordered sequence of 
elements
Look up elements by an 
integer index
Indices have an order
Index is an integer
Value can be any typeMatches “keys” to 
“values”
Look up one item by 
another item
No order is guaranteed
Key can be any 
immutable type
Value can be any type

###slide 26
EXAMPLE: FIND MOST COMMON 
WORDS IN A SONG’S LYRICS
1) Create a frequency dictionary mapping str:int
2) Find word that occurs most often and how many times
•Use a list, in case more than one word with same number
•Return a tuple (list,int) for (words_list , highest_freq )
3) Find the words that occur at least X times
•Let user choose “at least X times”, so allow as parameter
•Return a list of tuples, each tuple is a (list, int) containing the 
list of words ordered by their frequency
•IDEA: From song dictionary, find most frequent word. Delete most 
common word. Repeat. It works because you are mutating the song 
dictionary.
6.100L Lecture 14


###slide 27
CREATING A DICTIONARY
Python Tutor LINK
song = "RAH RAHAH AHAHROM MAH RO MAH MAH"
defgenerate_word_dict(song):
song_words = song.lower()
words_list = song_words.split ()
word_dict = {}
forw inwords_list :
ifw inword_dict:
word_dict [w] += 1
else:
word_dict [w] = 1
returnword_dict
6.100L Lecture 14

###slide 28
USING THE DICTIONARY
Python Tutor LINK
word_dict = {'rah':2, 'ah':3, 'rom':1, 'mah':3, 'ro':1}
deffind_frequent_word( word_dict):
words = []
highest = max(word_dict.values ())
fork,vinword_dict.items ():
ifv == highest:
words.append(k)
return(words, highest)
6.100L Lecture 14

###slide 29
FIND WORDS WITH FREQUENCY 
GREATER THAN x=1
Repeat the next few steps as long as the highest frequency is 
greater than x 
Find highest frequency
6.100L Lecture 14word_dict = {'rah':2, 'ah':3, 'rom':1, 'mah':3, 'ro':1}


###slide 30
FIND WORDS WITH FREQUENCY 
GREATER THAN x=1
Use function find_frequent_word to get words with the 
biggest frequency
6.100L Lecture 14word_dict = {'rah':2, 'ah':3, 'rom':1, 'mah':3, 'ro':1}


###slide 31
FIND WORDS WITH FREQUENCY 
GREATER THAN x=1
Remove the entries corresponding to these words from 
dictionary by mutation
Save them in the result
6.100L Lecture 14word_dict = {'rah':2,         'rom':1,          'ro':1}
freq_list = [(['ah',' mah'],3)]


###slide 32
FIND WORDS WITH FREQUENCY 
GREATER THAN x=1
Find highest frequency in the mutated dict
The result so far…
6.100L Lecture 14word_dict = {'rah':2,         'rom':1,          'ro':1}
freq_list = [(['ah',' mah'],3)]


###slide 33
FIND WORDS WITH FREQUENCY 
GREATER THAN x=1
Use function find_frequent_word to get words with that 
frequency
The result so far…
6.100L Lecture 14word_dict = {'rah':2,         'rom':1,          'ro':1}
freq_list = [(['ah',' mah'],3)]


###slide 34
FIND WORDS WITH FREQUENCY 
GREATER THAN x=1
Remove the entries corresponding to these words from 
dictionary by mutation
Add them to the result so far
6.100L Lecture 14word_dict = {                 'rom':1,          'ro':1}
freq_list = [(['ah',' mah'],3), (['rah'],2)]


###slide 35
FIND WORDS WITH FREQUENCY 
GREATER THAN x=1
The highest frequency is now smaller than x=2, so stop
The final result
6.100L Lecture 14word_dict = {                 'rom':1,          'ro':1}
freq_list = [(['ah',' mah'],3), (['rah'],2)]


###slide 36
LEVERAGING DICT PROPERTIES
Python Tutor LINK
word_dict = {'rah':2, 'ah':3, 'rom':1, 'mah':3, 'ro':1}
defoccurs_often (word_dict , x):
freq_list = []
word_freq_tuple = find_frequent_word (word_dict )
whileword_freq_tuple[1] > x:
freq_list.append(word_freq_tuple )
forword inword_freq_tuple [0]:
del(word_dict[word])
word_freq_tuple = find_frequent_word( word_dict)
returnfreq_list
6.100L Lecture 14

###slide 37
SOME OBSERVATIONS
Conversion of string into list of words enables use of list 
methods
Used words_list = song_words.split()
Iteration over list naturally follows from structure of lists
Used for w in words_list:
Dictionary stored the same data in a more appropriate way
Ability to access all values and all keys of dictionary allows 
natural looping methods
Used   for k,vin word_dict.items():
Mutability of dictionary enables iterative processing 
Used   del(word_dict[word])
Reused functions we already wrote!
6.100L Lecture 14


###slide 38
SUMMARY
Dictionaries have entries that map a key to a value
Keys are immutable/ hashable and unique objects
Values can be any object
Dictionaries can make code efficient
Implementation -wise
Runtime -wise
6.100L Lecture 14

##TRANSCRIPT

DICTIONARIES HOW TO STORE STUDENT INFO HOW TO ACCESS STUDENT INFO HOW TO STORE AND ACCESS STUDENT INFO A BETTER AND CLEANER WAY A DICTIONARY BIG IDEA A PYTHON DICTIONARY DICTIONARY LOOKUP YOU TRY IT! ['mg', [6, 7]]) DICTIONARY OPERATIONS DICTIONARY OPERATIONS most useful way to iterate over dict… Typical use is to itera DICTIONARY KEYS & VALUES WHY IMMUTABLE/HASHABLE KEYS? Memory block (like a list) Hash function: 1) Sum the letters 2) Take mod 16 (to fit in… A PYTHON DICTIONARY for STUDENT GRADES grades [0] returns 5 Ordered sequence of elements EXAMPLE: FIND MOST COMMON WORDS IN A SONG'S LYRICS lyrics in a pop song EXAMPLE: FIND MOST COMMON WORDS IN A… CREATING A DICTIONARY Python Tutor LINK USING THE DICTIONARY FIND WORDS WITH FREQUENCY GREATER THAN LEVERAGING DICT PROPERTIES Python Tutor LINK LEVERAGING DICT PROPERTIES All right, everyone, let's get started. So today's lecture will be on this thing called dictionaries, and it's not the dictionaries that our parents and grandparents used. Notice, I never actually used dictionary regular book dictionaries either. Maybe once in my entire life. But it's actually on a python dictionary. So this is going to be a new data type that we have not worked with before, but it'll be a compound data type. Much like we've seen lists and tuples to be. It's just going to be very different than lists and tuples. So before I introduce a bunch of syntax and and what a Python dictionary is, let's try to just motivate the need for such a data structure. So suppose we have the following problem. We've been dealing with this problem in many of our lectures, but we once again want to store student information. So let's say we want to store great information for a bunch of students with what we know so far. We can store information using lists. It's a very reasonable data structure to use because we might get new students in the class. Students might drop grades, might change things like that. So let's use this mutable data structure a list. Let's say we want to store names of students and their grades in the class like their final letter grade. Additionally, we can store things like micro quiz grades and pieces grades. But for now, let's just assume restoring just the names and the final grades in the class. So if we do this using lists, one reasonable way to store this information is by saying, Well, I'm going to have a list of all the names of the students in my class. I'm going to have a list of all the grades of these students in the class. And I'm basically going to go index by index and make the rule that says at a particular index, I'm storing all the information related to this one person. So I didn't get zero here. I'm storing the name of the student and their grade at index one. I'm storing the name of that student, John, and their grade at index two, I'm storing the name of that student and their grade and that index three and so on and so on. Right. So now I basically have to remember that for a particular index, I am storing all the information related to that student. Right. Okay. So seems like a reasonable way to to do this. Now, let's say that I wanted to look up the grade for a particular student. Okay. So I write this function called Get Grade. It takes in some parameters. So the first thing it'll take in is the name of the student. So an A for example, and I would pass in the list of all the names in my class and the list of all the grades in the class. So these are these two lists that I've previously created, right? So these get passed in to this function. So you can imagine if we have a list of everybody out of MIT, these lists are going to be pretty large that we're passing in as parameters. How do we actually grab the letter grade associated with the student? Well, we're going to use the fact that the letter grade for the student at index AI is in it in the grades list is going to be. Grabbing the letter grade for the student at that same index in the name list. Okay. So we have to figure out this particular student being passed in here, what index they're at in the names list. So that's what this line of code is doing. It's using this index function on the name list with a parameter, for example, Anna. So this will return for us, the index where Anna is in my list. So from the previous example, it's going to say that it's going to return the number zero because Anna is stored in the name list an index zero. So now that I have that index in hand stored in variable, I, I can just index into the grade list at that same index. Okay. So I can get grades list at index zero will return for me. The grade that I got for that particular class or whatever we're storing here. And then we just returned the tuple student comma grade. So this becomes really messy, right? I already mentioned that if I have a list of a whole bunch of students for a really large class or, you know, the entire university, then it becomes really unwieldy to just keep passing in all these lists. If I have in addition, all these micro quiz lists and all these problem set lists that also store additional information for the student, I then have to pass those in for their respective functions. And so it gets really messy, right, writing these functions that retrieve these this information. And additionally, if we're mutating these lists, like if a new student comes in and we need add all their information, I need to make sure to update every single one of these lists that I'm maintaining. If a student leaves, write or drops the class, I need to remember to remove that index from all of these different lists. So really, really messy situation that we could get into by using this method to store information about students. So let's try a different approach instead of using all of these different lists. Let's say that we're going to store everything in a master list so we're not storing many lists. We'll just store one list for the grades in the class, and the way it'll be stored, according to this in the slide, is going to be this grades list. So this is one list with three elements in it. And you can imagine if we have more students, we would just put all these students in this master list. So what is each one of these student elements? Well, each student element is itself a list. So already I've got my master list, and each element within this list is also a list. So this is a list for Eric, a list for Anna and a list for John. These are variable names. What are these lists going to be comprised of? Well, they will be comprised of three things. So notice. Right, two commas here. So the first thing is their name. The second thing is another list containing their problems, their grades. And I'm kind of using this element of that list to denote what that set of numbers represents. And then another list as my third element being for the Michael being the scores for the micro quiz grades. And again, I'm denoting the first element of that list telling me what this list contains. Okay, so I've got lists, master list with three sub lists for my three students. And each one of those lists contains three elements a string, a list and another list. And those two lists are then also comprised of a string and a list themselves. So super complex, a data structure or a sort of composition or design choice that I've made here. But it solves the problem of maintaining all these different lists in separate variables. So now let's say I wanted to write a function that gets the grades for a particular student for either, you know, problems that are in my grades. This is the function that does that. So, again, it's not looking super nice. So what is this function going to take in the who is going to be a string representing the name? So for example, Ana, the what will be also a string representing what information I'd like to grab either piece or MQ. And the data is going to be my master list of all the grades. So this grades equals this list of everything. So what is this code going to do? Well, it has a for loop down here. And a nested for loop inside it. The outer for loop basically looks through each one of these elements here and looks at the element at index zero. So either Eric, Anna or John and grabs only the list where that piece, the string here matches the who. All right. So if student at index zero equals who right here, then we found the student. I'm interested in grabbing the information for cool. So now I've gone. I grabbed the right piece, the right list, and now I'm interested in their grades for a particular what? Right. So either MQ or. Yes, so I do the exact same thing again for that list here. Right. So if I'm interested in Ana's grades, I've, I grab these lists here, right. And then I'm going to check if the info on index zero. So either this piece or this MQ matches the what. So either I'm Q to match what I'm interested in grabbing the information what information I'm interested in grabbing. And then I'm going to go inside this if statement if they match and the high return the who in the info so again super complex no need to understand this that well because we're not going to use this method for long so this get grades here. For example, if I grab a micro quiz grades and I run the code, it will return for me. This tuple that grabs that returns for me the name of the student. And then there's just this sub list of the thing that I was interested in, in this case, micro quiz. And it grabs for me all the grades and then I can then index into this returned to pull to grab either the first quiz or the second quiz grades. Okay. Um. And. And same for Anna. Right. In this particular case, it grabs for me just the tuple with my name and then that sub list with the problem. So great. Okay. So, again, really messy. I have to I've made my design choice for how to create this all these lists with some lists and some list within those. And so I'd have to document that probably if I was using this method and then this function to grab this information again, super complex, hard to read. So it's not really a great way to store information either. But the idea behind this, which is to try to store some data associated with some sort of key write the piece or MQ or in this case I'm storing, you know, a bunch of grades for Eric and or to that idea we can explore. And that's basically what dictionaries will do for us. It will allow us to create data structures that map some sort of custom index, a key to some value, so much like a book dictionary does, right? It maps the word to its definition. We'll be able to create our own dictionaries that map some object to another object. So when we create a dictionary, we call every sort of quote unquote element in the dictionary an entry. And that entry is, is that mapping of a key to a value. So just to draw a parallel with a list, we can think of a list as mapping something to another something. The thing that a list maps is this index number is 0123 in that order. Right so it has to start have an element at index zero and then that index increases by one from thereon. And for each one of these index indices, I'm mapping that index to some element in my list. Right. That's basically what the list there's something associated with index zero, something associated with the X one and so on. So it's kind of like a very restrictive dictionary, right? An actual python dictionary works in a similar way, except that now I am not putting any restrictions on my indices. My indices here become these sort of custom indices called a key. And so now I'm able to associate a value equivalent element in my list with that key so I can have an element associated with any object. Okay. So I am using the term value here and in a dictionary. The the key is associated with a value, and that's one entry in the dictionary. Now, this is going to be a little bit confusing because we've been using the term value to refer to just some objects value, right? Like, you know, in, you know, variable A has value five or something like that. But now I'm going to try to make a conscious effort now that we're introducing dictionary and dictionary values associated with a key to whenever I'm talking about the dictionary as value to say dictionary value, just so it's not confusing. Okay. But just, just keep that in mind. It can be a little bit confusing at first. Now that we're using the same terminology for two different things. So we're going to go through in this lecture, we're going to introduce a bunch of syntax and operations with dictionaries and there'll be lots of you try it exercises just to give you a little bit of practice with the syntax because this is kind of a syntax, heavy lecture. So hopefully it helps a little bit, but let's first see how to store data in a Python dictionary. So as I mentioned, a Python dictionary stores entries. And that entry is a key value pair. Okay. So you're mapping one key to its value. The key can be any immutable object. And we're going to see what this means in a little bit. And the value associated with that key or the python value associated with that key can be any object you'd like, even lists or other dictionaries. So the way we create a Python dictionary is by using these open and closed curly braces. So tuples were open and closed. Parentheses lists were open and closed square brackets. Dictionaries are open and closed curly braces. And this creates inside memory an empty dictionary. So an entry, a dictionary with zero entries. So the length of a dictionary is zero. To add to create a dictionary with one entry in it. Again, we have curly braces and we had one entry in it. So this something colon something else is an entry in my dictionary, one entry. And the thing before the colon is the key and the thing after the colon is the value associated with that key. So you can think of it. If we're drawing a parallel to lists, this is now mapping, you know, sort of at this custom index for we're putting element 16. Okay. So we can also create dictionaries that aren't just full of integers, and you can mix and match data types as you'd like. But usually in dictionaries we kind of have the keys, all be the same type and the values, you know, all be the same type. But you can certainly mix and match types just like you could. You could create lists and tuples full of an integer and a float and another list, you know, and mix and match in that way. So here I'm creating a dictionary again. Open and closed. Curly braces starts my dictionary and it has four elements in it. So each sorry, four entries in it and each entry is separated by a comma. I've got here my first entry. So it is mapping the key, Anna, to the dictionary value be. My second entry maps key map to value a third entry maps key drawn to value B and last entry maps key 82 value. Right? So this is a dictionary that essentially maps strings to other strings. So you can see here, I've kind of visualized the dictionary that we just created. We've got these custom indices, right? So we're basically mapping names to letter grades. Everything okay so far? Does it make sense? I guess conceptually. Okay. Okay. So the first thing we'd like to do is once we have a dictionary full of a bunch of entries, how do we grab an entry? How do we look up a value associated with a key? So the way we do that is in a very similar way to the way we look up an element in a list. Right. A key in a dictionary is just a custom index. Right. So how did we look up an element in a list? So if I wanted the element at index three, I would basically say l score brackets three. And that grabs for me the value at that index. Well, now I've got my custom indices right. My custom indices are these strings. The syntax will be exactly the same. I've got this custom index I'd like to look up. So I say dictionary name, square bracket. Custom index. So if I say great square bracket John Python will go in to my dictionary named grades it'll look up the key John. And it'll return for me the value associated with that key be. So this entire expression here is a value evaluates or gets replaced with the string. B Just like when we indexed into a list. L Score brackets. Three We replaced that entire index indexing operation with the value of the element at that location. Right. So similar here. If I try to index into a dictionary and that key doesn't exist. So notice my dictionary has no string. Grace. Python will give me a kicker. So if you run code with dictionaries and you get a killer exception being raised in the console, you'll know that you're trying to index into a key that doesn't exist. So the question might be, yes, we're able to look up a value. Right. Given a key, can we do the same thing backwards? Given a key? Sorry, given a value like a, B, C, whatever. Can we look up a key associated with that value? And the answer is no. We'd have to write some sort of loop or some sort of code that goes through every item in my dictionary to to check each value and see whether the key associated with that value is equivalent to the one I'm looking for. So there is no nice expression to do that backward operation. And that's because the values in my dictionary can be repeated. So if I look up the value, be right and I want what's the key associated with B? Well, there's actually two of them. So how does Python know I want both of them? How does it know I want only one of them? How does it know? I want maybe a list of all these things. It doesn't, right? So you'd have to write code that does something for that operation. And we're going to see how to do that later. Okay. So let's have you work on this. You try it. And this is just an exercise in looking up a value. So this is a function I'd like to write according to the specification. So it's called find grades. Grades is a dictionary mapping student names to grades. So string to string exactly like we've seen in the previous slide. And students is going to be a list of student names. So in the example here, I've got my input dictionary, this thing we just saw. And then my list of student grades is, for example, you know, these two strings, Matt and Katie. For a bunch of these questions, especially the one on the micro quiz and things like that. If it gets a little confusing when I try to write the specification in a very detailed way to make it clear what I'd like from from this function, it's important to try to use the example to help you figure out what we'd like, because we're writing the specification in a general sense. But the example should hopefully make things really clear for what we'd like. So in this particular case, what we want the function to return is a list of the grades for the students being passed it. Right. So we look up Matt, we see that their grade is a C, we look up Katie, their grades. And so I want to return the list C comma, right in the same order that I passed in my students. So I'll give you a couple of minutes to work on that and then we can write it together. So that's a line 94. So this is just an exercise on looking up values in the dictionary. All right. Does anybody have a start for me? Yes, please. Yeah. L knew. How about that? So this will be my results list. Yep. Yup. For loop. Yep. So grades square bracket alum looks up the value associated with my student named Elm. And maybe we can save it like this. Grade equals this. And then you said append. Yep. So we can do l new dot append the grade. Anything else? Yep. A return so we can return on you. Yup. So very reasonable code. I like it a lot. You know, besides the first lecture, I don't know that we've written any code that didn't involve a loop. So your best bet for writing code from or for any sort of thing in this class is to think, what loop can I do? So let's run the code and it should return for me. See, I'm a and it does. Now that we can iterate. So, you know, I mentioned this before, but once we're iterating over tuples and lists and things like that, one thing I would add and just for debugging purposes is say something like Elm is and then you can say like an example of what it could be like Ana or Matt or whatever it could be. Just to remind yourself that that thing, that loop variable is a string. And so it's one less thing to remember as you're writing further code. This is really nice. Okay. So dictionaries are already proving to be really, really useful. We can create values associated with custom indices. And if we want to grab the value associated with that custom index, it's really just a matter of indexing. Using a key, using that specific key, much like we did indexing into a list. Okay. No need to loop none of that. Iteration. It's just a single line of code that indexes into the list. So let's see a few more operations before we do the next. You try it. So I've got my list of grades that we've been working with in the past couple of slides. Let's say that we now want to add a new student in their grade. The way we do that is very similar to the way that we would add an element to a list. Once we already have an index for that list right here, notice we don't actually have a slot for grace yet. I'd like to add her to my dictionary. That's okay. With this particular syntax here. So grades at key grace. If Python does not find grace in my list, in my dictionary of keys, it'll just add her. Okay. Which is really nice, right? I don't need to check if she's already in there. There's no looping. You just say no grades at grace equals. Boom. It adds it for you. What if I want to change an entry in my dictionary? Well, let's say I want to change Grace's grade to a C grades at custom index. Grace equals C will go in. Look at my keys. When Grace didn't exist, Python added her with her value. But she already exists there. So Python will just overwrite her value. So really nice. You know, something to look out for in case you already have values in the dictionary. You know, you want to be careful if you actually do want to overwrite things, but it's really, really nice behavior and that's different than let's write. Especially adding an entry to the dictionary. To the dictionary. You can delete entries much like we deleted entries from a list. We use the dell function. And the Dell function says what entry you'd like to delete from what list? So here we just say the name of our dictionary at index. So this will completely remove Anna and her value and the value associated with Anna from the. From the dictionary. So what I want to make a note of is that our dictionaries being mutated with all of these different methods are all of these different functions, right? So here, when I added Grace, I've mutated my original dictionary. Right? The animation didn't make a copy of this dictionary with Grace added, leaving the original unchanged. I've literally gone in and mutated my original dictionary to Grace. I've mutated the original dictionary to act to change her grade. I've mutated the original dictionary to remove Anna from the dictionary. Right. So all these. All these functions are actually mutating in my dictionary. Okay. One other very useful thing that you can do with dictionaries is to check if a key is in my dictionary. So we do this using the in operator in keyword. We've seen the keyword being used to check if an element is in a list, to check if a substring or a character is in a string, to check if some element is in a tuple. We can also use it to check if an element or a key is in my in my dictionary. So I want to make a note. It's only checking the keys. It does not look for the values in the dictionary. We'll see how to check if some value is in the dictionary in a little bit, but in keyword specifically, only looks at the keys in the dictionary. So if I have the expression as the string John is in grades. Python only looks at the keys and say, yup, there it is. I don't care what values associated with it, I just care that it's in my keys. So this entire expression here, John, in grades will evaluate will be replaced with. True. Daniel obviously is not in my dictionary keys. So returns false. B is not in my dictionary keys. Even though it's in my values, it still returns false because it only looks at the keys. All right, let's have you try this exercise. So function is called find an L again, we can use the specifications and the example to help us figure out what we'd like from this function. So l d is going to be a list of dictionaries. So in the example here I've got three dictionaries defined and the first parameter here, the thing being passed as l d is the list with d one de to D3 as my elements and K is just an integer. What I'd like to do is return true from the function, if that key is a key in any of these dictionaries and false otherwise. So as soon as I see a key that matches K, I want to return. True. So in this example here, when I look at look for the K to inside these dictionaries D one doesn't have it, but D two has it. So I would return true when I look for 25 in that same list of dictionaries, 25 is a value in one of these in D three, but it's not a key in do you want it to be three? So that would return. All right. So that's just a little lower line 115. Give you a couple moments and then we can write it together like usual. All right. Does anyone want to start me off here? So. How can we do this? Create a loop? Yes. For you and for. Yep. Okay. So that means that D is, you know, I can say like K one mapped to V one or something like that. Right. Key to a value. If. Okay. Indy Yup. So that will check for me my keys in that particular dictionary that I'm looking at right now. Yep. We can immediately return. True, right. As soon as we found it. No need to check the other dictionaries just pop out of the function and return. True. Same inside the F or inside the floor? Outside the floor. Outside the four. We can return. False. Yep. I like this code a lot. Uses this in operator right to do that the task. So the return false outside of the for loop works really well because if I've gone through every d inside l d here, then I'm checking every single dictionary. Right. As soon as I find one that has that key, this return true acts like a break and a return. Right. So breaks out of the loop and returns immediately. And it doesn't return false. But if I've gone through every dictionary and didn't find the the key matching key, then I return. False. Did anybody try it a different way? Or is this. We could certainly try it with a boolean flag. Right. We can flag the fact that we found it through some loop and keep track of it and at the end just return that flag. That's another way to do it. But this is probably the most python likely. So we can run it on these two examples here. Right. So I'm expecting to be looking up to the return. True. And looking up 25 to return false. And it does. Questions about this code or dictionary so far as everything. Okay so far. Okay. All right. A couple more operations. So, so far, we've looked up values in the dictionary. We've added stuff to the dictionary. We've deleted stuff from the dictionary. One really useful thing to do is to be able to look at every single entry in my dictionary. The reason why we'd want to do this is because we should assume that when we create our dictionaries, there's no order to them. Right. This is very much unlike lists. Lists had an order to them. We knew that the first element in our list was that index zero. The next one was an index one and so on. Right lists were ordered sequences of of of elements. But dictionaries are not ordered sequences of elements. That's not super true. There are up until a very recent version of Python, there was no guarantee to order. They were put in some order that couldn't that I, I couldn't figure out how it was determined. But I forget which Python version, maybe 3.6 or something like that started to guarantee an order when you went for, for the list for the dictionary element in that order was the same order that you inserted the elements. Okay. But if you'd like to write robust code that could be run by people, you know, using an older version of Python, you should write the code. Assuming that no such order exists and it's okay. It doesn't make the code that much harder to write. But if we're not assuming any order to Python entries in the dictionary, then that means a lot of times we actually have to look at each entry in the dictionary to do some sort of task. Okay. So one of the first things you might want to do is to iterate through all the keys in the dictionary. To do that, we use a function called grades dot keys, and this great squeeze function here doesn't mutate the dictionary at all, but instead it returns for me an iterable, a sequence of values which are all the keys in my dictionary. Now the data type of this return value is called dict underscore keys. It's not a data type we've worked with before. Okay. Looks really weird. But if you'd like and you don't have to do this, you can always cast this sequence of values, that type dict keys to a list like this. So if you cast to a list grades, dot keys, it gives for us this more recognizable list with each key being an element in the list. Okay. You don't have to do this. But if it makes it easier for you, you can. Okay, so this line of code here grades our kids returns for you. You can think of it like this, Iterable. This list of all the keys in the dictionary, they're not ordered, right? I mean, they're ordered in the order that I added them into the dictionary. Right. And then Matt, then John than Katie. But they're not sorted in alphabetical order. If you have integers, they won't be sorted in ascending or descending order. So it's best to just not assume an order to begin. Similarly, we can get an iterable of all the values in the dictionary. Okay. And to do this, no surprise there we use grades, not values. And this is, again, a function where it doesn't mutate the grades at all, but instead gets replaced with this dict values data type. Never seen it before either. And you can cast it to a list if you'd like because it makes more sense to us at this point in time, which just returns for us. This list of every single value in my dictionary. Again, no order, right? We can see that there's no order except for the order that we actually added the element. Yeah. Um, when you say, like, an act like a boy, do you mean like another time about. Not the same. Yeah. Yeah, it'll turn out the same. The same iterable, I guess if you do it again. Yeah. Just doing like if they're just iterating over the dictionary there. It's like it comes out nowhere if you're iterating over the dictionary, not in the Python version we're using, but in a previous version. If you ran your on your machine or if I ran the same code on my machine, it might have given me a different order. But in the versions we're using from now on in Python, right. Because you guys all probably downloaded the latest version of of, you know, Anaconda and Spider. It will it will guarantee the order that you inserted the elements in. But if somebody's using an older version of Python takes your code and runs it, they might actually get, you know, A, B, B or some other order for these for these functions here. Right? Yes, you're welcome. So these being iterable just means that we can have something like for I or so for K in grades, our keys, basically giving us a loop where K is going to be each element in this list. So that's fine. So we can iterate over the keys or we can iterate over the values directly. But what I find personally most effective is to iterate over each entry in the dictionary, so not just over the keys or the values by themselves. It's to iterate over the keys and the values together. So to do that. We use this function called grades dot items. And unsurprisingly, this will return also an iterable where each element in my iterable is not just the key or the value, it's a tuple of the key, comma, the value. Okay. And again, we can cast it to a list to give us something that's more recognizable. You can see now each element in the returned list is going to be the tuple where I have an entry, right? So my entry and a comma B is this first element in my return list. And then Matt and then John B and then Katie. So I grab these entries together where I have access to both the key and the value for that entry, which means and this is the important part, that we can do something like this and we can do this for the previous slide as well. But for this particular grade sort items, iteration, if we're grabbing a key value pair out of items, that means we can do something like this for k comma V in grades dot items. Means that Python will map K to the key for that entry and read to the value for that entry as I'm iterating over each one of these pairs, right? So with each iteration, I have access to both the key and the value for that entry, which is pretty useful. Right. So if I have this line of code here, if I print key o k has value v the k and the v will change with each entry. Right. I'm just grabbing both the key and the value for that entry. Yeah. Question the a result. I didn't actually look at it. It's not a tuple. So the actual object type is this thing dict underscore items. So again, not a type that we've we've worked with before, but that's just the type, right? Like we've seen lists, tuples, dictionaries, dict underscore items is another data type. Yeah. But the cool thing is that it's an iterable. So it's a sequence of values, which means that you can cast it to a list, which is also a sequence of values and a knows how to do that casting. And you get to the more recognizable list that we've been using. Other questions. Okay. So I really like using greatsword items to iterate over entries. So let's have you try this exercise. So it's a function called count matches. It takes in one dictionary D. I didn't say what the the the elements are, but, you know, you can mix and match. So here I have a dictionary with just in its mapped to it and here I've got a dictionary where it maps you know, in some strings and things like that. And what I want this function to do is tell me how many entries in this input dictionaries have the key match its value. So here in this first example, the key here is one the values two so they don't match. These don't match and these don't match. So the count should be zero. But down here in this example, the one doesn't match to two. So that's fine. But the key matches its value. One count key five matches its value two counts. Right. So this should return count to. All right. Let's have you work on that down by line 137, and then we'll write it together. All right. How could I start this? Yes. Account? Yes. Zero. Yep. A for loop? Yup. Yep. As a function? Yep. We woke you up. So this is where my value equals my key for that particular country. Count equals count plus. Perfect. Yep. Return count. Did anybody do it a different way? Okay. Awesome. Look. Yeah. Why? Oh, yeah, we can write it. Yeah. Yeah. Like mechanical zero. And then it is like four x. I think they were just going to pass the value. I got it. I was going to call. Yeah. So we can say for X and D dot keys or something like that. Right. Something like that or no. We can also say for X and D, I think that might work too, because it would grab the key for us. But just to be safe. Keys. And now we need to grab the value. So how do you grab the value associated with X? No. Yes. It's just indexing. Right. So these four brackets X are oops if. D score brackets x equals. So that's the value equals the key. Right. Then again, we count plus one. So this is the. Either way. Yep. So we don't have to use items, but it just items makes things easier because we have in hand a variable that's, you know, the value and the variable that's the key. And doing things like indexing starts to get confusing. If you know, I mean, it can be confusing, but yeah, both ways are very valid. So let's run it. And it should work. So the first count is zero, as we expected, in the second count as two. Is that any questions about this code? Does it make sense? Is there another way that somebody tried it? Okay. Okay. So dictionaries are mutable objects. Right. So all the aliasing and cloning rules apply. You remember when we talked about lists and using the equal sign between a list and another variable name, just a plain old equal sign means that you are making an alias for that list. Same thing applies to dictionaries. So using saying D one equals d two where d two is a dictionary means that you've just created an alias for that dictionary. So if you change the dictionary through either of those variables, you're changing the object itself. If you want to actually make a copy, you use D copy. Where D is the name of the dictionary? You'd like a copy and that gives you a copy of that dictionary, and then you can change it without changing the original one. So let's talk a little bit about the values for a dictionary and the keys, because there are some restrictions on the keys for the dictionary. No restrictions on the values. So dictionary values can be any type, right? You can have a dictionary value that's a float and string tuple. You can have a dictionary value. That's a list which is a mutable object. You could have a dictionary value. That's another dictionary. All are okay, whatever you'd like for the values to be. You can have dictionary values that are duplicates, so you can have one key that maps to value. Five Another key that maps to value five. All good. Okay. So the key is so the values don't need to be unique. We do have restrictions on the keys, though. Okay. The first restriction on the keys is that it has to be unique. Right. So if you're mapping a key. One. Two. Value five. You cannot map a key one to value six. Because if you go and look up the value associated with one, how does Python know which value you'd like? The five or the six? Right. So the keys have to be unique, first of all. Second, the keys have to be immutable, technically hackable, but for the purposes of this class, just think of them as having to be immutable. So a key can only be one of these types that we've seen so far int, float, string, tuple or bool. You cannot have a key. That's a list. You cannot have a key. That's a dictionary because they're mutable objects. So let's look at that a little bit further and in detail. So the reason why we can't have a key that is mutable is because of the way keys are stored in Python. Sorry. The way the dictionaries are stored in Python. So I'm going to show you an example on the next slide. First, I'm going to explain how they're stored, and then we'll go through an example showing you exactly why you can't have a mutable structure. So the way keys are, the way dictionaries are stored in Python is you first need a key right to associate with a value. So everything starts off with the key you'd like to add to your dictionary. So Python basically runs a function called a hash function on the key. For simplicity's sake, let's say the key you're trying to store is a number. That hash function might return that same number. It might return something else. If you're trying to store a string as a key python again, runs it maybe a different hash function that takes in that string, which might be a bunch of characters and it converts it to some number. So the hash function always takes in your key and converts it to a number. Okay. That number. Think of it like representing a memory location where you're going to store the value associated with that key. Right. So you're always grabbing a number that represents a memory location. At that memory location, you will store the value. So next time you want to look up the value associated with a key, you just run that same hash function. The function won't change. You run the same hash function on your object and you'll be able to get that same integer back. You'll be able to grab that same value back. But if you're storing mutable objects, that means that object can change. So if you run the hash function, the thing that gives you a number on something that's changed. That number might not be the same. Right, because you've changed the thing that you're passing into the function. So why would it give you the same value back? So let's look at this example. So again, we're storing grades and let's say we're trying to store a bunch of grades inside our memory. And let's say our memory is just 16 locations, so zero through 50. So at each of these locations, I'm going to store grades associated with a person. The function I'm going to run on. The student is using their name, so I'm going to store Anna's grade somewhere. But I need to run a function that takes in the string Anna and gets gets for me a number. That number is where I'm going to store my grade. So a simple hash function we might do is to say, well, I'm going to take a and map it to one B, map it to to see them up to three and so on. I can sum all of those numbers associated with my letters in my name. Write 16 and then I can mod it with 16, which is how many entries I have in my memory. So if I it with 16, that's going to give me a number zero through 15, right? If you take the remainder, when you divide by 16, you'll either get zero all the way up through 50. So if I made my name, that means I'm going to store my grade at a memory location. Zero. So far so good. So I'm basically I made up this hash function that tells me where to put my my great. Now I add another person again. I'm going to look I'm going to convert the letters in their name to numbers so that I can easily get a number out of their out of their their letters. So I'm basically hashing their number, their letters to a number. Again, summing this for is 35. I'm going to mod it with 16, which means I'm going to put Erick's grade at location three. Next person. John. Same thing. Add the numbers mod 16. I'm going to put John at location 15. So this is my memory where I'm storing the values associated with these students. So if I want to grab back my grade, I run the exact same hash function. So I'm going to run the same hash function on my name. My name hasn't changed, right? It's still the string. I'm not allowed to change it because it's a string. And so I'm going to get the same value back zero. So that means to grab the letter associated with my name. I just need to go straight into my memory location and look up the value associated the value at that memory location. So I know it's going to be a C. Now, let's say I'm storing a list. A student name as a list. So again, Anna, Erick and John are immutable, right? They will not change. But if I store Kate as a list, her name might change. Again. I can run the same hash function on her name. That means her grade when I first store. It is going to be at location five, so I'm storing Kate at location five. All these three strings I know I can get back because they cannot change. But let's say that Kate went, goes and changes her name from Kate with a Kate to Kate with a C. It's the same object, right? The same person. She earned her grade B originally. So if I want to grab her grade back, even though her name has changed, I would still like to grab the B associated with her as a person. But Kate, with a C, if I run that same hash function that I ran to put her great in my table. Tells me that I now need to look up her grade at memory location 13 no longer at memory location five. Right. She's not there. Okay. So now it's like, you know, did the student disappear? All that stuff. So you see, now that means that's that's the reason why I cannot have a more immutable object as a key to my list. Because if that object changes. Running that hash function on that changed object might not give me the same memory location where I originally stored the value associated with that object. That makes sense. Okay. So let's revisit our original example, the one where we tried to store everything in a master list, all these grades in the master list. Now, let's store it in a master dictionary. Okay. So I've got my grades notice. Curly bracket. Curly bracket is a dictionary. I've got two students in my class and. Right. So this is Anna's information. And Bob, that's Bob's information. So just two students in my master dictionary. So the key, Anna. Right. Is going to be one entries, one entry key. Key, Bob is the other entry key. And once that information associated with these keys. Well, with Anna, I've got this dictionary associated with her name. So that's this big thing here. I'll explain it in a bit. And similarly with Bob, Bob has one thing associated with it, and it's another dictionary. So I'm mapping strings to dictionaries here, and that's fine because values in the dictionary can be other dictionaries. So what are these dictionaries about? Well, the number of items in the dictionary for a person. For a particular person, there's three elements, right? So comma, comma separates my three elements. The first one is going to be mapped with Key and Q, the second one mapped with key piece for problem set and the last one mapped with the string fin for final grade. So each one of these students has this dictionary associated with them. And that dictionary then itself has three entries one for the micro quiz, one for the one for the final scores. So now what's the values associated with those keys? Well, the micro quiz is going to be a list. The problem that is going to be a list and the final is going to be a string. So a really nice representation of my of my class. And same for Bob. So now what if we want to grab a student's exam grade or the student's list of exam grades? Remember that big function, right? With the two nested for loops and the nested ifs, that becomes baseline. Isn't that cool? APPLAUSE. I like that. Yeah, exactly. We should applaud this because look how easy it is now, too. Yes. Thank you. Yes. Dictionaries are awesome, guys. So. Yeah. So, look, that line becomes this, you know, grabbing one one's quiz score becomes this single line of code right here. So let's break it down again. We do. Left to right whenever we've got this chain of stuff going on. So the first thing we say is, well, we're looking up grades at some index. So grades that some index gives me that dictionary. So something like this whole thing here, right? Okay. Good. That's first chain. Now, this box here gets replaced with that dictionary, and I'm doing another index into that dictionary, so that means I'm going to grab the MQ associated with. That that dictionary. So the value associated with them. Q Is going to be this list five, four, four. So this box here gets replaced with the list five for four. And then if I want to grab just the first quiz value, I say now I'm going to index in the list five for four at index zero. So that grabs for me just the five. So then the first quiz score for Anna was a five. It's pretty bad. Okay. So. Let's have you think about this. This is a function. Nothing to code here. Just. Just to think this is a function that grabs. The average of every single. Thing. Where that thing is. What in the class. So if what is MQ as you know is in down here in this example if what is MQ this code is supposed to get the average of all of the micro quizzes for all the students in the class. So you basically want to grab the average of ten plus eight plus three. And if it's P. S, I would like to grab the average of all the problem sets for all the students in the class. So the average of ten, ten, seven, eight and zero. So we've got a loop, right? That goes through other student in the Keys. So the student student stud dude here is going to be this dictionary, right? So given this dictionary, what line should you insert here such that you're creating a list, just a single top level list of all of the values in there. So the thing you actually want to end up with, and if we're looking at the scores, just because it's a little easier to think about, is going to be ten, ten, right? Seven, eight and zero. So in the end, what I would like to get in my all data, this list that I'm maintaining here is something like this for the piece. So think about which one of these lines will accomplish that. And just to help you out we can say student is, you know my dictionary of who thinks it's the first one. Second one. Third one. Fourth one. Nobody thought it's the first one. You guys sure? Okay. Why do you think it's the second one? Is it because of the append? Yeah. Let's think about it. So all data is a list. And what are we appending? So what is data at stud at? What's going to give us? Data at student. Is the dictionary. This dictionary here. Right. This. Well, you hear. And if we take this value and index into the what will it be an integer or will it be a list? A list. So when we append a list to another list, what is that going to give us? So if we have a list already with, you know, you know, ABC, if I open another list to this, will it put the element within that list or the list itself? Yeah, exactly. So I don't that's not going to work for us. Clearly, this is not right either and definitely indexing into data at student at what is not going to be right. Okay. So that leaves one other choice. The first one. So let's see why the first one works. We're concatenating right so the plus concatenate. So let's say I already have a list, a, b, c, I'm going to concatenate something I already have with data at student at what. Which we said is what is it a single element or another list. Exactly. So we can name with something like, you know, ten, ten or something like that. So that will return for us A, B, C, ten, ten, which will allow us to do something like getting the sum of all these elements. Questions about that as it makes sense. Yes. Oh. Yeah. But why? Why wouldn't it? I like how Americans tend to dislike and. Because we're indexing into M2. So if you index into MQ, MQ is your key. So you grab the value associated with that key. So that would be this list here. The ten or four. It would be the list. Ten, ten. So quick recap on lists and dictionaries before we do one final longer example. So again, lists are ordered sequences of elements, right? There is some element at index zero. There's some element in index one, some element in index two. So we do have these quote unquote indices. Right. But there's there's an order to these indices and there has to be an element index zero and further up from there. Right. Dictionaries also have these quote unquote indices, which we call keys, but these are custom. So you can basically rearrange. You can think of it as being allowed to rearrange indices however you'd like. Right. There's no order to the indices in a dictionary. There are some restrictions on the keys or these indices so they can't be immutable or hackable. But other than that, you know, the things that you store related to that key can be any type, just like you can store any type in a list. So the last thing I'd like to go through is a larger example, and this will showcase a whole bunch of things that we've been talking about so far and will showcase sort of how to, first of all, create dictionaries, which is what we did today. It will showcase how to reuse functions. You know, how to write functions and reuse functions in other places. It will showcase a little bit of immutability as well. But, you know, this is all in a larger example. And, you know, if I go a little bit fast through this, I've given you Python tutor links and it's also in the file to run on your own so that the goal of this function, of this last example is to basically find the most common words in a song's lyrics. And dictionaries are going to be really useful for doing something like this. So I'm going to show you, first of all, what we want to end up with, and then we can talk about how to divide this larger problem into smaller pieces. So, uh, okay, so those are all the pieces. But basically what I want to end up with is I want to have a song. Be stored as a string. Okay. You'll recognize these, but these are very old. I actually haven't updated these songs for a few years. But anyway, don't judge. So I've got a song stored as a string. And I'm going to run each individual function. But in the end, what I'd like to do is come up with something like this. So I want to present the user the top most common words in the song. So here I have a list. So you can see open, close square bracket tells me it's a list and I've got elements in my list. So here's the first element in my list, which tells the user that the word EI occurs 18 times. The next element on my list tells the user that the word we occurred 17 times. The next element tells the user that the words ain't ever getting older, occur all 16 times, and then so on. Right? So we're decreasing in frequency, but the most common word occurring 18 times. And then I'm showing the user the most common words are down to and including six. So I would choose some arbitrary value. I want to find in the song the words that occur at least six times, for example. So that's the goal of this program. So how will we achieve this? It's obviously a pretty big task. I wouldn't want to code, you know, the entire thing right off the bat, but we can actually divide it into three smaller pieces. The first piece and we're going to write the code for this is to create something called a frequency dictionary. So given a string of words, we're going to create a dictionary that maps each word to how often it occurs. So fancy word, frequency dictionary. But it's pretty simple. It just maps the word to its count inside my long string. So this presents the data, which is this string of words in a much nicer format, right? It's a dictionary that tells me the frequency of each word. Once I have that in hand, things get a little bit easier. I can write another function that finds the word that occurs most often in that dictionary. So the way I'm going to do that is look up the frequencies in the values, find the maximum of those values, and then figure out which keys are associated with that maximum value. And this is all made possible because I've reimagined my data in this frequency dictionary format. The last step. Once I figure out how to write a function that returns for me, the words that occurred the most times is to find the words that occur at least some number of times. And I'll go through an example of this one in a few slides when we get to it. But this last function here, number three, you can actually rewrite it in a whole bunch of ways. I'm just going to show you one way to write it. That'll involve immutability, but you don't have to do it using your ability. You can definitely do it in a whole bunch of, you know, with a whole bunch of other implementations. So let's begin by first creating a dictionary that maps the words to their frequencies. So I've picked a song that has a real song and it has some repetition, and it's short that it fits in one line. So I've got this song here and I've got my function generate word dictionary. The song is a string, right? So it's basically the song a little bit cleaned up, not in terms of words, but in terms of removing punctuation, removing, you know, commas, maybe exclamation or I might have kept quotations or something like that. But basically it's removing all of the punctuation and stuff because that will mess up my word count. So what is this function going to do given a string for my song? Well, first, I'm going to convert all my letters to lowercase. This means that Capital G will be counted as the same as the same word as lowercase lowercase tag, which is the correct way to do it. So convert everything to lowercase. Then I'm going to use our friend the split function, remember, which takes in my string and splits on a character. So by default it'll split on the space. This puts our string of words in a very manageable format. A list of words. Right. Much nicer to work with lists than work with a string. Now that I have my word list, I'm going to create my empty dictionary and then populate it. So I'm iterating over my list of words. And then I have a choice. Either. I've seen this word already and I want to update the frequency. Right. So I want to increase the frequency by one because I've already added this diction, this word to my dictionary, or this is the first time I'm seeing this word. And I want to add it to my dictionary with a frequency of one. So the first if the first case here, the if we'll update the frequency because I've already seen the word in my dictionary. So here I'm using the keyword to check if the key, the word is already in my dictionary. If so, I increase its frequency by one. Otherwise, this is the first time I'm adding my word to my dictionary. So give it a frequency of one. And then I return the word dictionary. Right. So this will map strings to integers. Let's work through it in the Python tutor. So. Step, step, step, step, step. Lowercase my input string step. I've split it. So now I've got this list of all of my words. Step. This is where we begin. So I've created my empty dictionary over here. This is. Keep an eye on this area here. It will be populated soon. The first word W is RA. Right. It's the first word of my list. It's obviously the first time I'm seeing it. I have nothing in my dictionary right now, so I'm going to pop in my else and I'm going to add it to my dictionary with a frequency of one. That worked. Next word in my dictionary is in my list is this one same word I've already seen. So I'm going to go inside the F and increase the frequency to two. All right. Is now two. Next is all right. So here's my word. I've got the next one in my list. It's the first time I'm seeing it. Add it to my dictionary. The frequency of one next word I'm seeing is again, increase its frequency to two and I'm going to go faster. Now, this is increasing frequency to three, right? Because I've seen it three times now and then I'm adding Rome for the first time, Ma for the first time and row for the first time. And lastly, I'm going to increase my. Frequency two more times because it occurs two more times in my song, right? So it's increased to two and now it's increased to three. And then we're done. So we return the word dictionary. Really nice way to represent my list. My. My son. Right. Very nice. Okay. So now that I have this frequency dictionary and I've put it up here, this is what we ended up with. How can we write a function that returns for me the most frequent word? So one thing we can recognize is the most frequent word has the highest value python dictionary value in my dictionary. Right. So as a human, I would kind of look to see which which one of these entries have the biggest value. As a computer, I can't really do that because I have to do it a little bit more systematically. So what we can say is, well, let's look at our values and grab the maximum of the values. So here I'm using this dot values function on my dictionary to grab for to grab for me all of the values in my dictionary. So this will be kind of like the list two, comma three. Come on, one, comma, three, come in one. And then I'm running the max function on that list. So max of this list of numbers gives me the maximum value in that list of the three. So highest now has the value integer three. And now all I need to do is iterate over my element entries in my dictionary. So this is in the items and I'm checking now inside this iteration is if the value is equal to the highest. So as I'm looking at each entry, is the value for that entry the same as the highest one I've seen? If it is, I'm going to maintain a list of all the words with that highest value, because there might be more than one word that has that highest value, as we saw when we actually ran it here. Right here, I had a list of all of these words that occurred 16 times. So that's kind of the output that I want to maintain. Okay. So I'm appending to my words list and returning this tuple with the words comma that highest value. So. Python tutor like a like in the previous time. So let's create our original dictionary. This is what we ended up with last time. So the highest values three here and I'm going to loop through each entry in my dictionary so you can say C, k v is going to be each one of these in order. So first it's right two, then it's three and so on. Obviously the two is not equal to the three, so we move on. The three equals the three. So we take the R and boom, add it to my list here. So this is the list I'm maintaining of all the words that occur with that frequency three next. No for Rome. Yes for my. So I'm going to add it to my list and then no for row and I'm done. So the return is going to be this list. You know, this tuple here with the list of the words that occur three times. Okay. Good. Last part, I'm not going to go through Python tutor. I did include a link to it because it becomes very messy with the arrows. But I do encourage you to try it. Try to follow it along on your own time. I will explain how. However, the the way that I chose to solve this problem. So I chose to solve this problem to include mutation and reusing the function that we just wrote that grabs for me the highest value and the words associated with that highest frequency value. So this is the idea. I have my original word dictionary. Right. This is the frequency dictionary we created right off the bat. What I'm going to do is look to see which words occur with the highest frequency. So the highest frequency. My function from before grabs for me figures out that it's three and it figures out the words associated with that three. R and my. That's exactly what we just did. So I'm going to grab those words and those entries in the dictionary, and then I'm going to mutate the dictionary to remove those words, because I know those words occur with the highest frequency. So now I remove those words and I have saved them because they were the result of the function that I had just right. So I'm maintaining this frequency list which will contain all the words that occur, at least I guess I said one at greater than one time, so at least two times. So I'm going to grab the ones that occur three and two times. So right now, I had just grabbed the words that occur three times. I've remove them from my dictionary, so I've actually mutated my dictionary to remove those words. Now, if I run the exact same function that I just wrote the previous slide on this mutated dictionary. Which words will it give me? Which words occur the most now? Exactly right now. The highest value in my dictionary, in this frequency dictionary is two because I mutated to remove what was previously the highest value. So I'm running the same function again on the mutated dictionary to give me just the right. So I grab that, keep track of that in my frequency list. Right. Mutate the dictionary to remove that. And as I'm doing that, I'm I'm also keeping track to make sure that the highest frequency I have in the remaining dictionary is at least, you know, whatever I was interested in. So here I wanted at least two. So this function, the one I'll write, will no longer grab any other values from the dictionary because now one frequency, one I don't want to graph. So this is the resulting value. And that's the idea. We're using your ability in the function we just wrote to do this task. And this is the code that does that. So this runs the function we wrote previously. Step number two gives us that list, that tuple with the list of all the words. This loop here. Make sure I'm. I still have frequencies that are at least X in the dictionary. I grab the the tuple that I just created so something like this and add it to my frequency list. So this is the resulting list that I'm keeping track of. And then this bit here removes the word for my dictionary. So I'm mutating the dictionary using this del keyword that we saw at the beginning of this lecture. Yeah, of course. Uh. Well, well, well. Basically. Well, no. Yeah. I guess I would just. Why is it? Well, then that's. So I think maybe it's because the function I forget what the specification said, but I don't know if it said at least two or greater than two or greater at least x or greater than x. It depends on which one I actually said in the specification. But you can imagine changing this to greater than or greater than or equal to. And then we're running this function again inside this y loop to grab the the frequency that. Yeah. So these are just the observations I actually stated at the beginning of this example, a bunch of the different things that we've learned that we're using within this example. So slicing or splitting, iterating over the list directly. Mutability, you know, using the items. Things like that. Okay, so that's it. That's all I have. I'll see you guys on Monday. Monday is Halloween. If you'd like to bring a costume, I love Halloween. I will wear something different than what I usually wear. 
