document.querySelector('#room-name-input').focus();
document.querySelector('#room-name-input').onkeyup = function (event) {
    if (event.keyCode === 13) {  // enter, return
        document.querySelector('#room-name-submit').click();
    }
};

document.querySelector('#room-name-submit').onclick = function (event) {
    let roomName = document.querySelector('#room-name-input').value;
    window.location.pathname = '/chat/' + roomName + '/';
};