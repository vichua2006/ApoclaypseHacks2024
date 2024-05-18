var pressed = [];
const p = document.querySelector('h1');
const timeout = 100;

function onkeypressed(e){
    pressed[e.keyCode] = e.type == 'keydown';
}

function checkkeys(){
    let flag = false;
    for (i in pressed){
        if (pressed[i]) console.log(i), flag = true;
    }
    if (!flag) console.log("No keys pressed");
}

document.addEventListener('keydown', onkeypressed);
document.addEventListener('keyup', onkeypressed);
setInterval(checkkeys, timeout)


