const express = require('express');
const router = express.Router();
const vehicleModel=require('../models/vehicle.model');

router.get('/',vehicleModel.getAllVehicle);
router.get('/specific/:uid',vehicleModel.getSpecificVehicle);
router.get('/specificVID/:uid',vehicleModel.getVehicleIDbyUser);
router.post('/',vehicleModel.addVehicle);
router.delete('/delete/:uid',vehicleModel.deleteSpecificVehicle);
router.put('/update/:uid',vehicleModel.updateSpecificVehicle);

module.exports=router;
