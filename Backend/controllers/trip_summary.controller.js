const express = require('express');
const router = express.Router();
const tripSummaryModel=require('../models/trip_summary.model');


router.get('/:oid',tripSummaryModel.getTripSummaryDetails);
router.get('/:tripId',tripSummaryModel.getCurrentPassenger);


module.exports=router;
