//Javascript to block off lessons that you havent passed the prerequisites for

const test1 = document.getElementById("quiz1pass").textContent;
const test2 = document.getElementById("quiz2pass").textContent;
const test3 = document.getElementById("quiz3pass").textContent;
const loggedin = document.getElementById("loggedin").textContent;

const lesson1 = document.getElementById("lesson1");
const lesson2 = document.getElementById("lesson2");
const lesson3 = document.getElementById("lesson3");
const finalquiz = document.getElementById("finalquiz");

const lesson1text = document.getElementById("lesson1text");
const lesson2text = document.getElementById("lesson2text");
const lesson3text = document.getElementById("lesson3text");
const finalquiztext = document.getElementById("finalquiztext");

const lesson2link = document.getElementById("lesson2link");
const lesson3link = document.getElementById("lesson3link");
const finalquizlink = document.getElementById("finalquizlink");

if (loggedin == "False") { //blocks all if not logged it
    lesson1.style.filter = "grayscale(100%)";
    lesson1text.innerHTML = "Please log-in to begin lessons";
}

if (test1 == "False") { //blocks all after lesson 1 if lesson 1 hasn't passed
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
if (test2 == "False") { //blocks all after lesson 2 if lesson 2 hasnt passed
    lesson3.style.filter = "grayscale(100%)";
    lesson3link.setAttribute('href', "lesson2");
    lesson3text.innerHTML = "Must acquire passing grade in all previous lessons";
    finalquiz.style.filter = "grayscale(100%)";
    finalquizlink.setAttribute('href', "lesson2");
    finalquiztext.innerHTML = "Must acquire passing grade in all previous lessons";
}
if (test3 == "False") { //blocks final quiz if lesson 3 isn't passed
    finalquiz.style.filter = "grayscale(100%)";
    finalquizlink.setAttribute('href', "lesson3");
    finalquiztext.innerHTML = "Must acquire passing grade in all previous lessons";
}