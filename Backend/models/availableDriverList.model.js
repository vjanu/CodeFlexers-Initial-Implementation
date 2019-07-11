var db = require('../db.schema');

//model to get specific vehicle
exports.getSpecificDriverDetails = function (req,res) { //time  
    console.log(req.params.uid);
    
    //var uid = "'" + req.params.uid + "'";
    var data = req.params.uid;
    console.log(Object.keys(data).length);
    if(Object.keys(data).length == 2){
        console.log("No Drivers");
        res.send("No Drivers");
    }
    else{
        console.log("Drivers");
    //var data1=['U1558711443506', 'U1558711443507', 'U1558711443512', 'U1558711443513', 'U1558711443514']

    var x = data.replace('[','')
    var y = x.replace(']','')
    //var z = y.replace(/\s/g,'')
    //var queryData=[z];
    //var queryData1=[data1];

// console.log("wee: "+queryData);
// console.log("qqq: "+z);
// console.log("goo: "+queryData1);

    var sql="SELECT u.FullName,u.img,u.UserID,u.Token, v.Model, r.AverageRating, o.OID, o.Source, o.Destination, o.StartTime, o.WaitingTime FROM users u,vehicle v, rating_personal r, offerride o where u.UserID = v.UserID and u.UserID = r.UserID and u.UserID = o.UserID and u.UserID in("+y+")" 
    var query= db.query(sql,(err,rows,results)=>{
        if(!err){
            res.send(rows);
            console.log(rows);
        }
        else
         console.log(err);
    })
}
 };
