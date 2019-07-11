var db = require('../db.schema');


//model to get specific Passenger
exports.getSpecificPassenger = function (req,res) {
    var suid = "'" + req.params.suid + "'";
    var sql="SELECT * FROM spouse where SUID =" + suid
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
         //    console.log(rows);
        }
        else
         console.log(err);
    })
 };

//model to add Spouse
exports.addSpouse = function (req,res) {
    var rbody = req.body;
    var ID = "GS" + Date.now();
    var post = {
        ID:ID,
        SUID:rbody.SUID,
        PUID:rbody.PUID
    };
    var sql='INSERT INTO spouse SET ?'
    var query = db.query(sql,post,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log(rows);
        }
        else
         console.log(err);
    })
 };

//model to get specific Passenger
exports.getDrivers = function (req,res) {
    var puid = "'" + req.params.puid + "'";
    var sql="SELECT u.img, c.passengerId as PUID,c.driverId as DUID,u.Fullname, sum(c.price) as Amt, count(*) as Count FROM current_passengers c, users u where c.driverId = u.UserID and passengerId =" + puid +"GROUP BY PUID,DUID,Fullname , img"
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log(rows);
        }
        else
         console.log(err);
    })
 };

 exports.getTripHistory = function (req,res) {
    var puid = "'" + req.params.puid + "'";
    var duid = "'" + req.params.duid + "'";
    var sql="SELECT source, destination, dateTime, price FROM current_passengers where passengerId =" + puid +"and driverId=" + duid;
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log(rows);
        }
        else
         console.log(err);
    })
 };

 //model to report drivers by passengers
exports.reportDrivers = function (req,res) {
   var rbody = req.body;    
   var post = {
      // RID:rbody.RID,
      PUID:rbody.PUID, //rated passenger ID
      DUID:rbody.DUID  //driver ID
   };
   var sql='INSERT INTO reported_drivers SET ?'
   var query = db.query(sql,post,(err,rows,results)=>{
       if(!err){
           res.send(rows);
         //   console.log(rows);
       }
       else
        console.log(err);
   })
};

exports.checkReportedDriver = function (req,res) {
    var puid = "'" + req.params.puid + "'";
    var duid = "'" + req.params.duid + "'";
    var sql="SELECT * from reported_drivers where PUID =" + puid +"and DUID=" + duid;
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log(rows);
        }
        else
         console.log(err);
    })
 };

 exports.getSpecificReportedList = function (req,res) {
    var puid = "'" + req.params.puid + "'";
    var sql="SELECT DUID from reported_drivers where PUID =" + puid;
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log(rows);
        }
        else
         console.log(err);
    })
 };