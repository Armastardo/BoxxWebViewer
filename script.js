let portButton;
let webserial;

function addDivs(){
  for (let i = 1; i <= 21; i++) {
    const div = document.createElement('div');
    div.className = 'div' + i;

    const circle = document.createElement('div');
    circle.id = 'circle' + i;
    circle.className = 'circle';
    div.appendChild(circle);

    document.getElementById('grid-parent').appendChild(div);
}

}

function colorCircles(value){
  for(let i = 1; i <= 21; i++){
    const bitValue = value[i-1];
    const circleElement = document.getElementById('circle' + i);

     //Illuminate the circle if the corresponding bit is 1
    if (bitValue != 0) {
      circleElement.classList.add('on');
    } else {
      circleElement.classList.remove('on');
    }
  }
}

function setup() {
  addDivs();
  //drawCircles();
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