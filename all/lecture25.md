#lecture25

##SLIDES

###slide 0
PLOTTING
(download slides and . pyfiles to follow along)
6.100L Lecture 25
Ana Bell

###slide 1
WHY PLOTTING?
Sooner or later, everyone needs to produce 
plots
Helps us visualize data to see trends, pose 
computational questions to probe
If you join 6.100B , you will make extensive use of 
them
For those of you leaving us after next week, this 
is a valuable way to visualize data
Example of leveraging an existing library, 
rather than writing procedures from scratch
Python provides libraries for:
Plotting
Numerical computation
Stochastic computation
Many others
6.100L Lecture 25


###slide 2
MATPLOTLIB
Can import library into computing environment
importmatplotlib.pyplot asplt
Allows code to reference library procedures as  
plt.<processName>
Provides access to existing set of graphing/plotting 
procedures
Today will just show some simple examples; lots of 
additional information available in documentation 
associated with matplotlib
Will see many other examples and details of these ideas if 
you take 6.100B
6.100L Lecture 25


###slide 3
A SIMPLE EXAMPLE
Idea –create different functions of a variable (n), and 
visualize their differences
6.100L Lecture 25


###slide 4
To generate a plot:
plt.plot(<x values>, <y values>)
Arguments are lists (or sequences) of numbers 
Lists must be of the same length
Generates a sequence of <x, y> values on a Cartesian grid
Plotted in order, then connected with lines
Can change iPython console to generate plots in a new 
window through Preferences
Inline in the console
In a new windowPLOTTING THE DATA
6.100L Lecture 25

###slide 5
EXAMPLE
6.100L Lecture 25Note how 
matplotlib 
automatically 
fits plot within 
frame


###slide 6
ORDER OF POINTS MATTERS
Suppose I create a set of values for n and for n2, but in arbitrary 
order
Python plots using the order of the points and connecting 
consecutive points
6.100L Lecture 25


###slide 7
UNORDERED EXAMPLE
6.100L Lecture 25


###slide 8
SCATTER PLOT DOES NOT CONNECT DATA POINTS
6.100L Lecture 25


###slide 9
SHOWING ALL DATA ON ONE PLOT
6.100L Lecture 25


###slide 10
PRODUCING MULTIPLE PLOTS
Let’s graph each one in separate frame/window
Call
plt.figure(<arg>)
Creates a new display with that name if one does not already exist
If a display with that name exists, reopens it for additional processing 
6.100L Lecture 25

###slide 11
EXAMPLE CODE
6.100L Lecture 25

###slide 12
DISPLAY OF quad
6.100L Lecture 25

###slide 13
DISPLAY OF cube
6.100L Lecture 25

###slide 14
DISPLAY OF lin
6.100L Lecture 25


###slide 15
DISPLAY OF expo
6.100L Lecture 25Note how 
matplotlib 
automatically 
scales to fit both 
plots within frame


###slide 16
A “REAL” EXAMPLE
6.100L Lecture 25matplotlib has 
automatically 
selected x and y scales to best fit data


###slide 17
A “REAL” EXAMPLE
6.100L Lecture 25


###slide 18
A “REAL” EXAMPLE
6.100L Lecture 25


###slide 19
A “REAL” EXAMPLE
6.100L Lecture 25


###slide 20
A “REAL” EXAMPLE
6.100L Lecture 25


###slide 21
ADDING GRID LINES
Can toggle grid lines on/off with plt.grid()
6.100L Lecture 25


###slide 22
LET’S ADD ANOTHER CITY
6.100L Lecture 25
)
)

###slide 23
BUT WHERE AM I?
6.100L Lecture 25


###slide 24
LET’S ADD ANOTHER CITY
6.100L Lecture 25


###slide 25
PLOT WITH TWO CURVES
6.100L Lecture 25Note: Python 
picked different colors for each plot; we could specify if we wanted


###slide 26
CONTROL LING PARAMETERS
Suppose we want to control details of the displays
Examples:
Changing color or style of data sets
Changing width of lines or displays
Using subplots
Can provide a “format” argument to plot
“marker”, “line”, “color”
Can skip any of these choices, plot takes default
Order doesn’t matter, as no confusion between symbols
6.100L Lecture 25

###slide 27
CONTROLLING COLOR AND STYLE
6.100L Lecture 25

###slide 28
CONTROLLING COLOR AND STYLE
6.100L Lecture 25


###slide 29
USING KEYWORDS
6.100L Lecture 25

###slide 30
CONTROLLING COLOR AND STYLE
6.100L Lecture 25


###slide 31
Line Style
- solid line
-- dashed line
-. dash dot line
: dotted line
Color Options (plus many more)
b blue
g green
r red
c cyan
m magenta
y yellow
k black
w white
Marker Options (plus many more)
. point
o circle
v triangle down
^ triangle up
* starLINE, COLOR, MARKER OPTIONS
6.100L Lecture 25
whiteyellow


###slide 32
CONTROLLING COLOR AND STYLE
6.100L Lecture 25

###slide 33
WITH MARKERS
Note how actual 
points being plotted are now marked
6.100L Lecture 25


###slide 34
CONTROLLING LINE WIDTH
6.100L Lecture 25

###slide 35
MANY OTHER OPTIONS
Using the linewidth keyword (in pixels)
6.100L Lecture 25


###slide 36
PLOTS WITHIN PLOTS
6.100L Lecture 25

###slide 37
AND THE PLOT THICKENS
6.100L Lecture 25
But this can be 
misleading?  
Y scales are 
different!

###slide 38
PLOTS WITHIN PLOTS
6.100L Lecture 25

###slide 39
AND THE PLOT THICKENS
6.100L Lecture 25

###slide 40
LOTS OF SUBPLOTS
6.100L Lecture 25

###slide 41
AND THE PLOT THICKENS
6.100L Lecture 25


###slide 42
US POPULATION 
EXAMPLE
6.100L Lecture 25

###slide 43
Let’s try plotting some more complicated data
We have provided a file with the US population recorded every 
10 years for four centuries
Would like to use plotting to examine that data
Use plotting to help visualize trends in the data
Use plotting to raise questions that might be tested computationally 
(you’ll see much more of this if you take 6.100B)A MORE INTERESTING EXAMPLE
6.100L Lecture 25


###slide 44
THE INPUT FILE
USPopulation.txt
...
6.100L Lecture 25


###slide 45
PLOTTING THE DATA
6.100L Lecture 25


###slide 46
POPULATION GROWTH
What’s going on in the early years? Impact of WWII
6.100L Lecture 25Impact of Civil WarVisualizing data 
can expose things not easily seen in raw data
Could I visualize this differently?

###slide 47
CHANGING THE SCAL ING
6.100L Lecture 25Log scale means each increment along axis 
corresponds to exponential increase in size; while in normal scale each increment corresponds to linear increase in size 

###slide 48
POPULATION GROWTH
What does linear growth on a 
log scale mean?
6.100L Lecture 25Can now see that there was growth early on, actually at a faster rate than later years

###slide 49
WHICH DO YOU FIND MORE INFORMATIVE?
Visualization can raise questions: for ex. 
by eye, it appears that there are three different exponential growth periodsChanging visualization can help expose trends in data not seen with standard plotting
6.100L Lecture 25

###slide 50
COUNTRY POPULATION 
EXAMPLE
6.100L Lecture 25

###slide 51
THE DATA FILE
countryPops.txt
...
6.100L Lecture 25
Interested in 
analyzing the population numbers. Don’t care about rank, country, or year.

###slide 52
LOADING AND 
PLOTTING THE DATA
6.100L Lecture 25


###slide 53
POPULATION SIZES
6.100L Lecture 25

###slide 54
STRANGE INVESTIGATION: FIRST DIGITS
6.100L Lecture 25


