const express = require('express');
const router = express.Router();
const offer_ride=require('../models/offerride.model');

router.get('/',offer_ride.getAllDriverOffers);
router.post('/',offer_ride.addOfferRide);

module.exports=router;