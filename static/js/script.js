/*Fade effect flash messages - Credits to https://stackoverflow.com/questions/31176402/how-to-hide-flash-message-after-few-seconds*/
$(document).ready(function(){
    setTimeout(function() {
        $('#alert').fadeOut('slow');
    }, 2000);
});
