var db = require('../db.schema');

//model to get all offerrides
exports.getAllDriverOffers = function (req,res) {
   var sql='SELECT * FROM offerride'
   var query= db.query(sql,(err,rows,results)=>{
       if(!err){
           res.send(rows);
        //    console.log(rows);
       }
       else
        console.log(err);
   })
};


//model to add offer rides
exports.addOfferRide = function (req,res) {
    var rbody = req.body;
    var OID = "O" + Date.now();
    var post = {
        OID:OID,
        UserID:rbody.UserID,
        Source:rbody.Source,
        Destination:rbody.Destination,
        StartDate:rbody.StartDate,
        StartTime:rbody.StartTime,
        WaitingTime:rbody.WaitingTime,

    };
    var sql='INSERT INTO offerride SET ?'
    var query = db.query(sql,post,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log(rows);
        }
        else
         console.log(err);
    })
 };
