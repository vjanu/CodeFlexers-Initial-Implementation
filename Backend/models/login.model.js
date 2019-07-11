var db = require('../db.schema');

//model to get all users
exports.getUsers = function (req,res) {
   var sql='SELECT * FROM login'
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
exports.getSpecificUserName = function (req,res) {
    var usrname = "'" + req.params.uname + "'";
    var sql="SELECT * FROM login where Username =" + usrname
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
    var UID = "U" + Date.now();
    var post = {
        UserID:UID,
        Username:rbody.Username,
        Password:rbody.Password,
        Email:rbody.Email,
        Status: rbody.Status
    };
    var sql='INSERT INTO login SET ?'
    var query = db.query(sql,post,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log(rows);
        }
        else
         console.log(err);
    })
 };

 //model to add spouse
exports.addSpouse = function (req,res) {
    var rbody = req.body;
    var post = {
        UserID:rbody.UserID,
        Username:rbody.Username,
        Password:rbody.Password,
        Email:rbody.Email,
        Status: rbody.Status
    };
    var sql='INSERT INTO login SET ?'
    var query = db.query(sql,post,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log(rows);
        }
        else
         console.log(err);
    })
 };

//model to get specific users
 exports.getSpecificUser = function (req,res) {
    var username = "'" + req.params.username + "'";
    var password = "'" + req.params.password + "'";
    var sql='SELECT * FROM login WHERE Username ='+username+ 'AND Password ='+password
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log(rows);
            // console.log(password);
        }
        else
         console.log(err);
    })
 };

//model to delete specific users
 exports.deleteSpecificUser = function (req,res) {
    var uid = "'" + req.params.id + "'";
    var sql="DELETE FROM login where UserID =" + uid
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log("Deleted" + uid);
        }
        else
         console.log(err);
    })
 };
