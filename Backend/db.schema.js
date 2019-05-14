const mysql = require('mysql');

//database credentials
// const db = mysql.createConnection({
//     host:'localhost',
//     user:'root',//admin
//     password:'root',//123
//     database:'plus_go'
// })

const db = mysql.createConnection({
    host:'192.168.1.8',
    user:'admin',
    password:'123',
    database:'plus_go'
}) 

db.connect((err) => {
    if(err){
        console.log("Error");
        throw err;  
    }
    console.log('Mysql Connected...');
})

module.exports = db;