###slide 55
Benford’s Law
𝑃𝑃𝑑𝑑=𝑙𝑙𝑙𝑙𝑙𝑙10(1+1
𝑑𝑑)
6.100L Lecture 25
Many datasets follow this:
# social media followers
Stock values
Grocery prices
Sports stats
Building heights
Taxes paidFREQUENCY OF EACH DIGIT


###slide 56
COMPARING CITIES 
EXAMPLE
6.100L Lecture 25

###slide 57
Let’s use another example to examine how plotting allows us to 
explore data in different ways, and how it provides a valuable way to visualize that data
Won’t be looking at the code in detail
Example data set
Mean daily temperature for each day for 55 years for 21 different US 
cities
Want to explore variations across years, and across citiesAN EXTENDED EXAMPLE
6.100L Lecture 25


###slide 58
THE DATA FILE
temperatures.csv
...
6.100L Lecture 25


###slide 59
EXTRACTING DATA
6.100L Lecture 25This will return a list of temperatures (in F) and a 
corresponding list of dates for a specific city
File stores data as str, 
need to converttemperatures.csv
CITY ,TEMP ,DATE
SEATTLE,3.1,19610101SEATTLE,0.55,19610102SEATTLE,0,19610103SEATTLE,4.45,19610104
Only want temp 
for a specific city

###slide 60
AVERAGE TEMPERATURES
Just plotting points 
as a scatter plot (no 
connecting  lines)
Getlist of cities
6.100L Lecture 25
Using first two 
characters as 
labelCompute 
average 
temperatureThis will calculate the average temp over every day for 55 years, for every city.

###slide 61
AND THE TEMPERATURE IS …
6.100L Lecture 25Detroit, Chicago, 
BostonSan Juan, Miami, Phoenix

###slide 62
BUT MORE INTERESTING TO LOOK 
AT CHANGE OVER TIME
6.100L Lecture 25
Previous 
code
Get temp data for yearCheck that entry is for right yearFor one city, calculate the average temperature over each year. 

###slide 63
BUT MORE INTERESTING TO LOOK 
AT CHANGE OVER TIME
6.100L Lecture 25Pick some cities to plot 55 temps (avg temp over each year)

###slide 64
BABY IT’S COLD OUTSIDE!
6.100L Lecture 25

###slide 65
BUT WHAT IS VARIATION?
high, low, avg temps by year
6.100L Lecture 25

###slide 66
BUT WHAT IS VARIATION?
high, low, avg temps by year
6.100L Lecture 25

###slide 67
Can see range for each city
Not helpful for comparison between cities
Y axis for Boston is 0 to 80
Y axis for Miami is 40 to 90
Y axis for San Diego is 50 to 90SOME CITY EXAMPLES
6.100L Lecture 25

###slide 68
USE SAME Y RANGE FOR ALL PLOTS
6.100L Lecture 25Fix the 
display range for y axis

###slide 69
One reason to plot is to visualize data
Can see that range of variation is quite different for Boston, 
compared to Miami or San Diego
Can also see that mean for Miami much closer to max than min. Different from Boston and San DiegoBETTER CITY COMPARISON
6.100L Lecture 25

###slide 70
HOW MANY DAYS AT A TEMP in 1961?
6.100L Lecture 25Count number of 
days of a particular year for which a specific temperature was the daily average
Create a list of temperatures for a specific yearSet up a list of 100 elements, making a histogram -like structure.
•Index 0 stores how many days had a temp of 0
•Index 1 stores how many days had a temp of 1
… 
•Index 99 stores how many days had a temp of 99. 

###slide 71
HOW MANY DAYS AT A TEMP IN 1961?
6.100L Lecture 25

###slide 72
SAN DIEGO IS BORING?
6.100L Lecture 25
Could we fit a curve to parts of this data?
Uniform? Gaussian (aka bell)?

###slide 73
CHANGE OVER TIME?
6.100L Lecture 25Plot two distributions, one for 1961 and one for 2015

###slide 74
OVERLAY BAR CHARTS
6.100L Lecture 25

###slide 75
OR CAN PLOT SEPARATELY
6.100L Lecture 25

###slide 76
CAN CONTROL LOTS OF OTHER THINGS
Size of
Markers
Lines
Title
Labels
x and y ticks
Scales of both axes
Subplots
Text boxes
Kind of plot
Scatter plots
Bar plots
Histograms
…Scratch edthe surface today !
6.100L Lecture 25

##TRANSCRIPT

