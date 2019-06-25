var db = require('../db.schema');

//model to get all Current Passenger Details
exports.getAllCurrentUsers = function (req,res) {
   var sql="SELECT  cp.tripId,cp.passengerId,cp.driverId,cp.source,cp.destination,ts.description,u.UserID,u.Token,u.FullName FROM current_passengers cp , tripStatus ts, users u where cp.trip_status = ts.statusId and cp.passengerId = u.UserID"
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
           res.send(rows[0]);
           console.log(rows[0]);
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
           console.log("getAllCurrentPassengersDetails" + rows[0]);
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
  console.log(tripId)
  console.log(passengerId)
  console.log(driverId)
  var sql="Update current_passengers SET trip_status=0 Where tripId ="+tripId+" and passengerId ="+ passengerId +" and driverId =" +driverId
  db.query(sql,[rbody.trip_status], function (err,rows, result) {
      if(!err){
        res.send(rows);
      }
      else
       console.log(err);
  })
};