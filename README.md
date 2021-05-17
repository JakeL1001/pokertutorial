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
python -m venv venv #create a new virtual env
venv\Scripts\activate #activate venv
pip install -r requirements.txt #install requirements
flask run #run flask

To run consequent times on windows;
venv\Scripts\activate #activate venv
flask run #run flask

website can now be accessed on your browser with local host (127.0.0.1:5000)

-- Unit Testing information --
Note Updated requirements with selenium and pytest
Install chromewebdriver from https://sites.google.com/a/chromium.org/chromedriver/downloads
currently the chromedriver ver is 90 (the one in the project directory)

Open the virtual environment and enter this command to run the unittester.py file
python -m unittest -v unittester.py

---References---
Top Png, 2019. casino cards png - falling poker chips PNG image with transparent background. Available at: <https://toppng.com/uploads/preview/casino-cards-png-falling-poker-chips-11562995898mdvm5phghg.png> [Accessed 12 May 2021]

Wikipedia, 2005. A plot of normal distribution (or bell-shaped curve) where each band has a width of 1 standard deviation. Available at: <https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Standard_deviation_diagram.svg/1280px-Standard_deviation_diagram.svg.png> [Accessed 13 May 2021].

dribbble.com, n.d. Poker. Available at: <https://cdn.dribbble.com/users/1981371/screenshots/6547432/poker_dribbble.gif> [Accessed 13 May 2021].

legalbetting.com, n.d. Legal Online Poker in the USA. Available at: <https://www.legalbetting.com/app/uploads/2020/03/hero-img-poker.png> [Accessed 12 May 2021].

Fowler, D., 2020. Poker Hands The Ranking. [images] Available at: <https://tekeye.uk/playing_cards/poker-hands-the-rankings> [Accessed 15 May 2021].


Vexels.com, 2018. Spades Card Icon. Available at: <https://images.vexels.com/media/users/3/151229/isolated/preview/3fbd44975e2287324c2ee8d5f4017c67-spades-card-icon-by-vexels.png> [Accessed 13 May 2021].

pngpix.com, 2016. Playing Card Symbols. Available at: <https://www.pngpix.com/wp-content/uploads/2016/11/PNGPIX-COM-Playing-Card-Symbols-PNG-Transparent-Image.png> [Accessed 16 May 2021].

PokerStars, n.d. Poker Hands Texas Holdem. [image] Available at: <https://cmsstorage.rationalcdn.com/assets/ps/assets/common/images/how-to-play/content/poker-hands/texas-holdem/royal-flush.png> [Accessed 15 May 2021].

-- To Do List --
TODO: change card titles to one consistent heading (h2?)
