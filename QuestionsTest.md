Question's TestAnswered
=====

## 1. What is the difference between ++a and a++?
The difference is when increase the value.
In the case of ++a, first increase the value then is used the variable.
In the case of a++. first is used the variable then increse the value.


## 2. Can you explain what you consider to be the key differences between object-oriented programming and functional programming?
The key difference between both is how they work and interactive with the data. 
On OOP the data is mutable and uses object and methods, and interactive using loops. So in resum it uses concept of object. An example of an instruction from Class Object in C++.
And on Functional Programming the data is not mutable and uses functions and variables, and to interactive uses recursion. So in resum it uses function evaluation. An Example of an instruction on SQL.

## 3. What is the difference between a closure, a callback, a lambda, and a promise?
Closure is a function that start and end in the same environment where is defined.
Callback is a function that eventually get called back. For that reason it has been defined as "call back".
Lambda is a function with not name, also called anonymous function.
Promise, I don't know I didn't use it, or I don't remember used it.

## 4. Explain logic short-circuiting, and how it can affect the code you write.
A short-circuiting is instruction that in programming language is using Booleans operations.
Where the second argument or instruction is executed or evaluated just when the first argument is executed or evaluated.
Usually short-circuiting are expressions using Boolean operators as: &&, ||, AND, OR, XOR...
But also short-circuiting acts or occurs when on statements request for Boolean instruction or statement, like this example:

```python
isActivated = True
if (isActivated): # boolean instruction or short-circuiting
    then statements
    
```

## 5. What are your thoughts on composition versus inheritance?
Inheritance == "is a"; then Composition == "has a".
Inheritance is a class inherit that use the fields or variables and methods of its superclass. A class
can inherit from other class or inherit from many classes at the same time, and this superclasses even can inheret from
other superclass. Also can be subclasses that can override methods and/or fields to alter the behavior, creating a new inherit class. But this implementation can be done too using composition.
Composition is when in a field's class is defined as object of other class, allowing to extend the functionality of the class. 
Then, when I used inheritance is when I was sure that the initial desing of the structure's class is not going to make a big changes in the future. I have use inheritance like to implement an interface. And when I needed to extend a functionality of this interface I have use composition. Because if for any reason the code of any superclasss has to be change in fuction of the big structured designed can be more or less tedious. Then when I am not sure from the beginning that an inherit could be needed more functionalities in the future, I consider that implementing the code using composition can be more confortable and more easy to manage new modifications.

I going to give and example:
A car is a vehicle. A class vehicle has some many objects like wheels and other parts. This objects will be fields of the class car. And then the car would be a subclass of vehicle. If its need to add functionalities. Just we have to add objects as fields and add this functionalities in the classes of that objects (like wheels).
This allow to work with a modulation. Then that modulation could reuse for quickly and easily. As to creating a new vehicle, a motorbike. Then the motorbike can reuse functionalities of the wheels class just adding the object wheel as field inside the motorbike class. This example is using composition.

But if in this example is decided to create a superclass vehicle and then an inherited class called car, that inherit from vehicle and others class from each part of the car. If in the future is decided to modify the wheel class would make issues or work modiying the car's class. Basically because the pilars or base of the vehicle class are the others classes from where inherit. And in this example as more up we go in the inheritance to do a change, it would be more tedious to manage the subclasses. Because in subclasses we should manage and work a big change that affects all the subclasses form the inheritance.

Developing classes the important stage is at the beginning, when we should plan and design a good architecture to facility the future work.

## 6. How would you choose between using a regular expression, a parser, or a simple string search? Give examples.
I would use a regular expresion when I want to match specific requirements of an string. Like to validate if a string contains only lower characters 'a to z'.

```python
re.findall('[a-z]+', 'javierE')
```

A Parser to convert a data into a required format. As when we want to convert an integer data into a string variable.

```python
int a = 11
string number = ''
number = str(a)
```

A simple string search when we want to know if a string contains a string.

```python
sentences = "Javier is good boy"
str = "goo"
sentences.find(str)
```

## 7. Can you explain how dependency injection helps when writing unit tests?
No, I don't have the habit to work writing unit test. Usually I test my code by the traditional way, running the software trying all possibilities can be done. I took this bad habit when I learnt programming for video games. Using Django I use a couple times doing a simple test, to understand it how to code it. Then I don't know how dependency injection can help, because I don't have deep knowledge writing unit test. So, I considere that I should work more writing unit test for get deep experience to understand it and have opportunity to answer this question on secure way and trusting with myself on my answer.
But I can image it, that help faciliting structure code into the object or structre code that need to test. Like a kind of controller between the object or code and the view of the test. Similar that the design of MCV. Where the Controller help to represent the model into the view.

## 8. Give an example of how you would use defensive programming techniques (otherthan to sanitise user input).
Well, sanitise or double check the user input is the first that a beginner programmer learn programming. Once times that the developer realize the software can be broken (run a bug while is in execution) once times is decided to input a data that is not expected to be input. Like try to input number in a string's field (string variable).

I considere that the second technique that a developer learn is to check "nulls" or null data. If a variable is declarated but it is not created or assigned any value and is pretending to use it. The program will crash in execution.
Then a good practice is to check nulls or if the variable are nulls, before to manage them.
This can allow the developer to manage an error controlled.

