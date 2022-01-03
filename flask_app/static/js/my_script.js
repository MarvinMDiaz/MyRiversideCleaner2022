
var navLinks = document.getElementById("navLinks");


function showMenu(){
    navLinks.style.right = "0";
}

function hideMenu(){
    navLinks.style.right = "-200px";
}

function deleteAlert(){
    var close= document.getElementById("close");
    var Msg= document.getElementById("alertMsg");

    close.remove();
    Msg.remove();
}

// document.write(moment("2012-12-31T23:55:13 Z").format('LLLL'));


