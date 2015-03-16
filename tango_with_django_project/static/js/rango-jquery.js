$(document).ready( function() {

    $("#about-btn").click( function() {
        alert("You clicked the button using JQuery!");
    });

    $("p").hover( function() {
            $(this).css('color', 'red');
    },
    function() {
            $(this).css('color', 'blue');
    });

    $("#about-btn").addClass('btn btn-primary')

    $("#about-btn").click( function() {
    msgstr = $("#msg").html()
        msgstr = msgstr + "o"
        $("#msg").html(msgstr)
    });

});