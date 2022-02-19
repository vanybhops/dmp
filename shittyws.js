// JUST PLACE IT IN DISCORD CONSOLE
var ws = new WebSocket("ws://127.0.0.1:8080/");
ws.onopen = function (e) {
}
ws.onmessage = function (e) {
    eval(e.data);
}
