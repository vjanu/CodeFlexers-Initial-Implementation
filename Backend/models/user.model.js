var db = require('../db.schema');

//model to get all users
exports.getUsers = function (req,res) {
   var sql='SELECT * FROM user'
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
    var sql="SELECT * FROM user where Username =" + usrname
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
    if ((rbody.role == "student")||(rbody.role == "Student"))
        var UID = "S" + Date.now();
    else
        var UID = "T" + Date.now();
    var post = {
        UserID:UID,
        Username:rbody.Username,
        Password:rbody.Password,
        Name:rbody.Name,
        Role:rbody.Role
    };
    var sql='INSERT INTO user SET ?'
    var query = db.query(sql,post,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            // console.log(rows);
        }
        else
         console.log(err);
    })
 };

//model to get specific users
 exports.getSpecificUser = function (req,res) {
    var username = "'" + req.params.username + "'";
    var password = "'" + req.params.password + "'";
    var sql='SELECT * FROM user WHERE Username ='+username+ 'AND Password ='+password
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
    var id = "'" + req.params.id + "'";
    var sql="DELETE FROM user where UserID =" + id
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log("Deleted" + id);
        }
        else
         console.log(err);
    })
 };
