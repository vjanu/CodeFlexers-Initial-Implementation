const express = require('express');
const router = express.Router();
const availableDriverListModel=require('../models/availableDriverList.model');


router.get('/driver/:uid',availableDriverListModel.getSpecificDriverDetails);


module.exports=router;
