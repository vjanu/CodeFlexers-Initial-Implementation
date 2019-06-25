var db = require('../db.schema');

//model to get all vehicle
exports.getAllVehicle = function (req,res) {
   var sql='SELECT * FROM vehicle'
   var query= db.query(sql,(err,rows,results)=>{
       if(!err){
           res.send(rows);
        //    console.log(rows);
       }
       else
        console.log(err);
   })
};

//model to get specific vehicle
exports.getSpecificVehicle = function (req,res) {
    var uid = "'" + req.params.uid + "'";
    var sql="SELECT * FROM vehicle where UserID =" + uid
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows[0]);
             console.log(rows[0]);
        }
        else
         console.log(err);
    })
 };

//model to add vehicle
exports.addVehicle = function (req,res) {
    var rbody = req.body;    
    var VID = "V" + Date.now();   
    var post = {
        VehicleID:VID,
        UserID:rbody.UserID,
        Brand:rbody.Brand,
        Model:rbody.Model,
        VNumber:rbody.VNumber,
        Mileage:rbody.Mileage,
        MYear:rbody.MYear,
        RYear:rbody.RYear,
        FuelType:rbody.FuelType,
        TType:rbody.TType,
        EngineCapacity:rbody.EngineCapacity,
        FrontView:rbody.FrontView
    };
    var sql='INSERT INTO vehicle SET ?'
    var query = db.query(sql,post,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log(rows);
        }
        else
         console.log(err);
    })
 };



//model to delete specific vehicle
 exports.deleteSpecificVehicle = function (req,res) {
    var uid = "'" + req.params.uid + "'";
    var sql="DELETE FROM vehicle where UserID =" + uid
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log("Deleted" + uid);
        }
        else
         console.log(err);
    })
 };

 //model to update vehicle
 exports.updateSpecificVehicle = function (req,res) {
    var uid = "'" + req.params.uid + "'";
    var rbody = req.body;
   
 
    var sql = "UPDATE vehicle SET Brand=?,Model=?, Mileage=?,MYear=?,RYear=?,FuelType=?,TType=?,EngineCapacity=?,FrontView=?WHERE UserID =" + uid
    db.query(sql,[rbody.Brand,rbody.Model,rbody.Mileage,rbody.MYear,rbody.RYear,rbody.FuelType,rbody.TType,rbody.EngineCapacity,rbody.FrontView], function (err,rows, result) {
        if(!err){
            res.send(rows);
            // console.log(rows);
        }
        else
         console.log(err);
    })
 };