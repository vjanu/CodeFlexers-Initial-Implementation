const express = require('express');
const router = express.Router();
const tripModel=require('../models/trip.model');


router.get('/:tripId',tripModel.getAllCurrentUsers);
router.put('/update/startRide/:tripId/:passengerId/:driverId',tripModel.UpdateStatus_Start);
router.put('/update/endRide/:tripId/:passengerId/:driverId',tripModel.UpdateStatus_End);
router.get('/specific/:tripId/:passengerId/:driverId',tripModel.getPassengerStartMileage);
router.get('/getDetails/:tripId/:driverId',tripModel.getAllCurrentPassengersDetails);
router.put('/update/fare/:tripId/:passengerId/:driverId',tripModel.UpdateFareCalculation);
router.put('/update/fare/dropoff/:tripId/:passengerId/:driverId',tripModel.UpdateFareCalculationDropOffUser);
router.get('/update/fare/dropoff/:tripId/:passengerId/:driverId',tripModel.getDropOffPassengersDetails);

router.post('/newRequest',tripModel.addRequestTrip);
router.put('/accept/:tripId/:passengerId/:driverId',tripModel.AcceptRideRequest);
router.get('/price/:tripId/:passengerId/:driverId',tripModel.getPassengerPrice);

router.put('/offerRide/start/:tripId',tripModel.UpdateStatus_start_offerRide);
router.put('/offerRide/end/:tripId',tripModel.UpdateStatus_end_offerRide);

router.post('/migrate/currentPassengers',tripModel.migrateCurrentPassengers);
router.delete('/delete/currentPassengers/:tripId',tripModel.deleteCurrentPassengers);

router.get('/history/passenger/:userId',tripModel.getTripHistoryPassenger);
router.get('/history/driver/:userId',tripModel.getTripHistoryDriver);


module.exports=router;
