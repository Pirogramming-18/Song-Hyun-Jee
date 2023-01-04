
let second = 0;
let milisecond = 0;
let active = false;

document.getElementById('startbtn').onclick = function () {
    if (active == false) {
        active = true;
        timeoutld = setInterval(function () {
            milisecond++;
            if (milisecond > 100) {
                milisecond = 0;
                second++;
            }
            document.getElementById('time').innerText = (second < 10 ? "0" + second : second) +
                ":" + (milisecond < 1000 ? milisecond : milisecond);
        }, 10);
    }
}

function addRow() {
    const table = document.getElementById('tablefill');
    const newRow = tablefill.insertRow();

    const newCell1 = newRow.insertCell(0);
    const newCell2 = newRow.insertCell(1);

    newCell1.innerHTML = ('<i class="fa-regular fa-circle" id="circle"></i>');
    newCell2.innerText = document.getElementById("time").innerText;
};

document.getElementById("pausebtn").onclick = function () {
    clearInterval(timeoutld);
    active = false;
    addRow()
};


document.getElementById("resetbtn").onclick = function () {
    active = false;
    second = 0;
    milisecond = 0;
    document.getElementById('time').innerText = "00:00";
};

document.getElementById("circle").onclick = function () {
    circle = innerHTML('<i class="fa-regular fa-circle-check"></i>');
}














