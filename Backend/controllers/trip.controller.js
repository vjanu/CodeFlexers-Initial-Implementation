const express = require('express');
const router = express.Router();
const tripModel=require('../models/trip.model');


router.get('/',tripModel.getAllCurrentUsers);
router.put('/update/startRide/:tripId/:passengerId/:driverId',tripModel.UpdateStatus_Start);
router.put('/update/endRide/:tripId/:passengerId/:driverId',tripModel.UpdateStatus_End);
router.get('/specific/:tripId/:passengerId/:driverId',tripModel.getPassengerStartMileage);
router.get('/getDetails/:tripId/:driverId',tripModel.getAllCurrentPassengersDetails);
router.put('/update/fare/:tripId/:passengerId/:driverId',tripModel.UpdateFareCalculation);
router.put('/update/fare/dropoff/:tripId/:passengerId/:driverId',tripModel.UpdateFareCalculationDropOffUser);
router.get('/update/fare/dropoff/:tripId/:passengerId/:driverId',tripModel.getDropOffPassengersDetails);

module.exports=router;
