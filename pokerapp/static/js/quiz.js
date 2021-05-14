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
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Remove the background color of all tablinks/buttons
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
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
    // keep track of user's answers
    let numCorrect = 0;
    // for each question...
    QuizQuestions.forEach((currentQuestion, questionNumber) => {
        // find selected answer
        const answerContainer = answerContainers[questionNumber];
        const selector = `input[name=question${questionNumber}]:checked`;
        const userAnswer = (answerContainer.querySelector(selector) || {}).value;
        // if answer is correct
        if (userAnswer === currentQuestion.correctAnswer) {
            // add to the number of correct answers
            numCorrect++;

        }
    });
    let resultperc = (numCorrect / QuizQuestions.length) * 100
        // show number of correct answers out of total
    resultsContainer.innerHTML = `${numCorrect} out of ${QuizQuestions.length} | ${resultperc} `;
    document.getElementById("finalscore").innerHTML = `<input id="score" name="score" type="hidden" value=${resultperc}>`
    document.getElementById("submit-continue").style.visibility = "visible";
}


function buildQuiz() {
    // variable to store the HTML output
    const output = [];

    output.push(`<div class="card-deck">`)
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
                                <div class="question">${currentQuestion.question}</div>`)
                // and for each available answer...
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
    buildQuiz();
}

function beginQuiz2() {
    console.log("MADE IT");
    QuizQuestions = Quiz2Qs;
    buildQuiz();
}

function beginQuiz3() {
    QuizQuestions = Quiz3Qs;
    buildQuiz();
}
const quizContainer = document.getElementById('quiz');
const resultsContainer = document.getElementById('results');
const submitButton = document.getElementById('submit');
const startQuiz1 = document.getElementById("Quiz1");
const startQuiz2 = document.getElementById("Quiz2");
const startQuiz3 = document.getElementById("Quiz3");
let QuizQuestions = "";
const Quiz1Qs = [{ question: "Who invented JavaScript?", answers: { a: "Douglas Crockford", b: "Sheryl Sandberg", c: "Brendan Eich" }, correctAnswer: "c" },
    { question: "Which one of these is a JavaScript package manager?", answers: { a: "Node.js", b: "TypeScript", c: "npm" }, correctAnswer: "c" },
    { question: "Which tool can you use to ensure code quality?", answers: { a: "Angular", b: "jQuery", c: "RequireJS", d: "ESLint" }, correctAnswer: "d" },
    { question: "who's the man?", answers: { a: "Jake", b: "Not Jake", c: "Kane", d: "Jordan" }, correctAnswer: "a" }
];
const Quiz2Qs = [{ question: "test", answers: { a: "wrong", b: "right", c: "wrong" }, correctAnswer: "b" },
    { question: "test2", answers: { a: "right", b: "wrong", c: "wrong" }, correctAnswer: "a" }
]
const Quiz3Qs = [{ question: "testQ3", answers: { a: "wrong", b: "right", c: "wrong" }, correctAnswer: "b" },
    { question: "test2Q3", answers: { a: "not right", b: "wrong", c: "right" }, correctAnswer: "c" }
]

// display quiz right away
//buildQuiz();

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

// if answer is correct
if (userAnswer === currentQuestion.correctAnswer) {
    // add to the number of correct answers
    numCorrect++;

    // color the answers green
    answerContainers[questionNumber].style.color = 'lightgreen';
}
// if answer is wrong or blank
else {
    // color the answers red
    answerContainers[questionNumber].style.color = 'red';
}