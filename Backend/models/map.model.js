var db = require('../db.schema');

//model to insert trip data
exports.addTripData = function(req, res){

    console.log(req);

    let rbody = req.body;

    let startlatlong = rbody.source_lat + "," + rbody.source_long;
    let destinationlatlong = rbody.destination_long + "," + rbody.destination_lat;

    var post = {
        UserID:rbody.userid,
        StartingLoc: startlatlong,
        DestinationLoc: destinationlatlong
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