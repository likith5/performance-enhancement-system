
function animateCircularProgress(circularProgress, progressValue) {
    var progressStartValue = 0;
    var progressEndValue = parseInt(progressValue.text(), 10);
    var speed = 300;

    var progress = setInterval(function() {
        progressStartValue++;

        progressValue.text(progressStartValue + "/5");
        circularProgress.css("background", `conic-gradient(#423FB9 ${progressStartValue * 72}deg, #ededed 0deg)`);

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


function animateLinearProgress(linearProgress, progressValue) {
    var progressStartValue = 0;
    var progressEndValue = parseInt(progressValue.text(), 10);
    var speed = 10;

    var progress = setInterval(function() {
        progressStartValue++;

        linearProgress.css("width", (progressStartValue*100)/5 + "%");
        // progressValue.text(progressStartValue + "%");

        if (progressStartValue == progressEndValue) {
            clearInterval(progress);
        }
    }, speed);
}

$(document).ready(function() {
    var linearProgressElements = $(".progress-bari");
    var progressValueElements = $(".linear-value");

    linearProgressElements.each(function(index) {
        animateLinearProgress($(this), progressValueElements.eq(index));
    });
});

$(document).ready(function() {
    $(".program").each(function() {
      var $bar = $(this).find(".halfbar");
      var $val = $(this).find(".percentage");
      var perc = parseInt($val.text(), 10);

      $({ p: 0 }).animate({ p: perc }, {
        duration: 2000,
        easing: "swing",
        step: function(p) {
          $bar.css({
            transform: "rotate(" + (45 + (p * 36)) + "deg)", // 100%=180° so: ° = % * 1.8
            // 45 is to add the needed rotation to have the green borders at the bottom
          });
          $val.text(p | 0);
        }
      });
    });
  });
  const ctx = document.getElementById('myCharti');
  
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Communication', 'Presentation', 'Technical', 'Result oriented', 'Project Management', 'Interpersonal','Leadership','General knowledge','Time Management','Creativity'],
      datasets: [{
        label: 'Test1',
        data:  [1,2,3,4,5,4,3,2,1,4],
        borderWidth: 1
      },
      {
          label: 'Test2',
          data: [2, 1, 3, 5, 2, 3,4,3,5,1],
          borderWidth: 1
        },
        {
          label: 'test3',
          data: [2, 1, 3, 5, 2, 3,2,3,5,3],
          borderWidth: 1
        }]
    },
    options: {
        scales: {
            x: {
              grid: {
                display: true, // hide x-axis grid lines
              }
            },
            y: {
              grid: {
                display: false, // hide y-axis grid lines
              }
            }
          }
    }
  });
  const myline = document.getElementById('myline');




  new Chart(myline, {
    type: 'line',
    data: {
      labels: ['Test1', 'Test2', 'Test3'],
      datasets: [{
        label: 'Test graph',
        data: [ 1,  2, 5],
        borderWidth: 1
      }]
    },
    options: {
        scales: {
            x: {
              grid: {
                display: false, // hide x-axis grid lines
              }
            },
            y: {
              grid: {
                display: false, // hide y-axis grid lines
              },
              ticks: {
                stepSize: 1, // set the step size between values
              }
            }
          }
    }
  });

