
function animateCircularProgress(circularProgress, progressValue) {
    var progressStartValue = 0;
    var progressEndValue = parseInt(progressValue.text(), 10);
    var speed = 30;

    var progress = setInterval(function() {
        progressStartValue++;

        progressValue.text(progressStartValue + "%");
        circularProgress.css("background", `conic-gradient(#423FB9 ${progressStartValue * 3.6}deg, #ededed 0deg)`);

        if (progressStartValue == progressEndValue) {
            clearInterval(progress);
        }
    }, speed);
}

$(document).ready(function() {
    var circularProgressElements = $(".circular-progress");
    var progressValueElements = $(".progress-value");

    circularProgressElements.each(function(index) {
        animateCircularProgress($(this), progressValueElements.eq(index));
    });
});

