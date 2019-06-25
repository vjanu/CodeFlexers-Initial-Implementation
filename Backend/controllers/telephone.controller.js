const express = require('express');
const router = express.Router();
const TelephoneModel=require('../models/telephone.model');


router.get('/specific/:tp',TelephoneModel.checkTpExists);
router.post('/',TelephoneModel.addTpNumbers);

module.exports=router;
