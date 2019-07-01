const express = require('express');
const router = express.Router();
const ratingModel = require('../models/rating.model');


 router.get('/personals/:personid',ratingModel.getPersonalRatings);
 router.get('/vehicles/:vehicleid',ratingModel.getvehicleRatings);
 router.get('/copassengerslist/:tripId',ratingModel.getCopassengerList);
 router.post('/driver-rating',ratingModel.addDriverRating);
 router.post('/passenger-rating',ratingModel.addPassengerRating);
 router.post('/copassenger-rating',ratingModel.addCopassengerRating);
 router.post('/vehicle-rating',ratingModel.addVehicleRating);
 router.post('/reportDrivers',ratingModel.reportDrivers);

module.exports=router;