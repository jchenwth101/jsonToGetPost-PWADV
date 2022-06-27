# jsonToGetPost-PWADV
(Your participation in this test is subject to the Terms of Use in the attachment. If you do not agree to the Terms of Use, do not participate in the test, but please respond to this email to let us know the reason that you are not participating.)
Congratulations on being chosen to take the $$$$$$$$$$$$$$$$ Effort Test! To take this test, you will write a program that makes HTTP requests to a REST API to solve certain challenges. Here are some tips to get you started:
1) You can use any programming language you like.
2) We expect and encourage you to use the Internet to learn about topics you do not
know!
3) We will not review your code. We only record your submissions to our endpoints and
whether you have answered challenges correctly. You will not submit any code. Please
DO NOT send us any code. We will not look at it.
4) You do not have to complete all the challenges.
5) All sections of the test are weighted equally. Feel free to skip around if some challenges
seem more difficult than others.
6) All data returned and sent to our API must be in JSON format.
7) If you encounter errors or messages prompting you to contact us, and you choose todo
so, please include a pastebin of the relevant code. DO NOT include an image of the
code.
8) We WILL NOT provide guidance or “hints” for any individual challenges. This document
should have all the answers to any questions you might have. Only email us if you
receive an error message that says to contact us.
9) If your time gets extended or if you encounter an issue with your JWT, please grab a
NEW JWT before contacting us as this likely solve your issue.
Our API is hosted at: $$$$$$$$$$$$$$$$$$$$$$$$$$$ If you think there is a bug with one of the tests, please send us an email with a detailed description of the bug, steps to reproduce the bug, and the information you sent in your HTTP request. You have 1 week to work on this test.
NOTE: All request bodies are expected to be in application/json format. Except for the Knock-Knock exercise, we will always return a valid response in the following format:
{
    data: someDataReturned (if any),
message: information regarding the return of your request or the problems we are handing you.
}
 
Knock-Knock - Warm-up (NOT SCORED)
Do this exercise if you want a simple warmup, or if making web requests to APIs is new to you. Make a HTTP GET request to the endpoint /knockknock. You will receive a response whose body is the string “Who’s there?”. To see this work for yourself, go to: https://pa-kobayashi- test.herokuapp.com/knockknock in your browser.
NOTE: If you are new to this area, these instructions may not make much sense, so we encourage you to use the Internet to first gain a good understanding of the concepts mentioned in this exercise, since you will be using them throughout the test! Take your time here— foundations are important.
Authentication (DO BEFORE OTHER CHALLENGES BELOW)
Make a HTTP GET request to the endpoint /token with a header called uuid. The uuid should be set to the UUID provided to you in this email. If your request is successful, you will receive a JSON Web Token (JWT) in the response. This JWT will be used to authenticate you for each challenge below. To authenticate, attach the JWT to a header called token for each request.
NOTE: To find the expiration time and the final time that you may attempt this test until, please enter your JWT into this page: https://jwt.io/. The exp field indicates the expiration of the JWT and this test!
Math Problems
Make a HTTP GETrequest to the endpoint /getProblems. The response will contain an array of objects with three fields: operand1, operand2, and operator. Each of these objects represents a simple arithmetic problem. To solve this challenge, make a HTTP POSTrequest to the endpoint /submitAnswers, with the array of solutions. Each solution’s index should correspond to the index of the math problem given. In your JSON body, make sure your answers are set in a property called solution.
    
React
For the following portion of the test, you will be working with a JavaScript framework: React. React is a powerful JavaScript framework that allows us to build reusable front-facing user components more easily. It was developed by Facebook and is utilized by a wide range of companies such as: Facebook, Instagram, Netflix, NYT, Twitter, WeWork, Airbnb, Khan Academy, WhatsApp, Vivaldi, and Dropbox. At PowerAdvocate, we use React for most of our front-end code base along with some internal and third-party libraries. We have compiled a small selection of React problems for you to solve below.
To get started, the first thing you will need to do is set up a React environment. We recommend using a tool such as create-react-app to build an application. Once you have a React environment setup, then you should follow the following instructions to complete your test. If you experience any compilation errors, try updating your project to use “react-scripts” version 4.0.3, as there have been some issues with higher versions.
1. Replace App.jswith the code found in this: https://pastebin.com/abQpRcnw. This is your component code, which you will be editing to solve the problems. You will also need to install enzyme and enzyme-adapter for this. Before continuing, you may want to start the React server and make sure you don’t have any errors using the npm start command
2. Make a HTTP GET request to /reactProblem to get the Util code. This code will be obfuscated and look like gibberish -- this is intentional. PLEASE DO NOT attempt to de- obfuscate this code. Paste this code into a util.js in the same directory as App.js. For the code in util.js to run without errors, you may need to write a small program to properly write this code to a file, as JSON has escapes \'s and newlines.
3. Start your application using npm start. Your application should compile successfully, with compiler warnings. You can ignore these warnings if they come from the Util.js code.
4. The App.js file only has partially complete code. Follow the directions in the comments in the App.js file to complete all the app’s features. .
5. When you implement feature correctly, you’ll get a code to send to the Effort Test API. Make a HTTP POST request for each problem to /reactSolution/:index with a JSON body in the following format: The index starts from 0 and corresponds to the order that the problems are in.. The index starts from 0 and corresponds to the order that the problems are in.
NOTE: If you hit the /reactProblem endpoint multiple times, please use the obfuscated code that you received most recently, or else you WILL NOT be able to solve the problems.
   
