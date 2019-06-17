var db = require('../db.schema');

// TODO: Create a view for personal rating
//model to get personal rating from table view
exports.getPersonalRatings = function (req,res) {
   var pid = "'" + req.params.personid + "'";
   var sql="SELECT * FROM ratingsView where personID =" + pid //Correct this according to view
   var query= db.query(sql,(err,rows,results)=>{
       if(!err){
           res.send(rows);
        //    console.log(rows);
       }
       else
        console.log(err);
   })
};

//model to get vehicle rating from table view
exports.getvehicleRatings = function (req,res) {
   var vid = "'" + req.params.vehicleid + "'";
   var sql="SELECT * FROM V_VEHICLE_RATING where vehicleID =" + vid
   var query= db.query(sql,(err,rows,results)=>{
       if(!err){
           res.send(rows);
        //    console.log(rows);
       }
       else
        console.log(err);
   })
};

//model to add driver rating
exports.addDriverRating = function (req,res) {
   var rbody = req.body;    
   var avgRating = (rbody.GivenRating + rbody.CalculatedRating)/2;
   var post = {
       TripId:rbody.TripId,
       DriverId:rbody.DriverId,
       RatedBy:rbody.RatedBy,
       GivenRating:rbody.GivenRating,
       CalculatedRating:rbody.CalculatedRating,
       AverageRating:avgRating,
       Compliment:rbody.GivenRating,
       Dissatisfaction:rbody.Dissatisfaction,
       Sentiment :rbody.Sentiment 
   };
   var sql='INSERT INTO rating_driver SET ?'
   var query = db.query(sql,post,(err,rows,results)=>{
       if(!err){
           res.send(rows);
           console.log(rows);
       }
       else
        console.log(err);
   })
};

//model to add driver rating
exports.addVehicleRating = function (req,res) {
   var rbody = req.body;    
   var avgRating = (rbody.GivenRating + rbody.CalculatedRating)/2;
   var post = {
      tripId:rbody.tripId,
      vehicleId:rbody.vehicleId,
      RatedBy:rbody.RatedBy,
      GivenRating:rbody.GivenRating,
      CalculatedRating:rbody.CalculatedRating,
      AverageRating:avgRating,
      Dissatisfaction:rbody.Dissatisfaction,
      Sentiment :rbody.Sentiment 
   };
   var sql='INSERT INTO rating_vehicle SET ?'
   var query = db.query(sql,post,(err,rows,results)=>{
       if(!err){
           res.send(rows);
           console.log(rows);
       }
       else
        console.log(err);
   })
};

//model to add co-passenger rating
exports.addCopassengerRating = function (req,res) {
   var rbody = req.body;    
   var avgRating = (rbody.GivenRating + rbody.CalculatedRating)/2;
   var post = {
      tripId:rbody.tripId,
      CopassengerId:rbody.CopassengerId,
      RatedBy:rbody.RatedBy,
      GivenRating:rbody.GivenRating,
      CalculatedRating:rbody.CalculatedRating,
      AverageRating:avgRating,
      Dissatisfaction:rbody.Dissatisfaction,
      Sentiment :rbody.Sentiment 
   };
   var sql='INSERT INTO rating_copassenger SET ?'
   var query = db.query(sql,post,(err,rows,results)=>{
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
      RID:rbody.RID,
      PUID:rbody.PUID, //rated passenger ID
      DUID:rbody.DUID  //driver ID
   };
   var sql='INSERT INTO reported_driversHide SET ?'
   var query = db.query(sql,post,(err,rows,results)=>{
       if(!err){
           res.send(rows);
           console.log(rows);
       }
       else
        console.log(err);
   })
};