## 9. Do you think it is good or bad to commit ???built??? files? (E.g. the output of SCSS, etc.)Explain why.
It is not the end of the world, but it is not good idea. It is good idea when we want to share everything. Or allow to download all inside the project. But generally, is not good idea because the "built" files have been created and optimized in an specific hardware and software. Then the best practice is to re-built this files for each machine where will run it.
For small libraries that would be using when is building the files of a project, may be is doesn't make issuse working. But when there are big libraries and combined with them. The best practice is to re-built to optimize it.
Otherwise is when we are going to run the software in a container (virtualization) or virtual machine that is hosting the software with the source and the built files. Because as we share to the container or the virtual machine. Will not generate any problem.

## 10. When would you use fully-normalised form, and when would you use JSONcolumns?
I am not sure, but I think they are related with the normalization of a data base. So, I think that fully-normalised form are the form to input that into a normalized data base.
I am not really sure, but I think that JSON columns is used when is needed to insert an JSON string into a table of data base. To input structured data into a table that expect and unstructured data.

## 11. When would you use a stored procedure and why?
To save SQL statements to re use it. Like to have a repository of query code inside our database.

## 12. When is it inadvisable to rely upon ORM?
I don't know, I'm not sure. ORM is used to map tables structures into objects, to handle database data as objects. To facilitate searching and filtering of data, with object-oriented programming. So, logically, it would be inadvisable to trust when it will not be necessary to map the tables of a database into objects. I suppose this would be when trying to map a large data of tables, it would not be advisable to rely on ORM. Because maybe it slows down the process, or saturates the memory when it comes to mapping a large amount of data. So it would be more optimized to search and filter data through a direct SQL statement to the database.

## 13. What was the most useful feature that was added to the latest version of your chosen language? Please include a snippet of code that shows how you've used it.
The last useful feature that I have used is "async/await" or called asyncio. It is implemented from Python 3.5 and I have used it in recently personal project, programming a cryto-trading bot.
In a few word asyncio is a kind of threathing for network process or request managed in a specific lood desinged to work smoothly and with flow data.
When a client software does a request via http, the client create a process where request specific data from a server.
By default the process that does the request, doesn't finish until the server respond the request. And when the client receive and process the respond, then is when the software running in the client pass to the next process. The time of the respond depends of many factor like the size of the respond, the lantecy of the transmission, etc.
Then if we need to implement a software or part of code where is needed to does many request on the same time without depending that each request required be finished to pass to the next request, is when "asyncio" works to make this administration with flow simulating a kind of multi-threading of request.

In my case I used it to develop a part of bot. This bot is requesting data from 2 or more exchanges of cryptocurrencies. And then compare the value of each cryptocurrency of this 2 exchanges.
Then, let me explain how asyncio works using this example.
The software request the data from one exchange. And usually the respond comes in 4 seconds. Then, let's say that for any reason the respond from the server is cut or more long than expected; for example let's say 2 min. Then using the traditional use of the process, the request of the data from the second exchange will start 2 min after started the request of the first one.

Using asyncio it will force to the software to do basically both request on the same time. Or in other words, a request or to initialize a request will not depends directly from the respond on time of other resquest.
With this code it can allow the bot to received data from both exchanges practicaly at the same time. Making more accurate the time to compare price of same pairs of coins, in a similar faction of time.
The next code is not exactly what I used, but it represent approximately what I did or used.

```python
import asyncio

async def check_pair():
    result_exchange_A = await exchangeA()
    result_exchange_B = await exchangeB()
    
async def main():
    await check_pair()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
```

## 14. What is your preferred approach to responsive design?
Go back to 90s or 2000 year?? 15 years ago was the best era. When someone didn't need to care about to shot his mind.
When developer just did care about one solution, full size. Or an size inside the range of the usual resolution used.
What happened? Arrived the iphone/ipad era. The first devices with different screen's size and different resolutions.
Who has developed an software at the init of this era, may be can understand the headaches of multi-resulions.
Today by today this technique and the tecnology involved to manage the technique has been upgrade allowing to develop a software or website ready to delivery in any device, making a quickly road map.
Today there are so many diferent resolutions. And seems that each year appear new ones. And this will be continue meanwhile the screens are in evolution.
Then In my opinion I think that is essential to work with responsive design. Because If a product can't be load in an specific device, it means that there are potential lost of customers or users can't use the product.
For develop websites and with some specific libraries that works with vectorial draws, the responsive design is an easy task to manage it. That happens with all frameworks for work on responsive design for websites. Even working with pure images, RGB files or BMP files is a easy task using website frameworks. 
But when is working with BMP files and there is not a framework or library that re-scale automatically can be tedious. Because we will manage manually the scalation of the graphics. This is more usually when is developing video games based on BMP files. Like 2D video games. Because for each resolution we will manage manually the load of different size of each image. And previously we will design and export in different sizes, for each resolution. Plus probably we will need to manage manually the position of graphic for each resolution and size of screen.

So, concluding. Responsive design is necesary. But depending of the develop can be more or less confortable and/or easy.

## 15. Please describe yourself using JSON.
I am not an expert using JSON, but I can define myself using JSON making a comparation with practice surf.
I feel good on the sea, estable on the tableboard. I am not an expert using JSON, but I can define myself using JSON making a comparation with practice surf.
I feel good on the sea, estable on the tableboard. But I feel that I have to continue surfing waves to get better experience.