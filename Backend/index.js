const express = require('express');
const bodyparser = require('body-parser');
const cors = require('cors');
const routes = require('./routes');
var fs = require('fs');
const multer = require('multer');
var multipart = require('connect-multiparty');
const app = express();

app.use(bodyparser.json());
app.use('/',routes);

//to get the path of images
var publicDir = require('path').join(__dirname,'/images');
app.use('/images',express.static(publicDir));

app.post('/upload',multipart(),function(req, res) {
	console.log("started");
	console.log(req.files.image.originalFilename);
	console.log(req.files.image.path);
		fs.readFile(req.files.image.path, function (err, data){
		var dirname = "../Backend";
		var newPath = dirname + "/images/" + req.files.image.originalFilename;
		fs.writeFile(newPath, data, function (err) {
			if(err){
				res.status(400).json({message: 'Cannot Upload Now!'})

			}
			else {
				res.status(200).json({message: 'Image Uploaded Successfully!', data})

			}
		});
	});
});

//to listen to the port 8083
app.listen(8083,err => {
    if(err){
        console.log(err);
        process.exit(-1);
    }
    console.log('connected to localhost at post 8083');
});
