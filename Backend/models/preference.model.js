var db = require('../db.schema');

//model to get all preference
exports.getAllPreference = function (req,res) {
   var sql='SELECT * FROM preference'
   var query= db.query(sql,(err,rows,results)=>{
       if(!err){
           res.send(rows);
        //    console.log(rows);
       }
       else
        console.log(err);
   })
};

//model to get specific preference
exports.getSpecificPreference = function (req,res) {
    var uid = "'" + req.params.uid + "'";
    var sql="SELECT * FROM preference where UserID =" + uid
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows[0]);
         //    console.log(rows);
        }
        else
         console.log(err);
    })
 };

//model to add preference
exports.addPreference = function (req,res) {
    var rbody = req.body;    
    var PID = "PRF" + Date.now();   
    var post = {
        PID:PID,
        UserID:rbody.UserID,
        GenderP:rbody.GenderP,
        LanguageS:rbody.LanguageS,
        Smoking:rbody.Smoking,
        MusicLover:rbody.MusicLover,
        MotionSickness:rbody.MotionSickness,
        LikeQuietness:rbody.LikeQuietness
    };
    var sql='INSERT INTO preference SET ?'
    var query = db.query(sql,post,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log(rows);
        }
        else
         console.log(err);
    })
 };



//model to delete specific preference
 exports.deleteSpecificPreference = function (req,res) {
    var uid = "'" + req.params.uid + "'";
    var sql="DELETE FROM preference where UserID =" + uid
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log("Deleted" + uid);
        }
        else
         console.log(err);
    })
 };

 //model to update user preference
 exports.updateSpecificPreference = function (req,res) {
    var uid = "'" + req.params.uid + "'";
    var rbody = req.body;
   
    var sql = "UPDATE preference SET GenderP=?,LanguageS=?,Smoking=?,MusicLover=?,MotionSickness=?,LikeQuietness=? WHERE UserID =" + uid
    db.query(sql,[rbody.GenderP,rbody.LanguageS,rbody.Smoking,rbody.MusicLover,rbody.MotionSickness,rbody.LikeQuietness], function (err,rows, result) {
        if(!err){
            res.send(rows);
            // console.log(rows);
        }
        else
         console.log(err);
    })
 };