var db = require('../db.schema');

//model to get all Current Passenger Details

//Note:add cp.price
exports.getAllCurrentUsers = function (req,res) {
  var tripId = "'" + req.params.tripId + "'";
  console.log(tripId)
  var tripId = "'" + req.params.tripId + "'";
   var sql="SELECT  cp.tripId,cp.passengerId,cp.driverId,cp.source,cp.destination,cp.trip_status,cp.price,u.UserID,u.Token,u.FullName FROM current_passengers cp ,  users u where  cp.passengerId = u.UserID and cp.tripId = "+tripId
   var query= db.query(sql,(err,rows,results)=>{
       if(!err){
        res.end(JSON.stringify({'currentUsers':rows}));
        console.log(rows);
       }
       else
        console.log(err);
   })
};

//model to Update when Passenger Start the Trip
exports.UpdateStatus_Start = function (req,res) {
   var tripId = "'" + req.params.tripId + "'";
   var passengerId = "'" + req.params.passengerId + "'";
   var driverId = "'" + req.params.driverId + "'";
   var rbody = req.body;
   console.log(tripId)
   console.log(passengerId)
   console.log(driverId)
   var sql="Update current_passengers SET trip_status=?,startMileage=? Where tripId ="+tripId+" and passengerId ="+ passengerId +" and driverId =" +driverId
   db.query(sql,[rbody.trip_status,rbody.startMileage], function (err,rows, result) {
       if(!err){
         res.send(rows);
       }
       else
        console.log(err);
   })
};


//model to Update when Passenger End the Trip
exports.UpdateStatus_End = function (req,res) {
  
   var tripId = "'" + req.params.tripId + "'";
   var passengerId = "'" + req.params.passengerId + "'";
   var driverId = "'" + req.params.driverId + "'";
   var rbody = req.body;
   console.log(req.trip_status)
   console.log(tripId)
   console.log(passengerId)
   console.log(driverId)
   var sql="Update current_passengers SET trip_status=? Where tripId ="+tripId+" and passengerId ="+ passengerId +" and driverId =" +driverId
   db.query(sql,[rbody.trip_status], function (err,rows, result) {
       if(!err){
         res.send(rows);
       }
       else
        console.log(err);
   })
};



 //get start Mileage of the Specific User
 exports.getPassengerStartMileage = function (req,res) {
   var tripId = "'" + req.params.tripId + "'";
   var passengerId = "'" + req.params.passengerId + "'";
   var driverId = "'" + req.params.driverId + "'";
   var sql="SELECT startMileage from current_passengers where tripId="+tripId+ " and passengerId=" +passengerId+ " and driverId="+ driverId
   var query= db.query(sql,(err,rows,results)=>{
       if(!err){
           //res.send(rows);
           res.end(JSON.stringify({'startMileage':rows}));
           console.log(rows);
       }
       else
        console.log(err);
   })
};


 //get Last Price of the Specific User
 exports.getPassengerPrice = function (req,res) {
  var tripId = "'" + req.params.tripId + "'";
  var passengerId = "'" + req.params.passengerId + "'";
  var driverId = "'" + req.params.driverId + "'";
  var sql="SELECT price from current_passengers where tripId="+tripId+ " and passengerId=" +passengerId+ " and driverId="+ driverId
  var query= db.query(sql,(err,rows,results)=>{
      if(!err){
          //res.send(rows);
          res.end(JSON.stringify({'price':rows}));
          console.log(rows);
      }
      else
       console.log(err);
  })
};


 //get start Mileage of the Specific User
 exports.getAllCurrentPassengersDetails = function (req,res) {
   var tripId = "'" + req.params.tripId + "'";
   var passengerId = "'" + req.params.passengerId + "'";
   var driverId = "'" + req.params.driverId + "'";
   var sql="SELECT passengerId,startMileage,price from current_passengers where tripId="+tripId+ " and trip_status=1 and driverId="+ driverId
   var query= db.query(sql,(err,rows,results)=>{
       if(!err){
           res.send(rows);
           console.log("getAllCurrentPassengersDetails" + rows);
       }
       else
        console.log(err);
   })
};


//Update Price and Mileage
exports.UpdateFareCalculation = function (req,res) {
   var tripId = "'" + req.params.tripId + "'";
   var passengerId = "'" + req.params.passengerId + "'";
   var driverId = "'" + req.params.driverId + "'";
   var rbody = req.body;
   console.log(tripId)
   console.log(passengerId)
   console.log(driverId)
   console.log(rbody.price)
   var sql="Update current_passengers SET startMileage=?,price=? Where tripId ="+tripId+" and passengerId ="+ passengerId +" and driverId =" +driverId + " and trip_status=1"
   db.query(sql,[rbody.startMileage,rbody.price], function (err,rows, result) {
       if(!err){
         res.send(rows);
       }
       else
        console.log(err);
   })
};


