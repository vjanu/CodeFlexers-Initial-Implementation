const mysql = require('mysql');

//database credentials
const db = mysql.createConnection({
    host:'localhost',
    user:'root',//admin
    password:'',//123
    database:'plusgo_local'
})

// const db = mysql.createConnection({
//     host:'db4free.net',
//     user:'cdapadmin',
//     password:'cdapcdap',
//     database:'plusgo'
// }) 

db.connect((err) => {
    if(err){
        console.log("Error");
        throw err;  
    }
    console.log('Mysql Connected...');
})

module.exports = db;
