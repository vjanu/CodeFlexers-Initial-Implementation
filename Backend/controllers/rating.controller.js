const express = require('express');
const router = express.Router();
const ratingModel = require('../models/rating.model');


 router.get('/:personid',ratingModel.getPersonalRatings);
 router.get('/:vehicleid',ratingModel.getvehicleRatings);
 router.post('/driver-rating',ratingModel.addDriverRating);
 router.post('/passenger-rating',ratingModel.addPassengerRating);
 router.post('/copassenger-rating',ratingModel.addCopassengerRating);
 router.post('/vehicle-rating',ratingModel.addVehicleRating);
 router.post('/reportDrivers',ratingModel.reportDrivers);

module.exports=router;