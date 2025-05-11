{/* <html>
<head></head>
<body>
    <header></header>
    <script src="jquery.min.js"></script> */}
{/* <script> */}

function add(a,b){
   return a+b;
}

function subtract(a,b){
    return a-b;
}

function multiply(a,b){
    return a*b;
}

function divide(a,b){
    return a/b;
}

function specialOperation(x,y,operation){
    console.log("you have passed in a function named:" + operation);
    console.log(operation);
    console.log(operation(x,y));
}

specialOperation(35,20,add);
specialOperation(25,13,multiply);

// </script>
// </body>
// </html>