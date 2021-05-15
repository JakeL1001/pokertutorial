$(".flipper").click(function() {
    $(this).toggleClass("flip");
    return false;
});

$(".glow").click(function() {
    $(this).addClass("cardglow");
    return false;
});

$(".reject").click(function() {
    $(this).addClass("cardreject");
    return false;
});


$(document).ready(function() {
    $("#flopAnimate").hover(
        function() {
            $(this).attr("src", "../../static/lesson3animations/flop.gif");
        },
        function() {
            $(this).attr("src", "../../static/lesson3animations/flop.jpg");
        });
    $("#turnAnimate").hover(
        function() {
            $(this).attr("src", "../../static/lesson3animations/turn.gif");
        },
        function() {
            $(this).attr("src", "../../static/lesson3animations/turn.jpg");
        });
    $("#riverAnimate").hover(
        function() {
            $(this).attr("src", "../../static/lesson3animations/river.gif");
        },
        function() {
            $(this).attr("src", "../../static/lesson3animations/river.jpg");
        });
});

function openPage(pageName, elmnt, color) {
    // Hide all elements with class="tabcontent" by default */
    var i, tabcontenttoclear, tablinksdecolour;
    tabcontenttoclear = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontenttoclear.length; i++) {
        tabcontenttoclear[i].style.display = "none";
    }

    // Remove the background color of all tablinks/buttons
    tablinksdecolour = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinksdecolour.length; i++) {
        tablinksdecolour[i].style.backgroundColor = "";
    }

    // Show the specific tab content
    document.getElementById(pageName).style.display = "block";

    // Add the specific color to the button used to open the tab content
    elmnt.style.backgroundColor = color;
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();

function showResults() {
    // gather answer containers from our quiz
    const answerContainers = quizContainer.querySelectorAll('.answers');
    var numCorrect = 0;
    // keep track of user's answers
    // for each question...
    QuizQuestions.forEach((currentQuestion, questionNumber) => {
        // find selected answer
        const answerContainer = answerContainers[questionNumber];
        const answerfinder = `input[name=question${questionNumber}]:checked`;
        const userAnswer = (answerContainer.querySelector(answerfinder) || {}).value;
        // if answer is correct
        if (userAnswer === currentQuestion.correctAnswer) {
            // add to the number of correct answers
            numCorrect++;

        }
    });
    let resultperc = (numCorrect / QuizQuestions.length) * 100;
    // show number of correct answers out of total
    if (resultperc < 50.0) {
        resultsContainer.innerHTML = `<div class="card card2" style="background-color: red;"><div class=card-body>${numCorrect} out of ${QuizQuestions.length} | ${resultperc}</div></div>`;
    } else if (resultperc >= 50.0 && resultperc != 100) {
        resultsContainer.innerHTML = `<div class="card card2" style="background-color: green;"><div class=card-body>${numCorrect} out of ${QuizQuestions.length} | ${resultperc}</div></div>`;
    } else if (resultperc == 100) {
        resultsContainer.innerHTML = `<div class="card card2" style="background-color: gold;"><div class=card-body>${numCorrect} out of ${QuizQuestions.length} | ${resultperc}</div></div>`;
    }
    document.getElementById("finalscore").innerHTML = `<input id="score" name="score" type="hidden" value=${resultperc}>`;
    document.getElementById("submit-continue").style.visibility = "visible";
    document.getElementById("submit").style.visibility = "hidden";
}


function buildQuiz() {
    // variable to store the HTML output
    const output = [];
    document.getElementById("submit").style.visibility = "visible";

    output.push(`<div class="card-deck">`);
    // for each question...
    QuizQuestions.forEach(
        (currentQuestion, questionNumber) => {

            // variable to store the list of possible answers
            const answers = [];
            output.push(
                `<div class="card">
                        <div class="card-body">
                            <div class="card-title">Question ${questionNumber + 1}</div>
                            <div class="card-text">
                                <div class="question">${currentQuestion.question}</div>`);
            // and for each available answer...
            let letter = "";
            for (letter in currentQuestion.answers) {

                // ...add an HTML radio button
                answers.push(
                    `<ul class="list-group">
                        <li class="list-group-item"> 
                        <input type="radio" name="question${questionNumber}" value="${letter}"> ${letter} : ${currentQuestion.answers[letter]}
                        </li>
                    </ul>`
                );
            }
            output.push(`<div class="answers">${answers.join('')}</div></div></div></div>`)
        }
    );

    // finally combine our output list into one string of HTML and put it on the page
    output.push(`</div>`)
    quizContainer.innerHTML = output.join('');
}

function beginQuiz1() {
    QuizQuestions = Quiz1Qs;
    startQuiz1.style.visibility = "hidden";
    buildQuiz();
}

function beginQuiz2() {
    QuizQuestions = Quiz2Qs;
    startQuiz2.style.visibility = "hidden";
    buildQuiz();
}

function beginQuiz3() {
    QuizQuestions = Quiz3Qs;
    startQuiz3.style.visibility = "hidden";
    buildQuiz();
}
const quizContainer = document.getElementById('quiz');
const resultsContainer = document.getElementById('results');
const submitButton = document.getElementById('submit');
const startQuiz1 = document.getElementById("Quiz1");
const startQuiz2 = document.getElementById("Quiz2");
const startQuiz3 = document.getElementById("Quiz3");
let QuizQuestions = "";
const Quiz1Qs = [
    { question: "Which card has the highest value in the suit?", answers: { a: "Ace!", b: "Queen", c: "Draw Four" }, correctAnswer: "a" },
    { question: "Which of the three is a real suit?", answers: { a: "Spades", b: "Red", c: "Blue" }, correctAnswer: "a" },
    { question: "Which of these four is a real suit?", answers: { a: "Triangles", b: "Reverse", c: "Diamonds", d: "Spells" }, correctAnswer: "c" },
    { question: "Which is a valid card?", answers: { a: "Joker", b: "Jack", c: "Jill", d: "Jester" }, correctAnswer: "b" }
];
const Quiz2Qs = [
    { question: "A flush is four of the same card", answers: { a: "No", b: "Yes", c: "Trick Question!" }, correctAnswer: "a" },
    { question: "A Straight is five cards in consecutive rank order", answers: { a: "Correct", b: "No", c: "Wrong that's a penta pair" }, correctAnswer: "a" }
];
const Quiz3Qs = [
    { question: "What is a fold?", answers: { a: "Betting all your chips", b: "Forfeiting cards out of your hand", c: "Betting half the community pot" }, correctAnswer: "b" },
    { question: "Wnat is a raise?", answers: { a: "the player does not bet further as they have already put in an amount that satisfies the current bet.", b: "Betting all your chips", c: "Increasing the minimum bet size with a bet" }, correctAnswer: "c" }
];

// on submit, show results
submitButton.addEventListener('click', showResults);
if (startQuiz1) {
    startQuiz1.addEventListener('click', beginQuiz1);
}
if (startQuiz2) {
    startQuiz2.addEventListener('click', beginQuiz2);
}
if (startQuiz3) {
    startQuiz3.addEventListener('click', beginQuiz3);
}