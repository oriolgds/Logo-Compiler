const textarea = document.getElementById("code-input");
const btnExecute = document.getElementById("btn-execute");
const btnStop = document.getElementById("btn-stop");
const btnRestart = document.getElementById("btn-restart");
const console = document.getElementById("console");
const consoleInput = document.getElementById("console-input");
function execute() {
    eel.execute(textarea.value);
}
function stop(){    
    eel.stop();
}
btnExecute.addEventListener('click', execute);
btnStop.addEventListener('click', stop);
eel.expose(writeOnConsole);
function writeOnConsole(textToWrite = "", style="normal"){
    console.innerHTML += `<span class="${style}">${textToWrite}</span><br>`;
}
textarea.addEventListener('keyup', ()=>{
    localStorage.setItem('code-text', textarea.value);
});
textarea.value = localStorage.getItem("code-text");

