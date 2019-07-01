const express = require('express');
const router = express.Router();
const tripSummaryModel=require('../models/trip_summary.model');


router.get('/get/:tripId',tripSummaryModel.getTripSummaryDetails);
router.get('/currentPassenger/:tripId',tripSummaryModel.getCurrentPassenger);
router.get('/currentPassenger/accept/:tripId',tripSummaryModel.getAcceptPassenger);


module.exports=router;
