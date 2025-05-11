var name = "Jason";
var result = [{"Module Code":"EG1234","Grade":"A","Credit":4},
{"Module Code":"EG1298","Grade":"B+","Credit":4},
{"Module Code":"EG2255","Grade":"C","Credit":2},

];

var gradeToPoint = {
    "A":4.0,
    "B+":3.5,
    "B":3.0,
    "C+":2.5,
    "C":2.0,

  
};

function calculateGPA(){
    var totalCredit = 0;
    var totalGradePoint = 0;


    student.results.forEach(function(result){
        console.log(result);
        var grade = result.Grade;
        var credit = result.Credit;
        totalCredit+=credit;
        var point = gradeToPoint[grade];
        console.log("Grade "+grade+" is "+point+" points ");
        totalGradePoint+=point*credit;
    })
    
    var gpa = totalGradePoint/totalCredit;
    console.log("Gpa for Jason is "+gpa);
}

