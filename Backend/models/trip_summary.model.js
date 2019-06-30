var db = require('../db.schema');

//model to get summary details
exports.getTripSummaryDetails = function (req,res) {
    var tripId = "'" + req.params.tripId + "'";
    var sql="SELECT StartDate,StartTime,WaitingTime FROM offerride WHERE OID=" + tripId
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows[0]);
             console.log(rows);
        }
        else
         console.log(err);
    })
 };

 //model to get current passengers
exports.getCurrentPassenger = function (req,res) {
    var tripId = "'" + req.params.tripId + "'";
    var sql="SELECT COUNT(*) AS Count FROM current_passengers WHERE trip_status = '1' and tripId=" + tripId
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows[0]);
         //    console.log(rows);
        }
        else
         console.log(err);
    })
 };