PLOTTING WHY PLOTTING? MATPLOTLIB Can import library into computing environment A SIMPLE EXAMPLE PLOTTING THE DATA EXAMPLE ORDER OF POINTS MATTERS SCATTER PLOT DOES NOT CONNECT DATA POINTS SHOWING ALL DATA ON ONE PLOT PRODUCING MULTIPLE PLOTS EXAMPLE CODE DISPLAY OF cube DISPLAY OF expo A "REAL" EXAMPLE LET'S ADD ANOTHER CITY LET'S ANOTHER # Add LabeLs and title plt.title( 'Ave. Temperatures'… PLOT WITH TWO CURVES CONTROLLING COLOR AND STYLE USING KEYWORDS LINE, COLOR, MARKER OPTIONS LOTS OF SUBPLOTS AND THE PLOT THICKENS US POPULATION EXAMPLE A MORE INTERESTING EXAMPLE THE INPUT FILE POPULATION GROWTH CHANGING THE SCALING WHICH DO YOU FIND MORE INFORMATIVE? THE DATA FILE STRANGE INVESTIGATION: FIRST DIGITS FREQUENCY OF EACH DIGIT COMPARING CITIES EXAMPLE AN EXTENDED EXAMPLE DATA FILE EXTRACTING DATA AVERAGE TEMPERATURES AND THE TEMPERATURE IS BUT MORE INTERESTING TO LOOK AT CHANGE OVER TIME BABY IT'S COLD OUTSIDE! BUT WHAT IS VARIATION? high, low, avg temps by year SOME CITY EXAMPLES BETTER CITY COMPARISON HOW MANY DAYS AT A TEMP in 1961? SAN DIEGO IS BORING? CHANGE OVER TIME? OVERLAY BAR CHARTS OR CAN PLOT SEPARATELY CAN CONTROL LOTS OF OTHER THINGS All right. So let's begin today's lecture. We have only two lectures left. This this one. And next Monday, I realize that there are no more deliverables for this class, right? No more quizzes after tonight. No more presents. So I do appreciate you coming to these lectures. They're intended to be a little bit more fun. You know, no need to take notes, just kind of sit back and enjoy the content. Today we're going to be talking about library in Python that can help you do plotting. And the reason why we talk about this plotting library as opposed to something else that's maybe more machine learning or something else like that is because at one point or another, if you decide to take any other course that kind of builds upon this internal course, you'll probably want to create some graphs or visualize something, right? Even if you do a Europe, you'll probably have to visualize some sort of data. And it's a really nice next step to show you how to use a library that already exists. So somebody already put in the work in creating this library that can plot things for us. So let's just try to use it. And so it's just a really, really nice way for us to to kind of wrap up the course by showing this visualization library. So we're going to the library, we're going to do two uses called Matt Plot Lib. And it's kind of the most basic plotting visualization library that we can have. And the way that we bring it into our code, just like we have in the past few lectures, is this is with this import statement and the actual file that comes into our into our that we would bring into our program is called Map Plot, Live Dot Pi plot. Now that's kind of a mouthful. And a lot of times when we want to use this or when we want to use this library, you'd have to basically say, Matt, plot lib pi, plot dot function name from that file. And so that's a lot of writing and a lot of typing. So when we bring it into our when we bring in this library into our own file, we can actually rename it. So as Peel T tells Python that now I would like to refer to this file and this library as the name Potti. So if we ever want to call functions or maybe objects and things like that from this file, we would do it using Potti Dot and then the name of whatever we want to use. So it's just a much nicer way to grab the contents of the file instead of always writing. Matt Plot led by plot dot something else? Yeah. You can think of it as a variable name. It's it's anything you want it to be so you can import it map plot lib pipe plot as Anna. And then from there on you can say Anna dot in a process, name or plot or whatever it is. So it's just whatever name you want to get. Okay. So there are other visualization libraries that exist out there. A lot of them or all of them build upon this one. So this is kind of the most basic library that you can get. And the other ones that exist build upon it by kind of doing some things behind the scenes to maybe make your lives easier or to do some really cool visualizations or maybe things where you can like hover the mouse over a coordinate and things like that. But we don't need to do any of that. At this time, it's just nice to take a look at this really basic visualization library. So throughout throughout the lecture, we're going to look a little bit at some code. We're going to run it on the python just from a python file. Then we'll just talk about it on the slides. So whenever we're plotting things, we need to tell Python a set of X values and a set of Y values. That's pretty common. If you've used MATLAB, you'll you'll know that that's kind of the way it's done. Same and Python. So when we're creating the coordinates that we'd like to plot in a 2D plane, we're essentially just creating two lists where index by index, we're going to have a list containing all the values that we want for the X coordinate and a list and in a separate list, all the values that we'd like for the Y coordinate. So at index zero, in each of these lists, you're basically creating X values at index zero Y values and index zero becomes the coordinate one coordinate point. So one of the very simplest things that we can do is we can create a nice list of values that will be our x. X values. So our x axis will basically be the number zero through 29. And then down here we can create four different lists containing four different y y value ports. So when we're plotting, we're going to plot this X value list against all these linear points, this x value list against all these quadratic points on this X value list against the cubic points and so on. So the way we're creating these lists are pretty familiar a python syntax. Our end is going through 0 to 29, and then we're appending to the end of each one of these lists linear, quadratic, cubic and exponential, some function of that, right? So the linear list will just have all the values again. So we're plotting 0011, two, two. So on the quadratic list will be plotting 00112, four, three, nine and so on. Same with the cubic and then this exponential. I just chose randomly 1.5 to the power of one just because it kind of looked nice in the plot. But you can imagine a different number for the exponential in there. So the way we plot sum some values is by not surprisingly, the plot command. So plot was how we decided to import that library as the name that we gave it. Dot plot tells Python we'd like to plot some list of x and y values. So the parameters of the plot command are going to be two sequences of values. They can be lists typically, but they could also be tuples. They could also be, you know, the keys you get from a dictionary that was also an iterable, things like that. So we have to pass in a list of of numerical things. So this will be typically the stuff on your x axis. And the second parameter is going to be the function of those values of the x axis. The lists have to be the same length, obviously. So Python knows which coordinates we're plotting. If they're not the same length by accident, then Python will throw an error and then you don't. You know, it. It just won't plot. So when we run the code, Python will generally plot the values in either a new window or directly in line in the console. So right over here. So right in here, it could put the plot directly, sort of in line with a bunch of stuff that you might print out to toggle between that. Just out of curiosity, you go to tools preferences, I Python console graphics and then here you can choose either automatic which will make a new window for us that's interactive. You can zoom in and out things like that or inline, which will just put the plot that that you tell Python to generate directly in the console here. Okay. So I prefer the new window because it's easier for me to interact with it. So we'll do that. So let's actually run one of the plot commands. So pretty the plot where we're plotting here, the x axis, the x axis as just the number zero through 29. And the y axis is just going to also be the value zero 329. So we've made a nice little linear plot and you notice it popped up a little window down here for me. And this is the plot that it generated. Okay. Not surprising. This is exactly what we expected out of it, right? Okay. So what do we notice about that plot? We notice how Python nicely fit the line within this frame. Right? So it added a little bit of wiggle room to the left and to the right of my line and to the below and above my line, just so it fits nicely within the frame. It didn't zoom out to some standard, you know, 0 to 100 value. It zoomed in to this 0 to 30 ish range, 0 to 30 ish on the Y axis range. So really, really nice that it did all that for us. The order of the points does matter in the list. So you'll notice one of the other things in this in this plot here is we gave it actual points that it needed to plot, but the plot command doesn't plot the points by default. Instead, it just connects all the points by line. So it connects consecutive indices of points by a line so connected the 001 1 to 2 and so on. So the order of the points does actually matter if if we have a function. For example in this case and squared, right. So now being zero 329 and squared being 01240149 and so on. But they're in our but they're out of order. Python will just take consecutive pairs from those lists and connect them with a line. So here's an example. I've got my lists, my X values list is this test samples. It's all the numbers zero through 29, but out of order and the test values associated with each one of those, again, they are correct. This is zero squared, this 25 is five squared, this nine is three squared, but they're out of order. So if we run that. Just with a pure plot command. We're going to get some garbage. But right. It doesn't look very nice. And we already know what's wrong, right? Python just connected. 005 25 and then three nine by a line. Not really. Very nice. Instead, what we'd like to do is to just tell Python to plot the points. So I don't care about connecting them with a line. In this case, I would tell Python instead of just plotting it to create a scatterplot for me. So plot dot scatter with the same list of x and y values is going to just create for me this nice plot where it plots the coordinates. Doesn't matter that they're out of order because they just get plotted without anything connecting. It's a pretty nice. So that's, you know, this example that we just did here. And then this is us doing a scatterplot, giving us this nice book. Okay. One of the other things that you might want to do is to have a whole bunch of lines being plotted on one window. Right. So to do that, all you have to tell Python is just a sequence of all the commands, all the plotting commands or everything that you'd like to plot on the one finger. So without telling Python, you'd like to create a new figure. Any time it sees a plot command, it will just keep adding whatever points get generated or whatever lines get generated to the current figure that's open. So we just have one thing that's open right now, so it'll just keep adding stuff to our figure. So here I've got four plodding commands in a row. I never explicitly told Python to create a new figure for me, so it's just going to add all four of these lines to the same plot. So it just doesn't create a new figure. It just keeps adding stuff to my plot. So you can imagine if I added a scatterplot as well, it would just add the individual dots to this plot. Okay. So, again, what do we notice? Well. Python nicely framed everything for me, right? To make sure that every line that I have fits within this this graph. So my x axis is comfortably between zero and 30, and my y axis is also comfortably between zero and 120,000. So there's a little bit of gap up at that top of the of that exponential line. But this leads us if we were presented this graph to kind of mistakenly. Not knowing what's going on with these bottom lines here. Right. So this is our linear the blue line and the orange one is the quadratic. We're not really sure what's going on down there. Right. Because the scales are just it is just is just the y scale is just too high. So in this particular case, it would be better to visualize the data in in separate, different windows. Right. So instead of having everything be plotted in one window, we're going to tell Python to create a new window and plot some stuff in it. So the way we tell Python to create a new window for us is with the command plot dot figure. Okay. So as soon as Python sees peeled dot figure, it will create a new window, bring it to the foreground, and any further plot and commands will be added to this new figure. So there's a parameter that this figure can take. And that's going to be the name of the figure. So, you know, like when you have a window at the top, there's has a name for like the name of the program or whatever is running. Well, the string that you put in there is going to be the name that you give to that figure. If. Python doesn't have a figure with that name already there. It creates a new figure, brings it to the foreground. But if there's a figure with that name already there and you just happen to appeal to that figure with that same name, it'll just re bring that, that, that window up to the foreground again to re add more stuff to it. So we're going to look at this this example here. We've got a whole bunch of stuff being plotted. So the first two lines of code here, first we've got a new figure being created and we called it Expo. And then this plot command here coming up right after the figure, we'll add this exponential that we created to that expo figure. Then we've got a pretty dark figure right after that. So Python will bring this new figure to the foreground and the plot command that comes right after that will add the linear line to this new figure that we called in. A couple more times we're going to create do the same thing to create this quad and this cube, and those will each get one line added to them. And then down here we're going to say, well, let me just go back to that exponential figure and add another different exponential curve to it. So we're going to create the exponential curve this time 1.6 to the power of AI instead of 1.5 to the power of AI. Then we're going to tell Python to bring the figure called XPO back up to the foreground. So remember we created it up here so it doesn't create a new figure. It'll just bring that one back up and it already has a curve in it. And then we're going to tell Python to plot a second curve to it. Okay. So let's see that. That's all this code right here. Run it. Okay. So not just one figure, one one window got created, but four. So this is my cube. And you can see up in the top here, a little hard to see, but that's the name that we gave it. This is my quad. This is my lin, my linear. And this is my exponential. Right? So we see the exponential one was has two lines in it because we added one way at the beginning and then we brought it back for processing to add another line to it. Okay. So again, just so you know, this these these graphs are actually in slide. This is the quad one. This is the cube one. This is linear one, and this is the exponential one. The blue line was our original curve 1.5 to the power of X and the orange one is 1.6 to the POWERPACKS. So they both got added to the same plot. So again, just something to note. You'll see how Python nicely framed our line so that it's able to fit everything that it needs to plot within this graph. Okay. So what we're going to do next. I know that was a little bit tedious, but we're going to do next is we're start looking at some real exam, some real world data. So first, we're going to do some toy real world data, and then soon we're going to start dealing with some some actual data sets that we're going to read in, we're going to plot, we're going to investigate, try to answer some questions about them and things like that. So first, let's look at this real life example where we've got months and temperatures for each of those months. So notice the months here is actually this, this, this of the value that this range returns, which is like an iterable, like a tuple. So it's still a sequence of values. It's not a list, but totally fine to be passed in as, as an argument to the plot. And temps, of course, are going to be temperatures corresponding to each of those months as a list. Okay. So the plot looks something like this. If we actually run that code. What do we notice? Well, just like before, map plot nicely framed our data. Right. It's got a little bit of wiggle room, left and right, top and bottom, and it automatically selected the scales. Right. How low to go? How high to go. And the tick marks for this. But let's say that you you know, you're the advisor to a student and they came to you with a plot that looked like this. Would you be able to tell anything about this plot? Right. Without knowing exactly what the code that generated this plot is? Not really right. It just looks like a bomb. It could be any sort of data. So what we'd like to do before actually, you know, for Europe and things like that in the future, before presenting a plot to somebody else, you'll want to add a title and you'll want to label your axes. Right. So what we want to do, in addition to actually plotting the data, is to tell Python to add for us a title and labels for our axes. So we do this using these three lines of code here. So since it's we haven't told Python to create a new figure or anything like that, anything any commands that we do with regards to plotting will just get added on to this figure. So here I've got Python adding this, this title, these two labels to our axis, to our axes. So here, I've got this. And it's blocked. So I run it. And today we have something that looks much nicer. So now we can hand this plot to somebody and they'll know what it's about. Now, that's fine. But since it's temperatures, what I'd really like to do is to say, well, the temperature, the lowest temperature I have should really start at the Y axis here. This intersect with the Y axis and the highest temperature I've got. I don't really want that wiggle room because this is my last temperature value. Let's just have the frame, just end there so we can do that little change by setting limits on our x axis. So here I'm going to limit the x axis to say that it starts from one and ends at 12. So if I do that again, that's just a little command we put in continuation with the rest of the commands and it gets applied to this plot. So as soon as I do, that Python now creates for me the same plot, except that the y, the the x axis starts at one and ends at 12. Nicely framed within here. Right. So no more wiggle room. Okay. Still some improvements to be made to this plot as in here the months skip right so python decided that it's it's you know it's best to just show 2468 1012 as the ticks on the x axis. But I decide that I would since I'm decided, since I'm showing all the months of the year and their temperatures, I would really like to have ticks for every single month. Right. So again, a little command will do that for us. So Plot X ticks takes in a tuple of all of the places where you'd like one of those little ticks to be created. Okay. So if we do that again, just another little command in in series here. If we do that, python now fills in the ticks for every single spot that we told it to fill it. Right. So it's looking way better already, right? But still not quite right. I promise this will be the last improvement we make. I personally find it hard to map numbers to the months. I still count my fingers. So what would be nice is to say, well, instead of having numbers on my x axis, I would like to have the actual names of my months right Jan Fab Ma and so on. So to do that, we're going to make one small change to our X Ticks Command here. We're going to give it a second parameter. So first one is, of course, what we had before saying these are all the ticks that I would like to have. And the second parameter is the labels for each one of those ticks. So one by one they'll be mapped. So one will be mapped to Jan two, map to Fab and so on. So instead of using the numerical values Python will create for us, the. The the string values that I've told it to do. All right. So here it is. Run creates for me this nice, very nice looking plot. So this I would be happy to receive as an advisor compared to that very first one that we had. All right. Questions so far seem all right. Okay. Okay. The other thing that you can do is potentially add grid lines if you wanted to. So appeal to dot grid will either toggle the grid lines on and off. So if there's already grid grid lines, it'll toggle them off when it sees that command. If there are no grid lines, it'll toggle them on. So you could potentially have a bunch of grid commands that keep toggling things on and off. And so. Okay. So that was us plotting one tempered, one city's temperature values for a year, let's say an average. Let's say that we wanted to plot two different cities. Okay. The code to do that is as follows. So again, we've got months being this range one through 12 inclusive. I've got a list of all the Boston temperatures here. I plot that. I list of all the Phenix temperatures here and I plot that. And of course, I'm going to add some labels to my to my graph. So. That. So if I run that. We get something that looks like this. Now, of course, I could kind of remove that little those little wiggle rooms on the left and right, but for now, it's fine. What's missing from this plot? Let's say you didn't see the code and you were just given this plot. Yeah, exactly. I don't know what like. Yes, these are different temperatures from the title and the and the labels, but you don't know which city is which exactly. So what we'd like to do is tell Python how to label these two lines. Right. So to do that, it's just an extra parameter here in the plot command. So when you tell it which data to to plot, you can also tell it what label that data should get. So here I've got Boston label for the first one, Phenix label for the second one, and then you tell Python to add a legend to your plot. So here the parameter is the location for the legend. And best just means Python should decide where to put the legend. Top left, top right, middle, wherever. So it doesn't really interfere much with the with the data. Or you can just tell it where to put that legend, right? So you can force the legend to be in a particular spot. So here I've got already labeled data and then we add the legend. And now you can see in this particular case it decided to put it in the top right. But again, you could force it to go somewhere else. Bottom, middle seemed like a fine choice as well. Okay. Very nice. So now we've got a python. You know, it automatically did the X and Y axes for us as we told it to do, but the colors that it picked were random. Now we can specify a bunch of different details for the plot. So we're going to do that next, just to show you that you can. So we're going to choose different colors and different styles for our plots. We're going to choose different widths for our for our lines. And then maybe we can and then we'll also add some markers where exactly each data point we have we're going to mark and then I'll show you how you can create subplots. So instead of creating new windows, you can actually have one window with different little subplots with it. Okay. So the first thing we're going to see is how to customize the data to have a certain line style and a certain color. So there's a shorthand notation to do this instead of actually passing in the parameter name in the plot command, we could do it shorthand notation. So you might have already noticed this little extra bit here. So. More you use it, the more you'll get used to it. But this basically tells Python that I would like this plot, this line corresponding to this data to be blue. That's what the B stands for and to be a solid line. That's what that little dash means. But Phenix, one, you may have guessed, tells Python that I would like this one to be red or for red and to be a dashed line. And then the last one, I'm going to add one more temperature here. Temperature data for Minneapolis. I would like this one to be green and a dash dot dash dog line. Okay. So we can run that. And it looks something like this. All right. So I got my solid blue line for Boston, my dash line for Phenix, and my dashed out dashed out line for Minneapolis. Very nice. Now, instead of doing that shorthand notation where we've got this one parameter that just somehow magically knows the color and the style based on just being passed in, we can actually tell Python the parameter values that it should that correspond to the color. So here I've got color equals B for blue and then the correspond to the line style. So here line style equals and then you explicitly pass in the line cell that you'd like. So this may be more or more intuitive according to what we've learned, but Python does allow you the option to kind of do it all in one. So if we do if we run with this with these specific, explicit parameters, then we'll get the exact same graph as before. I feel suppressed. Okay. So there's a lot of options that we can have here. So these are all the lifestyle options. So you can also add a dotted line, which I didn't show. These are all the color options, plus many more. You could also pass in the RGV values, or maybe the hex values if you want a very specific shade of magenta or something. And then we can also add markers to our to our lines. We haven't seen this yet, but let's do that next. So let's say that I would like to have the actual data points that I that I've plotted show up in my lines. Right? Right now the lines just get connected or the data points just get connected with our lines dashed or dotted or whatever we chose. But the marker, the data points themselves don't show up with markers. So again, in shorthand notation we can tell Python, hey, let's add these markers. So here I'm telling Python to just do a dot for this blue solid line here. I'm telling Python to do a larger dot for this red dashed line. And here I'm telling it to do a star for the green dash dot dash top line. All right, so that's down here. Run it. And we see nice little markers for every one of our data points. Right. So we can also do triangles, we could do squares. There's lots of other marker options and they're all exist in the documentation for map plot loop. Okay. So this is what we got. Perfect. The last thing that we can do is to add thickness to our lines. So oftentimes it's good to, first of all, delineate the lines using, you know, dashes or dots and things like that, but also width. So here, another parameter passed in the line with this is going to be a skinny line. This is going to be maybe a thicker line and this one's going to be unreasonably thick. So let's see exactly what this will look like. It's going to look super weird. As I said, unreasonably thick line. But there it is. And then you can see that the legend itself also adjusted to whatever you chose for your. Your line starts right. Okay. Uh, so that's exactly what I said. Go. Last thing I want to talk about is subplots. So right now, the only things that we've kind of learned about plotting is you either plot every line that you have on one figure or you create a new figure and then it becomes a new window that you have to kind of switch between for whatever you'd like to plot. Oftentimes what's really nice to do is to create only one figure. So you have one one only one thing that pops up, right? Like one window. And within that window with some name here. Right. And within that window, you can create a bunch of different subplots. So here I've created, you know, six different subplots. So we can tell that to Python and we do that using the subplot command. So in this particular case, I've told Python to create for me a subplot with two rows. That's what the first parameter says. And one column, that's what the second parameter says. So here, this is one window with two two positions within it. The third parameter tells Python which one of these positions to open for adding lines to or data to. Right. So one means this is the one that you're opening. And two means this is the second one that you're opening. So you can see here the very top subplot. Command tells Python to open up this one for four for editing, basically. So we're going to add to it the Boston temperature. So this is all the plot and commands and all the labels and everything after it belonged to this top subplot here. And then subplot command down here tells Python that on this figure with two rows and one column, I would like to now open position number two for editing and then everything that I have thereafter gets added to the subplot of this position. So the way that this is going to look is as follows. So I've got these this is just one window that gets created. And you can see the top one has the Boston temperature and the bottom one has the Phenix temperature. At first glance does this look right in terms of temperatures? Like if you're just to look at the pictures themselves. I don't know about you, but I at first glance, I thought that the temperatures for Boston and Phenix were the same because I didn't look closely at the Y axis. Right. It kind of looked like, hey, they both bottom out in the same way. They both top out in the same way. So they look very similar to me. But if we inspect the y axis closer, we see that the Boston temperature starts at 30, goes to 70, but the Phenix one starts up, you know, what is this, 50 and goes to 90. So if we're presenting plots in one figure, what would be really nice to do is to make sure that the axes are both bounded in a similar way, especially if we're plotting similar data. Right. Temperature in this particular case. So in our in our code, what we'd also like to do is set limits on our axes and just the Y axis, because the x axis is the same. Right? So here I can limit the x, the Y axis from 0 to 100. I can do a reasonable set of temperatures in Fahrenheit. Right. So if I fix these temperature or temperature limits from 0 to 100 and now I plot, I get something that looks like this. And now, at first glance, this makes a lot more sense to me. Right. I've got the Phenix. Temperatures now seem to be on for this, you know, for this year on average, higher than the Boston temperatures. Okay. So we can plot now multiple we can create multiple subplots. So here, you know, in the previous example, I just had two top and bottom, but I can create as many subplots as I'd like within my window. So when I create them and I and I tell Python how many rows and columns I have in this particular example I just drew here, I have three rows, right, and two columns. So the third parameter that I pass in, well, basically tell Python which one of these subplots to open up for for processing. So this will be the first one. This will be the second one, kind of the way we read third, fourth, fifth and sixth. So that third parameter to these subplot commands will be either one, two, three, four, five or six telling Python which one of these sections I'm going to add plots. In this particular case, I had a Boston Phenix and Minneapolis temperature, so I'm just creating a two by two matrix, right? So here I just have this thing that looks like this, a figure with these four subplots. And I am going to add the Boston one over here, the Phenix one over here, and then the Minneapolis down here. Right? So one, two and three, as my subplot that subplots that I'm opening nothing in for. So that fourth spot will just be empty. So the plots will look something like this. And I haven't changed the line widths in this particular case. I didn't need to write. And you can see everything's plotted with the heights again, limited from 0 to 100, just so everything's comparable. And notice the empty spot here because I had nothing to fill in. Questions about this this interesting. Okay. All right. So that finishes up just some really basic things that we can do with plodding, basic, you know, customizations. Now, what I'd like to do is just open up a few different data sets for for processing. We can start by just plotting the pure values on a regular plot, and then we can start to investigate things that we visualize. Ask more questions and see where we go from there. So the first thing I'd like to do is open up a file on the US population. So this particular file contains 40 different numbers. So it has a population value over about 400 years, every ten years, right. So that's 40 different values for the temperatures starting from, I don't know, from a really long time ago till about 2010 or something like that. So the file looks something like this. So it starts at 1610 and goes down to 2010. So this is 40 lines for 40 years. 4400 years every ten years. Then there's a space in the file and then I've got the population value. Okay. So starts at 350 and creases goes down to 300,000 in 2010. So that's what the file looks like. It's important to know what the file looks like because you're going to have to read in this value this data and save it in some sort of data structure that's easy to manipulate. So in our case, a data structure that's really easy to manipulate where you have a whole sequence of values is a list, right? So what we can do is we can open up this file for processing read in the years as a list and then reading the the population values as a list as well. We could use a dictionary also if we wanted to, but in this case I just used two lists. So let's look at the code to do that. It looks like a lot, but I'll kind of go through it. So here is the function that's going to read in the file. It just opens up the file, creates two empty lists. One contain will contain the dates, the other one contain the populations. It iterates through each line in the file. So I've put up what a line in the file kind of looks like up here. So it's got some numbers, space, some other number. But when we read in file, when we read in a line from a file, Python actually reads it as a string. So what that means for us is we're going to have to take this string, each line being the string 1640 space to six, comma, 634, something like that, and somehow separate it so that we have the date and then the number right of the population and then somehow save those two pieces to list. So the first thing to notice is that we have a pesky comma in our population values, right? Those values are human readable, so it makes it easy for us to read. But the the computer is not so happy about them. Right. So if I have a number like, you know, 11,345, whatever, this is written as a string, right? And if I just try to cast that as an integer just straight without doing any sort of processing on it, python's very unhappy, right? So what we need to do is remove that comma, because as long as I don't have a comma there, Python can convert that. Not that you know that that string number into a regular integer number for us to then plot. Okay. So that's what this bit of the code is doing. It's doing it in kind of a weird, weird way. It's saying, hey, take this entire line of characters and only keep characters that are either a digit or a space. So in doing so, it effectively removes the comma because it creates a new version of that line containing only digits and spaces. So it'll just take the two six and then the six three for right after, right? So it just creates this new line that looks like that. And then after it has this new line, we're going to split on the space because we note that every single after every date, every year, we've got a space that separates our population value in our date. So if we split on the space using the split command, the thing before the space. So the line at index zero gives us the date. We'll just cast that to an end and upend it to date. And then the line at index one is the thing after the space again without the comma, because we did that trick and then we cast that to an integer and append that to our population value. Okay. That's what we do there and that's what we do there. And then from there on out, we just return the dates and the populations. The dates become my x value, x values for my plot and the populations become the Y values for my plot. Okay. And then we plot it and it looks something like this. So much easier to read, to tell or to tell what's going on with than just looking at pure numbers. Right. Always nicer to visualize things than to just read a whole bunch of numbers, even if it's just 40. And in fact, we can tell a couple of things that we weren't able to tell. You know, we definitely couldn't have been able to tell from just looking up your numbers. The first is that we notice a little bump right here, right in the population. And this is the impact of World War Two on the population. Second, a little harder to tell is another little bump down here. And that's the impact of the civil war on the population. Okay, so nicer to visualize. It exposes some interesting things. The other thing to notice is, well, what's going on down here? It kind of looks like the population is not really growing much. Right. And then maybe from 1750 onward, it starts to grow exponentially. It's hard to tell what exactly is going on in that lower part. So let's think about a different way of showing this data. Instead of having a linear scale on our y axis, let's see about doing it in a logarithmic scale. Right. So we're going to add a command that tells Python to make our y axis a log x logarithmic scale instead of linear. Okay. So if we do that, then that means that every note, every regular increment in our Y on our y axis is going to imply an exponential increase in the population. Right. Okay. So let's plot that. And if we plot that, we get something that looks like this. The x axis remains unchanged. We're still incrementing the years linearly. Right. But the y axis is now logarithmic. So what do we notice? Well, I see linear, linear line here and I see another line here. Again, linear growth on a large scale means exponential growth, right, on a linear scale. So what we noticed is that there's sort of these two time periods of exponential growth and in fact, those early years actually seem to be growing. The population seems to be growing at a faster rate than the later years. Right. And that was not readily visible on the previous graph that we have. So the question, you know, I have a question for you. Which one of those did you find more informative? Well, it kind of depends on what we're interested in finding out, right. If we're interested in sort of big trends in the data where, you know, in the top left one we spotted here the impact of wars on the population. Well, then the top left one is the one to look at. But if we visualize the data in a slightly different way, it gives us different insights into what's happened to the population. Right? That wasn't as apparent in the previous graph. So it really kind of just depends on what you're interested in finding and finding out which one of these plots you find more important, informative and you know, sometimes both are probably necessary to figure out exactly what happened. Okay. So that finishes our example on the US population. Now let's look at a slightly different file. This particular file we're going to look at country populations. So these are the populations in a whole bunch of different countries. Ah, sorry. All the countries are ordered from countries with the highest population up at the top of the file, down to the countries with the lowest population at the bottom of the file. So they're basically ranked in this order. Right. So I know that this order is correct. So there's 237 lines in this file. What do we notice about the data? So we need to know what the data looks like in order to read the file in. And again, we're going to be interested in kind of extracting certain parts of it for the particular analysis I'm going to do next. I'm actually only interested in the population itself, so I don't care about the rank and I don't actually care about the country either. Okay. So all that might the code that's going to read in the file will only be interested in extracting the population value. And notice once again, we've got our commas here in the population values, right? So we're going to use the same trick to get rid of those. Again, nice human readable format here, but not so good for reading in the file and dealing with with the data. So. Right, so we're going to have to take care of that when we read in. So here's the part of the function that reads in the file. It's going to have a very similar feel to the previous one. Again, I've got a little sample of our file up here just to remind ourselves what it looks like. So this particular file, I'm only interested in grabbing the population value and it's actually a tab separated file. So I've got, you know, rank tab, country tab, population tab and then the date. So when I take a line of code, what I'm first going to do is split it on the tab character and the tab character is this backslash t thing. So once I split it on the tab character, the thing I didn't do zero is by rank. The thing at index one is my country and the thing at index two is my population. The thing and index three is my date. So if I'm only interested in growing the population, I'm going to look at the thing at index two and this gives me this the population as a string here. And then we do the exact same trick as before to eliminate the comma. There's no space in this particular case, right? Because I've just got the number saved because of my tab split. So all I need to do is keep digits. And then if I keep the digits, then I'm just going to keep that number as a population. Again, I cast it to an integer because I would like to work with numbers in my lists as opposed to strings. That would be very weird. And at the end of this function, I've got all of the populations in the same order that they were in that file read as a list numbers, not strings. And so if we plot the populations, just pure populations, I'm going to have something like this. All right. If I plot just the pure populations, I see something that looks like this. Kind of hard to tell. I mean, it's a big exponential decrease, but is that really what it is? So again, we'll do a little semi log plot on the Y axis to see exactly if there's, you know, any sort of linear action going on on that log plot. And, you know, unsurprisingly, you know, it kind of matches our intuition. There are very few countries that have a really high population. There are very few countries that have a low population. And then a bunch of countries that are kind of in the middle here where the population just exponentially decreases. All right. But that's not the analysis I would like to do on this on this data, because that's kind of boring. So instead, what we're going to analyze is actually just the first digits from every country's population. Right. So what I'd like to do from that data set is once I'm grabbed a list of all of the country populations, I am going to extract that first digit. So the way we do it is we know if we have a population, I don't know, two, five, 4 to 1, three, six, whatever. I'm going to take this number, cast it to a string. That's what this one line of code is doing all in one. It cast it to a string. Extracts the element, an index zero. This becomes the string two. And then we cast that to an integer. Right, to give us two. So that line of code does all of those steps in order. So at the end of this loop, I've got this first digits list that contains all of the first digits of every single one of those country populations. So I'll print that for you just to give you a sense of what it looks like. So we see this, right? So we had two countries up at the top that had 1 billion people, 1 billion people. Then the next country down, we had 300 million people, then 200 million, then 200 million, then 200 million, 100 million and so on. Right. So just extracting that first digit, we see this kind of this pattern of values. Okay. So if we plot that. So that's exactly what we do down here and I'll just do it in the slides. If we plot that list in that order, we get a plot that looks something like this, right? It's a nice little sawtooth pattern. Right. And if we stare at it a bit, it makes sense because the numbers that we got right from the file were already in ranked order, highest population to the lowest population. So here down here we had sorry, down here, this little dot right here had two countries out there that were 1 billion, so one one and then had one country that had 300 million and then it had three countries that had 200 million. Then a bunch of countries that had 100 million something. So 111, one, one, one one. And then since we're going in decreasing order in terms of rank, right, once we finished going to that significant digit when we moved down, then we're going to start looking at countries that have, you know, 90 million, 90 million, 90 million, 80,000,080 million, so on. So just the order of all of these values, the first digits of every one of these values, it makes sense to have that sawtooth pattern. Right? We basically have, you know, nine, eight, seven, six, five, four, three, 21987, six, five, four, three, two, one. And so. Right. So we get this pattern. What I'd like to do is ask how many how many countries have their first digit a one. It seems like there's a lot, right, if we count sort of how many of these countries are down here? It seems to be a lot. How many countries have a first digit of two? So again, we count how many countries are on the step of my sawtooth? How many countries have the first digit? Three and so on. And it kind of looks like, I don't know, maybe there are more countries that have a first digit of one. Then there are countries that have a first digit of nine. Right. There's only a couple here. Maybe like five here, maybe one here, a couple here, a couple here. Where is the number of countries that have a one are actually a lot. So let's try to plot this data. The values here. So what I'm interested in doing is creating a histogram. So a histogram on the x axis has a bunch of bins. In this particular case, what the way I'd like to bin my data is by saying my bins are going to be the digits. One, two, three, four, five, six, seven, eight and nine. That's the x axis. And the Y axis is going to be a count frequency of how many of my countries have the number one as their first digit. How many countries have the number two as my first digit and so on. So in terms of this list containing all of the first digits in the of the countries, I'm essentially have I essentially have one bin that counts how many ones I have in this list. Another bin that counts, how many twos I have in this list. Another bin that counts, how many threes I have in this list and so on. Okay. So if I plot that histogram, it looks like this. Now. I would have expected this histogram to be about even. Right? Like, why does it matter? The first digit? It seems like in this particular case, the first digit has a higher probability of being a one than being a nine. But intuitively, I would have expected every digit to come out with equal probability. Right? Like 11%, one over nine. But instead what we get is this really surprising result, which is that the first digit seems to be about 30%. Right to have the first start to have the first digital one seems to be about 30%. To have the first first digit being a two seems to be about 18 or something percent and so on and so on. And then the first digit being a nine is is pretty low. It's going to be about what is this, 12 out of 200 countries. Right. So pretty low probability. So as it turns out, this graph actually follows something called Bedford's law. And this is a well-proven law. It applies to a bunch of different data sets that we find in nature datasets that don't really have upper or lower bounds. Right. Like country populations. Right. So Bedford's law effectively says the probability of the first digit in some so some big set of numbers being a12 or three whatever this D being the one or two or three or whatever. Is according to this formula. So if we find the probability of that first digit being a one, we basically find log base ten of two, which is about 2.28. Probability of that first digit being a two is log base ten of one and a half, which is about 0.17. So our data. The country populations. Right. If we look at just the first digit of our data, it also follows this law. Just pretty neat. Right. So a lot of data that we deal with on a daily basis follows this large number of social media followers, number of posts people make stock values, grocery prices, sports statistics, building heights, income taxes, things like that. All follow this this law, which is pretty cool. As an aside, one of the ways that people figure out tax fraud on income taxes is by applying Bedford's law to income taxes submitted people. When they kind of submit fraudulent numbers, they tend to make every number kind of come up with an equal probability. They forget about Bedford's law, and so they run this Bedford's law on potentially fraudulent tax submissions, and they figure out that, you know, whatever those people submitted don't actually follow this law and hence it's fraudulent. So, you know, if you're making up numbers, just remember Bedford's law. So, yeah, that's that's a really interesting thing that that can come out of some data. And again, we got to visualize it and see the the law in action. Okay. One last example I want to go through this one will have to oh, we'll kind of show a bunch of different things. It's going to have a lot of code. I'm going to briefly talk about it. But the code is in the slides or sorry, in the python file if you want to look at it more in depth. I'm going to compare city temperatures again, but we're going to do a more in-depth analysis dealing with a whole bunch more data. So this particular dataset, I've got daily temperatures for 55 years for 21 different cities. So the amount of data that I have here is going to be three, 65 times, 55 times 21. So that's how many rows would exist in my dataset, right? So that's a lot of numbers to look at manually. So instead we're going to rely on kind of aggregating it with averages and things like that to kind of make sense of all of this data. So this is what the file would look like. I've got three columns, effectively separated by commas. So the first one corresponds to the city. Second one corresponds to the temperature in Celsius. And the third one is the date that it was taken. So it's it's nicely in order. The date is delineated like this. So it's got. Yea. Yea. Yea, yea. Month, month, day, day. So this is 1961, January 4th. That's how we would read that. Right. So later, when we're trying to think about, you know, what, which one of grabbing, you know, particular temperatures for a specific year or things like that, then we can use the format, keep the format in mind and use that to extract the relevant information. Okay. So the first thing we want to do is to grab this data and save it again in a nice data structure that allows us to manipulate it, our heart's content. That is a list. So we're going to open up our file for reading. I'm creating two lists here, one for the temperatures, the other one for the dates. I'm going to loop through each line in my file and I know it's comma separated, so I'm going to split it on the comma. The thing at index zero will be my date will be my city. The thing at index one will be my temperature value. The thing at index two will be my date. Okay. I would like to take the temperature value and save it as a number because I want to plot these numbers. This specific function will get a list of all of the temperatures for a particular city. So the city here is going to be a parameter. So as I'm reading the file, I would only like to grab the lines that match that city. So here I've got this if statement. So I'm only going to do this stuff inside this statement if the city is matching the one I'm interested in. And then what do we do? Well, we're going to take our temperature value, which is the thing at index one, right? Because I've split on the commas, convert it to a float. There's no commas or anything weird like that in that number. So it's just a pure float near 0.55 as a string. If we cast it to a float, Python will happily do that for us. Then we're going to run a Celsius to Fahrenheit function throwback, to lecture one, to convert that Celsius to a Fahrenheit value. And then we're going to append all of these temperatures in a nice list. And at the end of the function, we're going to return all the temperatures. So it's going to be 365 times 55. Right. That's how many temperature values we have for one city. And what we'd like to do as a first step is to just get a sense of the average temperatures for each one of these different cities. So over every single data point that we have for a particular city, what is the average temperature over all these days, for all of these years? So I would like one number to represent the temperature per city. So that's what this code is doing. It's going to first get all of the cities that are in my file. It's all the unique values. Then it's going to get the average temperature over all of those three, 65 times, 55 years. Then it's going to grab the name of my city as just the first two characters, and then it's going to create a nice scatterplot. So I don't want to link all of these city values together. I would just like them to be dots in my plot. If we do that, we get something that looks like this. So this point here represents the temperature in Seattle over every day, over 55 years. So one point temperature point that represents the Seattle temperature. Right. For all of this data that I've got. What does this tell us? Well, not much that we didn't already know. I've got these cities down here that are super cold and those cities up there that are super warm. Right. And then all the rest of my cities are somewhere in the middle on average. Right. So nothing that we didn't really know. Nothing groundbreaking here. What would be a nicer thing to look at is the temperature change over time. Right. So here, my one data point tells me. The temperature of represents that city. But what I would like to do is grab the temperature that represents that city for each year. So for each year, I would like to get the average temperature for that year. And maybe I could see a trend, you know, for the temperatures getting warmer over time or or cooling over time or something like or not having any change at all. So this is the code that does that. I've got to get temperatures by here for city. This is kind of the function that gets run and it calls the one at the top. So here I've got the code from the previous slide. It gets a list of all the temperatures for a particular city. So over all those 55 years. And then I'm interested in all of these different years. So for each one of these years, I'm going to get a temperature value, right? This get temps for years, the function up there. And all it does is it looks at that third column and grabs the year. It matches those first four characters of the year entry. All right. And as long as it matches that year, then it's going to get added to this running sum. And at the end, I'm going to get the average for the year. And let's say that I'm going to compare four different cities. So I've got 55 values for each city representing the average temperature in those 55 years. And I've got four cities to compare. So this is what one plot would look like for Boston. Sorry. So this is what the plot would look like. I've got one line for Boston. That's the blue one line for San Diego. The red one line for Phenix, the orange, and one line for Miami, the green. What do we see? Well, yes, Boston on average is a lot colder than any of the three other cities. We knew that Miami and Phenix are nicely hot there. I would like to be there right now. And what about trends? Right. This is why we did this analysis. What do we see from the trends here? Well, the Boston temperature maybe increases a little bit slightly over time. San Diego seems to say about steady. The Phenix one seems to increase right pretty dramatically as time has gone by on average. And the Miami one may be also slightly increased. But this only tells us average temperatures. So one thing that we can do is check out the extremes. Right. In addition to plotting the average. Let's also plot the minimum for Boston and the maximum for Boston. Right. And see exactly how close that average is, is the average, you know, in the middle. And then the minimum and maximums are super far away from the average? Or are they all pretty much close to the average? So this is the code that does that. The function here is exactly the same as on the previous slide. The only difference is, instead of returning the average, we're also going to grab the max and the min for that list of temperatures. And then we've got all of the different cities to plot this for. So we get something that looks like this. Again. At first glance I have I tend to ignore the y axis at first glance. So at first glance again it looks like, hey, the minimums are pretty much the same. The maximums are pretty much the same, averages are pretty much the same. So misleading to think about that. So once again, let's help the the the reader and set limits on our y axis. Right? So here I've got a limit to my function or to my code. It's going to have every one of my graphs start at zero and top out at 100. And now the plots are nicely comparable. So now I'm plotting the average temperature for each year. So there's 55 of these data points. The minimum temperature for each year and the maximum temperature for each year. So 55 data points being plugged. What can we tell? A lot easier to infer information from this. Right. So we can see that the average temperature in Boston is the minimum temperature in Miami and San Diego. What else can we see? The variation in Boston is pretty high, right? The variation in Miami and San Diego is a lot lower. Right? San Diego goes from 40 to 80, whereas Boston goes from 0 to 90. So pretty high variation. The average for Boston and San Diego seems to be almost the same. Right. But that variation is very different between these two cities. Okay. So you know what would happen if there's a failure like the minimum one? Oh, yeah. Then it doesn't get plotted. Yeah. So that was a little tenuous there, but it didn't go down. I could imagine, like the minimum in Boston being below zero for one year, but yeah, then it would just wouldn't get plotted. So you could use that to guide you guide your limits like the the the code here could say y limit equals minimum of those three lists. Right. And you would be sure to make sure to like 2 to 2 you will ensure that that minimum will be will be hitting the limits. Great question. Okay. So one other thing that we can look at is the distribution of temperatures. All right. So this is a nice plot. It gives us sort of an an overview look at what happens year by year. But what if we focus on one specific year? And now for that year, let's think about what the temperature distribution looks like. Right? So what I'm interested in, in plotting is something like this. So I've got on the x axis maybe bins that correspond to different temperatures. So a temperature of zero. Temperature of one. Temperature of two, three, four, and so on. And then this is going to be a pretty big because maybe my max temperature will be 100. So for one particular year, I would like to have 100 bins and the height of each bin is going to be a count of how many days. Within that year we reached a temperature of zero. How many days? Within the year we reached a temperature of one. And we can average things or we can round temperatures. Right? Because obviously the temperature would be like 20.6 or something like that. Right. And then we can just round it so it fits in one of these bins. So that's exactly what this code is doing. So here it's looping over every single one of the the dates, and we're creating this list of the temperatures. And the list is for one specific year. So this year is my parameter here. Right. So here, this is just going through the data and ensuring that I'm grabbing only the rows that match that year. And then down here is where I'm creating a list of 100 elements. Right. So this down here, you can think of it as a list. I like this. And the index nicely. It worked out really nicely. The index is going to correspond to a temperature value, which is weird to think it only works in this particular scenario with Fahrenheit temperatures, but the index in this list corresponds to a temperature. So as I'm iterating through my list of temperatures over 365 days in a year, I'm going to round that temperature and I'm going to add it to the index that I believe it belongs to. Right. So in this way, I'm going to have, you know, if the temperature was four degrees, then not index four. I'm going to increment my count by one. Right. And if further on in the list, I've got another temperature that's four and index four, I'm going to increment it again. So I've got this nice list, this nice counts of all of the temperatures at different sorry, all of the the counts at all of these different temperatures. Right. So out of those three, 65 days, how many days had a temperature of four of three? 65 days. How many days had a temperature of 85? Okay. And then we can plot it. And then we're not going to plot a regular plot because we don't want these connected. We're not going to do a histogram because we made our own histogram here. Instead, we're going to do a bar plot, and the bar plot takes in my x axis and my y axis, the x axis being this list zero through 100 of corresponding temperatures and the y axis being the count of how many days had each one of those temperatures. And we get something that looks like this. So this is only for one year, right? So if we count the sum of all of these bars, right. How many how many times they appear? It should add up to three, 65 days. So this is the the distribution, I think in 1961, left as Boston and right to San Diego. Already. We can tell some pretty interesting things from this, right? So in 1961, what does the distribution look like for these two cities? Well, it looks like this is something we could already tell from the minimum and maximum. It looks like temperatures in Boston kind of went from about 0 to 85. But what the distribution tells us that the minimum and maximum couldn't tell us is how many days were that low, right? How many days were that high? Is it that we have some sort of nice looking bell curve type distribution, right, where most of our temperatures land comfortably in this middle range? Right. That's one option. Or maybe there is some city out there where it just has an even distribution. Right. So basically they're going to have temperatures that I'm sorry, the count of the temperatures basically is even so it doesn't really matter what temperature you're talking about. There will be an even number of days throughout the year that are at that temperature. Right. So this kind of graph can tell us this. So it looks like the temperature in Boston kind of maybe follows a very wide bell shaped curve, kind of maybe two, two bumps by a bimodal temperature in San Diego. Again, much a much lower variability, but also seems to follow this bell type curve here where maybe bimodal with two bumps here. One with temperatures that are just, you know, in the 50 fives, very few temperatures in the middle and then a bunch of temperatures in the seventies. So this is the distribution for 1961. And then we can again ask what happens to the distribution in a later year? So if we take more than one year that we plot here, I'm going to plot 1961 and 2015. So just two years and everything in between would be a very, very cluttered graph. I'm going to label the 1961 temperatures blue and the 2015 temperatures red. So then I get something that looks like this. A little hard to tell. So what we can do for this graph is we can actually add something called an alpha value. So a transparency. So we can kind of see what's behind the red. Does the blue go all the way down here? Is the blue just slightly below the red heart to tell from this? One thing we can do is to add that transparency. Like I said, another thing that we can do is to just plot them on two separate subplots. Okay. And then we can try to compare them to see exactly what happened from 1961 in terms of the distribution to 2015. Again, in terms of the distribution, right. So you can, if you want, play around with different cities, you know, your home city and see exactly what happened to the temperatures over all those years. So it's kind of a cute thing to try. Any questions? Okay. So that's the end. We've really just scratched the surface of the things that you can do with plotting today. Right. We saw how to customize our graphs. We saw how to create labels, you know, some really, really basic things. But I hope that sort of throughout all of this, you saw how useful this to visualize the data. Right. The commands are not so important. Right. Because you can always look those up. But what's important is to take some sort of set of data. Right. Which you'll be working with in the real world. If you do your app, if you decide to take other computer science courses in other departments, computation courses, you'll you'll be working with data. And as soon as you get it, it's important to just visualize it, to see what it looks like, sort of get a general sense of it. And once you get a sense of it, it can lead to more questions, which will cause you to kind of visualize the data in a slightly different way, which becomes more useful in answering questions and potentially posing new questions to investigate. So that's it for today. Next lecture will be just tying up some loose ends regarding dictionaries and just some ideas and hash tables and how dictionaries are stored in memory, as well as doing a little bit of preview of simulations, which are something that's a really useful technique. You know, again, if you're going to do some more computation courses in other departments, a simulation is something that's going to be really, really helpful. 
