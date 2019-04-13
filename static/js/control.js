$( document ).ready(function() {
    setContainer();
});

function setBackgroundColor(){
    randomiseColor();
    setInterval(randomiseColor, 1800000);
}

function webSocketHandler(){
    webSocket = new WebSocket('ws://localhost:8000/message');
    webSocket.onmessage = function(event) {
        onMessage(event)
    };   
}

function onMessage(event) {
    console.log(event.data)
    window.eval(event.data) 
}

function randomiseColor(){
    colors = ["Aquamarine", "Goldenrod", "Indianred", "Blueviolet", "Green", "Greenyellow","BlanchedAlmond"];
    prev = [];

    for (i=0; i<6; i++){
        j = Math.floor(Math.random()*colors.length);
        selected = colors[j];
        colors.splice(j,1);
        $("#"+i.toString()).css("background-color",selected);
    }
}

function setContainer(){
    $.ajax({url: "/modules", success: function(result){
        $(".baseContainer").html(result);
        setBackgroundColor();
        webSocketHandler();
      }});
}