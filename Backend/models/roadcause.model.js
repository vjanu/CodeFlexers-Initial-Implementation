const firebase = require('../db.firebaseconfig');
const AWS = require('../amazons3config');

//model to insert accident/traffic data
exports.insertAccident = function(req, res){

    let type = req.body.type;
    let username = req.body.username;
	let destination = req.body.destination;
	let situation = req.body.situation;
    let latitude = req.body.latitude;
    let longitude = req.body.longitude;
    let image;
    let status= req.body.status;

    /** Related with amazon S3 */

    //configuring parameters
    let s3Bucket = new AWS.S3({params: {Bucket: 'codeflexerss3bucket', Key : "folder/"+Date.now()}});

    img_buffer = new Buffer(req.body.image.replace(/^data:image\/\w+;base64,/, ""),'base64');
    console.log("Image : ", img_buffer);
    let data = {
        Key: req.body.username, 
        Body: img_buffer,
        ContentEncoding: 'base64',
        ContentType: 'image/jpeg',
        ACL:'public-read'
    };

    //upload image to s3 bucket
    let promise = new Promise((resolve, reject) => {
        s3Bucket.upload(data, function(err, data){
            if (err) { 
                console.log(err);
                console.log('Error occered while uploading the image: ', data); 
                return reject(err);
            } else {
                console.log('Image successfully uploaded', data.Location);
                image = data.Location;
                return resolve();
            }
        });
    });

    /** Related with amazon S3 */

    let base_url = '/accident/';
    if(type == "TRAFIC")
        base_url = '/traffic/'
        
    //Add trafic data to firbase
    let referencePath = base_url + Date.now();
    let userReference = firebase.database().ref(referencePath);
    
    promise.then(function(results){
        userReference.set({destination: destination, situation: situation, latitude: latitude, longitude: longitude, image: image, status: status, username: username}, 
            function(error) {
               if (error) {
                   res.send("Error occured while inserting" + error);
               } 
               else {
                   res.send("Data inserted successfully.");
               }
       });
    });
};