Regular Expressions
This challenge has three sub-challenges, all with varying difficulty. Each sub-challenge can be solved by making a HTTP GET request to /firstRegexProblem, /secondRegexProblem, or /thirdRegexProblem, respectively. The instructions for each sub-challenge will be in the response. You DO NOT have to solve the problems in order, but the first sub-challenge includes helpful tips and resources, so it is recommended that you solve that one first.
NOTE: Each regular expression should match the entire string, not an occurrence of the string in a larger string.
SQL Queries
SQL stands for Structured Query Language. SQL itself is a standard and can be implemented differently from database to database. A database is made of tables. Each table has a name and columns. Each column has a name and constraints on the data that can be stored in the column. Information stored in databases is referred to as “records”. Common queries written in SQL can perform tasks such as creating new records in databases, updating existing records, deleting existing records, and retrieving existing records.
NOTE: Here are some resources that we recommend for learning SQL if you have no prior experience: (A) (B).
For this challenge, you will be asked to craft queries that will select a subset of data from a database. We will be using the AlaSQL database. To create a database unique to you, make a HTTP GET request to the /createDatabase endpoint. Each time you make this request, it will reset your database, repopulating it with new records. If you get any “database doesn’t exist” errors, you can make a new request to /createDatabase to fix them.
NOTE: All databases conform to the SQL standard, but their implementations differ from vendor to vendor. Some keywords might exist in one but not the other. When looking for specific functionality to use, refer to the AlaSQL Wiki.
The database you are using has two tables: owner and pet. Each table holds approximately 1000 records. The pastebin holds the structure of the tables: https://pastebin.com/JVV3rikK.
   
For each sub-challenge listed below, make a HTTP POSTrequest to the specified URL with your solution query in a JSON body like the format here: https://pastebin.com/WUfZZy4K.
   /allPets
/dogsOnly
/noOwnerDogs
/catsAndDogs
Submit a query to get all pets.
Submit a query to get only pets that are dogs.
Submit a query to get only pets that are dogs and do not have owners.
Submit a query to get pets that are cats or dogs.
         /ownersIncludingDo
gs
   Submit a query to get all owners, and if they have dogs, include their dogs, ordered by owner_id and then by pet_id. This is the expected result table format:
{
    owner_id,
    owner_name,
    pet_id,
    pet_owner,
    pet_name,
    pet_type,
    pet_breed
}
owner_id should be the id of the owner owner_name should be the name of the owner pet_id should be the id of the pet pet_owner should be the owner id
pet_name should be the name of the pet
pet_type should be the type of the pet
pet_breed should be the breed of the pet
   /onlyOwnersWithThe
irDogs
  Submit a query to get only owners with dogs, and include the dogs in the results, ordered by owner_id and then by pet_id. This is the expected result table format:
{
    owner_id,
    owner_name,
    pet_id,
    pet_owner,
    pet_name,
    pet_type,
    pet_breed
}
owner_id should be the id of the owner owner_name should be the name of the owner pet_id should be the id of the pet pet_owner should be the owner id
pet_name should be the name of the pet
pet_type should be the type of the pet
pet_breed should be the breed of the pet
 
   /howManyOfEach
  Submit a query to get all the different breeds of pets, along with their count, sorted alphabetically by breed. The expected format is a 2D array:
[
[ breed1, 10 ], [ breed2, 31 ], ...
]
   /allNames
   Submit a query to get all names that exist in both tables, and order them in ascending order. DO NOT list duplicate owner names.
 
NOTE: To test your queries, you can make a HTTP POST request to /testQuery. For example, if you make the following request:
{
     solution: “SELECT * FROM owner”
}
The /testQuery response will be: [
{id: 123, name: “John Smith”},
{id: 456, name: “Linda Smith”}, {id: 789, name: “Arnold Topher”}, {id: 753, name: “Samantha Bowman”}, {id: 159, name: “Pepper Arker”}, {id: 825, name: “Thor Odinson”}, ...
]
