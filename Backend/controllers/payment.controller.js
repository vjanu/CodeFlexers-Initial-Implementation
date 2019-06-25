const express = require('express');
const router = express.Router();
const payModel=require('../models/payment.model');

router.get('/',payModel.getAllPayments);
router.get('/specific/:uid',payModel.getSpecificPayment);
router.post('/',payModel.addPayment);
router.delete('/delete/:uid',payModel.deleteSpecificPayment);
router.put('/update/:uid',payModel.updateSpecificPayment);

module.exports=router;
