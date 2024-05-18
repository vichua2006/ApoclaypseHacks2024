var pressed = [];
const timeout = 1000;

function onkeypressed(e){
    pressed[e.keyCode] = e.type == 'keydown';
}

function checkkeys(){
    let flag = false;
    var downed = []
    for (i in pressed){
        if (pressed[i]) console.log(i), downed.push(i) , flag = true;
    }
    if (!flag) console.log("No keys pressed");

    $.ajax({ 
        url: '/receive_keypress', 
        type: 'POST', 
        data: JSON.stringify({ 'value': downed }), 
        contentType: 'application/json',
        error: function(error) { 
            console.log(error); 
        } 
    }); 
}

document.addEventListener('keydown', onkeypressed);
document.addEventListener('keyup', onkeypressed);
setInterval(checkkeys, timeout)


