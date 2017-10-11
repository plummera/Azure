function updateScroll(){
    var element = document.getElementById("portal");
    element.scrollTop = element.scrollHeight;
}

setInterval(updateScroll,500);
