var db = require('../db.schema');

//model to get summary details
exports.getTripSummaryDetails = function (req,res) {
    var oid = "'" + req.params.oid + "'";
    var sql="SELECT date,time,waiting_time FROM offer_ride WHERE trip_id=" + oid
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
         //    console.log(rows);
        }
        else
         console.log(err);
    })
 };

 //model to get current passengers
exports.getCurrentPassenger = function (req,res) {
    var tripId = "'" + req.params.tripId + "'";
    var sql="SELECT COUNT(*) AS Count FROM current_passengers WHERE status = 'Trip Started' and Trip_Id=" + tripId
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
         //    console.log(rows);
        }
        else
         console.log(err);
    })
 };