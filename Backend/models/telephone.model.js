var db = require('../db.schema');

exports.checkTpExists= function (req,res) {
    var tp = "'" + req.params.tp + "'";
    var sql="SELECT * FROM telephone_numbers where telephone =" + tp
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
         //    console.log(rows);
        }
        else
         console.log(err);
    })
 };


exports.addTpNumbers = function (req,res) {
    var rbody = req.body;    
    var TID = "T" + Date.now();   
    var post = {
        TelephoneID:TID,
        Telephone:rbody.Telephone
    };
    var sql='INSERT INTO telephone_numbers SET ?'
    var query = db.query(sql,post,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log(rows);
        }
        else
         console.log(err);
    })
 };
