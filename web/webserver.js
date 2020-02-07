var express = require('express');
var app = express();
var http = require('http');

var exec  = require('child_process').exec;
var fs =  require('fs');
var myJSONObject = {};
var RRE_Calculation = {};

var run_rre_calculation = function(rows, values) {
    exec('/usr/bin/python3 /home/hamzamian_patwa/Reduced_Row_Echelon_Calculator/rref_calculator.py -rownum ' + rows + ' -colnum ' + columns + ' -values ' + values + ' -show_equations ' + show_equations, function (error, stdout, stderr) {
    if (error != null) {
      RRE_Calculation.info = { "RRE": error};
      RRE_Calculation.status = false;
      console.log('An Exec Error occured: ' + error);
    } else if (stderr.length != 0) {
      RRE_Calculation.info = { "RRE": stderr};
      RRE_Calculation.status = false;
      console.log('An Exec Error occured on STDERR: ' + stderr);
    } else if (stdout.length != 0 || stdout != null) {
      RRE_Calculation.info = { "RRE": stdout};
      RRE_Calculation.status = true;
      console.log(stdout);
    } else {
      RRE_Calculation.status = false;
      console.log("Unknown Error Occurred: The output of rref_calculator.py script is empty!");
    }
    });
}

// Setup base directory for html and all other web server files.
app.use(express.static('/home/hamzamian_patwa/Reduced_Row_Echelon_Calculator/web'));

http.createServer(app).listen(8080);

app.get('/run-rre-calculation', function (req, res) {
  run_rre_calculation(req.query.Rows, req.query.MatrixValues);
  var refreshId = setInterval(function() {
      if (RRE_Calculation.status != null) {
        res.json(RRE_Calculation);
        RRE_Calculation.status = null;
        clearInterval(refreshId);
        return;
      }
    }, 100);
});
