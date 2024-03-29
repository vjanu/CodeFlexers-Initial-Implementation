var db = require('../db.schema');

// TODO: Create a view for personal rating
//model to get personal rating from table view
exports.getPersonalRatings = function (req,res) {
   var pid = "'" + req.params.personid + "'";
   var sql="SELECT * FROM V_PERSONAL_RATING where UID =" + pid //Correct this according to view
   var query= db.query(sql,(err,rows,results)=>{
       if(!err){
        //res.end(JSON.stringify({'PRating':rows}));
        res.send(rows);
           console.log(rows);
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

//model to get vehicle rating from table view
exports.getCopassengerList = function (req,res) {
   var TripID = "'" + req.params.tripId + "'";
   var sql="SELECT * FROM V_COPASSENGERS_IN_TRIPS where TripID =" + TripID
   var query= db.query(sql,(err,rows,results)=>{
       if(!err){
           res.send(rows);
        //    console.log(rows);
       }
       else
        console.log(err);
   })
};

//model to add driver rating by passenger
exports.addDriverRating = function (req,res) {
   var rbody = req.body;    
   var avgRating = (parseInt(rbody.GivenRating) + parseInt(rbody.CalculatedRating))/2.0;
   var post = {
      TripId:rbody.TripId,
      UserID:rbody.UserID,
      UserType:"driver",
      RatedBy:rbody.RatedBy,
      GivenRating:rbody.GivenRating,
      CalculatedRating:rbody.CalculatedRating,
      AverageRating:avgRating,
      Compliment:rbody.Compliment,
      Dissatisfaction:rbody.Dissatisfaction,
      Sentiment :rbody.Sentiment 
   };
   var sql='INSERT INTO rating_personal SET ?'
   var query = db.query(sql,post,(err,rows,results)=>{
       if(!err){
           res.send(rows);
         //   console.log(rows);
       }
       else
        console.log(err);
   })
};

//model to add passenger rating by driver
exports.addPassengerRating = function (req,res) {
   var rbody = req.body;    
   var avgRating = (parseInt(rbody.GivenRating) + parseInt(rbody.CalculatedRating))/2.0;
   var post = {
      TripId:rbody.TripId,
      UserID:rbody.UserID,
      UserType:"passenger",
      RatedBy:rbody.RatedBy,
      GivenRating:rbody.GivenRating,
      CalculatedRating:rbody.CalculatedRating,
      AverageRating:avgRating,
      Compliment:rbody.Compliment,
      Dissatisfaction:rbody.Dissatisfaction,
      Sentiment :rbody.Sentiment 
   };
   var sql='INSERT INTO rating_personal SET ?'
   var query = db.query(sql,post,(err,rows,results)=>{
       if(!err){
           res.send(rows);
         //   console.log(rows);
       }
       else
        console.log(err);
   })
};

//model to add co-passenger rating by passenger
exports.addCopassengerRating = function (req,res) {
   var rbody = req.body;    
   var avgRating = (parseInt(rbody.GivenRating) + parseInt(rbody.CalculatedRating))/2.0;
   var post = {
      TripId:rbody.TripId,
      UserID:rbody.UserID,
      UserType:"copassenger",
      RatedBy:rbody.RatedBy,
      GivenRating:rbody.GivenRating,
      CalculatedRating:rbody.CalculatedRating,
      AverageRating:avgRating, // This is inserted automatically 
      Dissatisfaction:rbody.Dissatisfaction,
      Sentiment :rbody.Sentiment 
   };
   var sql='INSERT INTO rating_personal SET ?'
   var query = db.query(sql,post,(err,rows,results)=>{
       if(!err){
           res.send(rows);
         //   console.log(rows);
       }
       else
        console.log(err);
   })
};

//model to add driver rating
exports.addVehicleRating = function (req,res) {
   var rbody = req.body;    
   var avgRating = (parseInt(rbody.GivenRating) + parseInt(rbody.CalculatedRating))/2.0;
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
         //   console.log(rows);
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




//model to get personal rating from table view response as a JSON Object
exports.getPersonalRatingsObject = function (req,res) {
   var pid = "'" + req.params.personid + "'";
   var sql="SELECT * FROM V_PERSONAL_RATING where UID =" + pid //Correct this according to view
   var query= db.query(sql,(err,rows,results)=>{
       if(!err){
       // res.end(JSON.stringify({'PRating':rows}));
        res.send(rows[0]);
           console.log(rows);
       }
       else
        console.log(err);
   })
};

//model to get vehicle rating from table view response as a JSON Object
exports.getvehicleRatingsObject = function (req,res) {
   var vid = "'" + req.params.vehicleid + "'";
   var sql="SELECT * FROM V_VEHICLE_RATING where vehicleID =" + vid
   var query= db.query(sql,(err,rows,results)=>{
       if(!err){
           res.send(rows[0]);
            console.log(rows);
       }
       else
        console.log(err);
   })
};

//model to get reported drivers
exports.getReportedDrivers = function (req,res) {
    var uid = "'" + req.params.uid + "'";
    var sql="SELECT * FROM reported_drivers where PUID =" + uid
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
         //    console.log(rows);
        }
        else
         console.log(err);
    })
 };

