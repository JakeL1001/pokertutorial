//Javascript to block off lessons that you havent passed the prerequisites for

var test1 = parseInt(document.getElementById("quiz1pass").textContent);
var test2 = parseInt(document.getElementById("quiz2pass").textContent);
var test3 = parseInt(document.getElementById("quiz3pass").textContent);
const loggedin = document.getElementById("loggedin").textContent;

const lesson1 = document.getElementById("lesson1");
const lesson2 = document.getElementById("lesson2");
const lesson3 = document.getElementById("lesson3");
const finalquiz = document.getElementById("finalquiz");

var lesson1text = document.getElementById("lesson1text");
var lesson2text = document.getElementById("lesson2text");
var lesson3text = document.getElementById("lesson3text");
const finalquiztext = document.getElementById("finalquiztext");

const lesson2link = document.getElementById("lesson2link");
const lesson3link = document.getElementById("lesson3link");
const finalquizlink = document.getElementById("finalquizlink");

lesson1text.innerHTML = "Learn the difference between spades, diamonds, clubs and hearts.<br>" + test1 + "%";
lesson2text.innerHTML = "In this lesson you will learn the hands and their ranking.<br>" + test2 + "%";
lesson3text.innerHTML = "In this lesson you will learn how texas hold 'em no limit is played.<br>" + test3 + "%";

if (loggedin == "False") { //blocks all if not logged it
    lesson1.style.filter = "grayscale(100%)";
    lesson1text.innerHTML = "Please log-in to begin lessons";
}

if (test1 < 50) { //blocks all after lesson 1 if lesson 1 hasn't passed
    lesson2.style.filter = "grayscale(100%)";
    lesson2text.innerHTML = "Must acquire passing grade in all previous lessons";
    lesson2link.setAttribute('href', "lesson1");
    lesson3.style.filter = "grayscale(100%)";
    lesson3link.setAttribute('href', "lesson1");
    lesson3text.innerHTML = "Must acquire passing grade in all previous lessons";
    finalquiz.style.filter = "grayscale(100%)";
    finalquizlink.setAttribute('href', "lesson1");
    finalquiztext.innerHTML = "Must acquire passing grade in all previous lessons";
}
if (test2 < 50) { //blocks all after lesson 2 if lesson 2 hasnt passed
    lesson3.style.filter = "grayscale(100%)";
    lesson3link.setAttribute('href', "lesson2");
    lesson3text.innerHTML = "Must acquire passing grade in all previous lessons";
    finalquiz.style.filter = "grayscale(100%)";
    finalquizlink.setAttribute('href', "lesson2");
    finalquiztext.innerHTML = "Must acquire passing grade in all previous lessons";
}
if (test3 < 50) { //blocks final quiz if lesson 3 isn't passed
    finalquiz.style.filter = "grayscale(100%)";
    finalquizlink.setAttribute('href', "lesson3");
    finalquiztext.innerHTML = "Must acquire passing grade in all previous lessons";
}