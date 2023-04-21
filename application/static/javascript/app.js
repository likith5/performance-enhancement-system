var xValues =  ['Strong in Tech',
'Project Management role',
'Customer facing roles',
'Team lead',
'Design profile',
'sales/marketing role'
]
;
var yValues = [8, 5, 6, 9, 5,8];
var barColors = [
  "#b91d47",
  "#00aba9",
  "#2b5797",
  "#e8c3b9",
  "#1e7145",
  "#5478F6"
];

new Chart("myChart", {
  type: "pie",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues,
      color:'#5478F6'
    }]
  },
  options: {
    title: {
      display: true,
    }
  }
});




var xValues = ["Python", "CSS", "JAVA", "SQL", "JAVASCRIPT","Flask"];
var yValues = [5,6,8,3,9,4];
var barColors = ["red", "green","blue","orange","brown","pink"];

new Chart("myBar", {
  type: "horizontalBar",
  data: {
  labels: xValues,
  datasets: [{
    backgroundColor: barColors,
    data: yValues
  }]
},
  options: {
    legend: {display: false},
    title: {
      display: true,
      
    },
    scales: {
      xAxes: [{ticks: {min: 1, max:10}}]
    }
  }
});
