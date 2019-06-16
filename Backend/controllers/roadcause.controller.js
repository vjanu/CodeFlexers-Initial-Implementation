const express = require('express');
const router = express.Router();
const accidentmodel = require('../models/roadcause.model');

//insert accident data
router.post('/', accidentmodel.insertAccident)

module.exports = router;