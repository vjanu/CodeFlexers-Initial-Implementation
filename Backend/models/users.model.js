var db = require('../db.schema');

//model to get all users
exports.getAllUsers = function (req,res) {
   var sql='SELECT * FROM users'
   var query= db.query(sql,(err,rows,results)=>{
       if(!err){
           res.send(rows);
        //    console.log(rows);
       }
       else
        console.log(err);
   })
};

//model to get specific users
exports.getSpecificUser = function (req,res) {
    var uid = "'" + req.params.uid + "'";
    var sql="SELECT * FROM users where UserID =" + uid
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
         //    console.log(rows);
        }
        else
         console.log(err);
    })
 };

//model to add users
exports.addUser = function (req,res) {
    var rbody = req.body;       
    var post = {
        UserID:rbody.UserID,
        FullName:rbody.FullName,
        Profession:rbody.Profession,
        Email:rbody.Email,
        Gender:rbody.Gender,
        RName:rbody.RName,
        RPhone:rbody.RPhone,
        Age:rbody.Age,
        img:rbody.img
    };
    var sql='INSERT INTO users SET ?'
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
 exports.deleteSpecificUser = function (req,res) {
    var uid = "'" + req.params.uid + "'";
    var sql="DELETE FROM users where UserID =" + uid
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
 exports.updateSpecificUser= function (req,res) {
    var uid = "'" + req.params.uid + "'";
    var rbody = req.body;

    var sql = "UPDATE users SET FullName=?,Profession=?,Email=?,Age=?,Gender=?,RName=?, RPhone=? WHERE UserID =" + uid
    db.query(sql,[rbody.FullName,rbody.Profession,rbody.Email,rbody.Age,rbody.Gender,rbody.RName,rbody.RPhone], function (err,rows, result) {
        if(!err){
            res.send(rows);
            // console.log(rows);
        }
        else
         console.log(err);
    })
 };