
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

$(document).ready(function () {
    $(".program").each(function () {
        var $bar = $(this).find(".halfbar");
        var $val = $(this).find(".percentage");
        var perc = parseInt($val.text(), 10);

        $({ p: 0 }).animate({ p: perc }, {
            duration: 2000,
            easing: "swing",
            step: function (p) {
                $bar.css({
                    transform: "rotate(" + (45 + (p * 1.8)) + "deg)", // 100%=180° so: ° = % * 1.8
                    // 45 is to add the needed rotation to have the green borders at the bottom
                });
                $val.text(p | 0);
            }
        });
    });
});   