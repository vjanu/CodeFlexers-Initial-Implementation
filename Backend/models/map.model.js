var db = require('../db.schema');

//model to insert trip data
exports.addTripData = function(req, res){

    console.log(req);

    let rbody = req.body;
    var SID = "S" + Date.now(); 

    var post = {
        SID: SID,
        UserID:rbody.UserID,
        StartingLat: rbody.StartingLat,
        StartingLong: rbody.StartingLong,
        DestinationLat: rbody.DestinationLat,
        DestinationLong: rbody.DestinationLong
    };

    console.log(post);

    var sql='INSERT INTO searching_destination SET ?'
    var query = db.query(sql,post,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log(rows);
        }
        else
         console.log(err);
    })
};


//get passenger location by userID
exports.getAllUsers = function (req,res) {
    var userid = "'" + req.params.userid + "'";
    var sql="SELECT * FROM searching_destination WHERE UserID =" + userid
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log(rows);
        }
        else
         console.log(err);
    })
 };