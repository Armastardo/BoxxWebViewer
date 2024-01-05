let portButton;
let webserial;
const TOTAL_BACKGROUDNS = 3;
let currentStyle = 1;

function changeStyle(){
  background = document.getElementById("background");

  if(currentStyle === 3) currentStyle = 1
  else currentStyle++;

  background.src = "images/background" + currentStyle + ".png";
}

function createButtons(){
  const container = document.getElementById("viewer");
  for (let i = 1; i <= 21; i++) {
    const div = document.createElement('img');
    div.id = 'button' + i;
    div.classList.add("button");
    div.src = "images/" + i + ".png";
    div.style.visibility="hidden";
    container.appendChild(div);
  }
}

function colorCircles(value){
  for(let i = 1; i <= 21; i++){
    const bitValue = value[i-1];
    const button = document.getElementById('button' + i);

     //Illuminate the circle if the corresponding bit is 1
    if (bitValue != 0) {
      button.style.visibility="visible";
    } else {
      button.style.visibility="hidden";
    }
  }
}

function setup() {
  createButtons()


  portButton = document.getElementById("logo");
  portButton.addEventListener("click", changeStyle);

  webserial = new WebSerialPort();
  if (webserial) {
    webserial.on("data", serialRead);
    // port open/close button:
    portButton = document.getElementById("connectButton");
    portButton.addEventListener("click", openClosePort);
  }
}

async function openClosePort() {
// label for the button will change depending on what you do:
let buttonLabel = "Open port";
// if port is open, close it; if closed, open it:
if (webserial.port) {
  await webserial.closePort();
  colorCircles("0000000000000000000000000");
} else {
  await webserial.openPort();
  buttonLabel = "Close port";
}
// change button label:
portButton.innerHTML = buttonLabel;
}

function serialRead(event) {
  serialData = event.detail.data;
  if(serialData.length === 25){
    colorCircles(serialData)
  }
  



}

// run the setup function when all the page is loaded:
document.addEventListener("DOMContentLoaded", setup);