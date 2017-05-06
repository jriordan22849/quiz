# quiz
Coding Challenge
Name: Jonathan Riordan
Date: 6th of May 2017

URL for website: http://188.166.82.38:8000

Challenge

The challenge was to create a web application that allows a user to complete quizzes online.

Solution

The technologies that I used were to complete the challenge were:

The solution that I came up with is as follows. I developed a web application that allows users to complete quizzes online. 

A user can register to the site or log into the website. Once a user has logged in, the user can choose a quiz to complete. The names of the quizzes are displayed in a table.

User authentication was also implemented, if a user is not logged into the website, the user wont have access to a quiz. If the user try to paste the quiz url into the browser the website will redirect the non logged in user to the login page.

The quizzes consist of question and answers. The minimum number of questions for a quiz is one. The user can select their answer to a question by clicking on a radio button.


The architecture of the system consists of three tiers. The first tier is the client. This consists of HTML and CSS. Its purpose is the displaying of information to the user. 

The second tier is the server. The server handles request from the website for both GET and POST requests.  The Django server is running on a Ubuntu server on a Digital Ocean droplet. The server interacts with the last tier which is the database. The database holds all the data. Data such as users login credentials and all the information relating to the quizzes.

Further work that I would have implemented would be allowing a logged in user create their own quiz. Providing an interface to allow a user to have this functionality. Other parts that I would of improved would of been the results page. Instead of just displaying the user score, I would of liked to display the users selected answers to the quiz and highlighted the question the user got wrong and right. Due to time restrictions and exams for college, I was unable to complete those tasks. 

The database was also set up using foreign key. Each question has a foreign key linking to the quiz name the question belongs to. This is the same for the Answers. Each answer has a foreign key to the Question the answer belongs to. This was done so the correct data is been displayed to the user. The models for the database can been on my Github:

GitHub Link: https://github.com/jriordan22849/quiz/blob/master/mysite/quiz/models.py

When a user completes a quiz, the answers selected by the user are sent to the server. I retrieve the questions and answers from the database relating to the quiz selected by the user. I compare the user answer to the answers in the database. In the Option model, there is a field called “rightAnswer”. This a boolean. If this boolean is True, then it is the right answer for that question. I get the user answer and a I get the object in the database. If the field “rightAnswer” is True on  object selected by the user, the user score increases by one. If the field is set to False, then 0 is added to the user score. 
