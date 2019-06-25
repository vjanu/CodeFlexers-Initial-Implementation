var db = require('../db.schema');

//model to get all payments
exports.getAllPayments = function (req,res) {
   var sql='SELECT * FROM payment_details'
   var query= db.query(sql,(err,rows,results)=>{
       if(!err){
           res.send(rows);
        //    console.log(rows);
       }
       else
        console.log(err);
   })
};

//model to get specific payment
exports.getSpecificPayment = function (req,res) {
    var uid = "'" + req.params.uid + "'";
    var sql="SELECT * FROM payment_details where UserID =" + uid
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
         //    console.log(rows);
        }
        else
         console.log(err);
    })
 };

//model to add payment
exports.addPayment = function (req,res) {
    var PaymentID = "PAY" + Date.now();
    var rbody = req.body;       
    var post = {
        PaymentID:PaymentID,
        UserID:rbody.UserID,
        CardNo:rbody.CardNo,
        ExDate:rbody.ExDate,
        CVC:rbody.CVC
    };
    var sql='INSERT INTO payment_details SET ?'
    var query = db.query(sql,post,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log(rows);
        }
        else
         console.log(err);
    })
 };



//model to delete specific users
 exports.deleteSpecificPayment = function (req,res) {
    var uid = "'" + req.params.uid + "'";
    var sql="DELETE FROM payment_details where UserID =" + uid
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log("Deleted" + uid);
        }
        else
         console.log(err);
    })
 };

 //model to update user details
 exports.updateSpecificPayment = function (req,res) {
    var uid = "'" + req.params.uid + "'";
    var rbody = req.body;

    var sql = "UPDATE payment_details SET CardNo=?,ExDate=?,CVC=? WHERE UserID =" + uid
    db.query(sql,[rbody.CardNo,rbody.ExDate,rbody.CVC], function (err,rows, result) {
        if(!err){
            res.send(rows);
            // console.log(rows);
        }
        else
         console.log(err);
    })
 };