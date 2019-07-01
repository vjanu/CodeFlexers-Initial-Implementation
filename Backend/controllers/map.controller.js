const express = require('express');
const router = express.Router();
const mapModel=require('../models/map.model');

//controller to add trip data
router.post('/', mapModel.addTripData);

//controller to add trip data
router.get('/passenger/:userid', mapModel.getAllUsers);

module.exports=router;