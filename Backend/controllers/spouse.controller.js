const express = require('express');
const router = express.Router();
const spouseModel=require('../models/spouse.model');


//controller to validate users
router.get('/specific/:suid',spouseModel.getSpecificPassenger);
//controller to add users
router.post('/',spouseModel.addSpouse);
router.post('/report',spouseModel.reportDrivers);
router.get('/:puid',spouseModel.getDrivers);
router.get('/specific/report/passenger/:puid',spouseModel.getSpecificReportedList);
router.get('/:puid/:duid',spouseModel.getTripHistory);
router.get('/available/:puid/:duid',spouseModel.checkReportedDriver);


module.exports=router;
