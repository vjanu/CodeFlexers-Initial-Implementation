const express = require('express');
const router = express.Router();
const accidentmodel = require('../models/roadcause.model');

//insert accident data and images
router.post('/', accidentmodel.insertAccident)

module.exports = router;