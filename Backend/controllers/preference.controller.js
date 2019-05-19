const express = require('express');
const router = express.Router();
const preferenceModel=require('../models/preference.model');

router.get('/',preferenceModel.getAllPreference);
router.get('/specific/:uid',preferenceModel.getSpecificPreference);
router.post('/',preferenceModel.addPreference);
router.delete('/delete/:uid',preferenceModel.deleteSpecificPreference);
router.put('/update/:uid',preferenceModel.updateSpecificPreference);

module.exports=router;
