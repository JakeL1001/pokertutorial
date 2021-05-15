# pokertutorial
Agile Web Development Project; Poker Tutorial.

-- The Website Purpose --
We developed this website to be used as an introduction into the basics of poker. During the various
covid-19 lockdowns we played virtual poker as a safe, isolated activity. Poker can seem intimidating at first
but we aim to ease users into the experience by explaining the basics. That is, information not relating to;
complicated odds, strategy and such.

The website is designed to deliver content and quiz the users. We felt this was the most efficient and user-friendly way to deliver a sub 10 minute experience. The quizzes are markable and results are both immediately given and graphed and displayed.

-- The Website Architecture --
The website is formatted to have two main groups of pages, lessons and 'home' pages.
Users open to the landing splash page which "promotes the theme and purpose to user". Users can register and login.
After doing so lessons are available. On the lesson pages are content and assessments. Some other 'home pages' include
the profile page for "giving feedback to the user". As well as a page for "aggregate results and usage statistics"

--Setting Up the Virtual Environment --
To run first time on windows; 
python -m venv venv              #create a new virtual env
venv\Scripts\activate            #activate venv
pip install -r requirements.txt  #install requirements 
flask run                        #run flask

To run consequent times on windows;
venv\Scripts\activate           #activate venv
flask run                       #run flask

website can now be accessed on your browser with local host (127.0.0.1:5000)

-- Unit Testing information --
Note Updated requirements with selenium and pytest
Install chromewebdriver from https://sites.google.com/a/chromium.org/chromedriver/downloads
currently the chromedriver ver is 90 (the one in the project directory)




-- To Do List --
TODO: change card titles to one consistent heading (h2?)