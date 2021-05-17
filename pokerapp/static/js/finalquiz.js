function updateanswers(question, answer) {
    if (!submitted) {
        clientresponse[question] = answer;
        for (i = 0; i < document.getElementsByClassName("question")[question].getElementsByClassName("answer").length; i++) {
            if (document.getElementsByClassName("question")[question].getElementsByClassName("answer")[i].classList.contains("chosen"))
                document.getElementsByClassName("question")[question].getElementsByClassName("answer")[i].classList.remove("chosen");
        }
        document.getElementsByClassName("question")[question].getElementsByClassName("answer")[answer].classList.add("chosen");
    }
}

function findresult() {
    submitted = true;
    var total = 0;
    for (i = 0; i < answerkey.length; i++) {
        if (answerkey[i] == clientresponse[i]) {
            console.log(document.getElementsByClassName("question")[i].getElementsByClassName("answer")[clientresponse[i]]);
            document.getElementsByClassName("question")[i].getElementsByClassName("answer")[clientresponse[i]].classList.add("correct");
            total++;
        } else if (clientresponse[i] > -1) {
            document.getElementsByClassName("question")[i].getElementsByClassName("answer")[clientresponse[i]].classList.add("incorrect");
        }
    }
    let resultperc = (total / answerkey.length) * 100;
    resultperc = resultperc.toFixed(2);
    const resultsContainer = document.getElementById("results");
    if (resultperc < 50.0) { //show in red box if fail
        resultsContainer.innerHTML = `<div class="card card2" style="background-color: red;"><div class=card-body>${total} out of ${answerkey.length} | ${resultperc}</div></div>`;
    } else if (resultperc >= 50.0 && resultperc != 100) { //show in green box if pass but not 100%
        resultsContainer.innerHTML = `<div class="card card2" style="background-color: green;"><div class=card-body>${total} out of ${answerkey.length} | ${resultperc}</div></div>`;
    } else if (resultperc == 100) { //show in gold box if 100%
        resultsContainer.innerHTML = `<div class="card card2" style="background-color: gold;"><div class=card-body>${total} out of ${answerkey.length} | ${resultperc}</div></div>`;
    }
    submitButton.style.display = "none";
    document.getElementById("finalscore").innerHTML = `<input id="score" name="score" display:"none" value=${resultperc}>`;
    return total;

}


var output = document.getElementsByClassName("question");
for (i = 0; i < output.length; i++) {
    for (x = 0; x < output[i].getElementsByClassName("answer").length; x++) {
        output[i].getElementsByClassName("answer")[x].addEventListener('click', updateanswers.bind(event, i, x));
    }
}


var submitted = false;
var answerkey = [3, 1, 1, 3, 0];
var clientresponse = [-1, -1, -1, -1, -1];
const submitButton = document.getElementById('submit');
submitButton.addEventListener('click', findresult);
document.getElementById("myForm").setAttribute("action", "");