//Update Price and Mileage
exports.UpdateFareCalculationDropOffUser = function (req,res) {
   var tripId = "'" + req.params.tripId + "'";
   var passengerId = "'" + req.params.passengerId + "'";
   var driverId = "'" + req.params.driverId + "'";
   var rbody = req.body;
   console.log(tripId)
   console.log(passengerId)
   console.log(driverId)
   var sql="Update current_passengers SET startMileage=?,price=? Where tripId ="+tripId+" and passengerId ="+ passengerId +" and driverId =" +driverId + " and trip_status=2"
   db.query(sql,[rbody.startMileage,rbody.price], function (err,rows, result) {
       if(!err){
         res.send(rows);
       }
       else
        console.log(err);
   })
};

//to get a drop off passenger Details
 exports.getDropOffPassengersDetails = function (req,res) {
   var tripId = "'" + req.params.tripId + "'";
   var passengerId = "'" + req.params.passengerId + "'";
   var driverId = "'" + req.params.driverId + "'";
   var sql="SELECT passengerId,startMileage,price from current_passengers where tripId="+tripId+" and passengerId="+passengerId +" and trip_status=2 and driverId="+driverId
   var query= db.query(sql,(err,rows,results)=>{
       if(!err){
           res.send(rows);
           console.log("getAllCurrentPassengersDetails" + rows);
       }
       else
        console.log(err);
   })
};


//model to add Trip Request 
exports.addRequestTrip = function (req,res) {
  var rbody = req.body;       
  var post = {
    tripId:rbody.tripId,
    passengerId:rbody.passengerId,
    driverId:rbody.driverId, 
    source:rbody.source,
    destination:rbody.destination,
    trip_status:"4",
    startMileage:"0",
    price:"0",
    
  };
  var sql='INSERT INTO current_passengers SET ?'
  var query = db.query(sql,post,(err,rows,results)=>{
      if(!err){
          res.send(rows);
          console.log(rows);
      }
      else
       console.log(err);
  })
};


//Driver Accept the Driver 
exports.AcceptRideRequest = function (req,res) {
  
  var tripId = "'" + req.params.tripId + "'";
  var passengerId = "'" + req.params.passengerId + "'";
  var driverId = "'" + req.params.driverId + "'";
  var rbody = req.body;
  console.log(rbody.trip_status)
  console.log(tripId)
  console.log(passengerId)
  console.log(driverId)
  var sql="Update current_passengers SET trip_status=? Where tripId ="+tripId+" and passengerId ="+ passengerId +" and driverId =" +driverId
  db.query(sql,[rbody.trip_status], function (err,rows, result) {
      if(!err){
        res.send(rows);
      }
      else
       console.log(err);
  })
};


//to update the offride status when driver start the trip
exports.UpdateStatus_start_offerRide = function (req,res) {
  var tripId = "'" + req.params.tripId + "'";
  var rbody = req.body;
  console.log(tripId)
  var sql="Update offerride SET tripStatus = ? Where OID ="+tripId
  db.query(sql,[rbody.tripStatus], function (err,rows, result) {
      if(!err){
        res.send(rows);
      }
      else
       console.log(err);
  })
};

//to update the offride status when driver End the trip
exports.UpdateStatus_end_offerRide = function (req,res) {
  var tripId = "'" + req.params.tripId + "'";
  var rbody = req.body;
  console.log(tripId)
  var sql="Update offerride SET tripStatus = ? Where OID ="+tripId
  db.query(sql,[rbody.tripStatus], function (err,rows, result) {
      if(!err){
        res.send(rows);
      }
      else
       console.log(err);
  })
};


//model to Current Passenger Details move to the Trip History Table
exports.migrateCurrentPassengers = function (req,res) {
  var rbody = req.body;       
  var post = {
    tripId:rbody.tripId,
    passengerId:rbody.passengerId,
    driverId:rbody.driverId, 
    source:rbody.source,
    destination:rbody.destination,
    trip_status:rbody.status,
    fare:rbody.price,
    
  };
  var sql='INSERT INTO trip_history SET ?'
  var query = db.query(sql,post,(err,rows,results)=>{
      if(!err){
          res.send(rows);
          console.log(rows);
      }
      else
       console.log(err);
  })
};


 //model to delete current passengers
 exports.deleteCurrentPassengers = function (req,res) {
  var tripId = "'" + req.params.tripId + "'";
  var sql="DELETE FROM current_passengers WHERE tripId=" + tripId
  var query= db.query(sql,(err,rows,results)=>{
      if(!err){
          res.send(rows);
           console.log(rows);
      }
      else
       console.log(err);
  })
};


//trip use as a passenger
exports.getTripHistoryPassenger = function (req,res) {
  var userId = "'" + req.params.userId + "'";
  var sql="SELECT *  from trip_history where passengerId="+userId
  var query= db.query(sql,(err,rows,results)=>{
      if(!err){
          res.send(rows);
          console.log("getHistoryPassenger" + rows);
      }
      else
       console.log(err);
  })
};


//trip use as a passenger
exports.getTripHistoryDriver = function (req,res) {
  var userId = "'" + req.params.userId + "'";
  var sql="SELECT distinct tripId FROM plusgo.trip_history where driverId ="+userId
  var query= db.query(sql,(err,rows,results)=>{
      if(!err){
          res.send(rows);
          console.log("getHistoryDriver" + rows);
      }
      else
       console.log(err);
  })
};