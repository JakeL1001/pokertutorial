


function updateanswers(question, answer) {
    clientresponse[question] = answer;
    

    
    for( i =0; i<document.getElementsByClassName("question")[question].getElementsByClassName("answer").length;i++ ){
        if(document.getElementsByClassName("question")[question].getElementsByClassName("answer")[i].classList.contains("chosen"))
        document.getElementsByClassName("question")[question].getElementsByClassName("answer")[i].classList.remove("chosen");  
    }
    document.getElementsByClassName("question")[question].getElementsByClassName("answer")[answer].classList.add("chosen");
    
  }

function findresult(){
    var total = 0;
    for(i=0; i<answerkey.length;i++){
        if(answerkey[i] == clientresponse[i])
            total++;
    }
    
    resultperc = (total/answerkey.length)*100
    console.log(resultperc)
    document.getElementById("finalscore").innerHTML = `<input id="score" name="score" type="hidden" value=${resultperc}>`;
    return total 
    
} 


var output = document.getElementsByClassName("question");
for( i = 0; i <output.length; i++){
    for(x=0; x<output[i].getElementsByClassName("answer").length;x++){
        output[i].getElementsByClassName("answer")[x].addEventListener('click', updateanswers.bind(event,i,x));
    }
}



var answerkey = [1,3];
var clientresponse = [-1,-1];
const submitButton = document.getElementById('submit');
submitButton.addEventListener('click', findresult);


