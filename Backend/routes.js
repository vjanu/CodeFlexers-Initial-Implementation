const express = require('express');
const routes = express.Router();
const loginroute = require('./controllers/login.controller');
const userroute = require('./controllers/users.controller');
const payroute = require('./controllers/payment.controller');
const preferenceroute = require('./controllers/preference.controller');
const vehicleroute = require('./controllers/vehicle.controller');
const telephoneroute = require('./controllers/telephone.controller');
const ratingroute = require('./controllers/rating.controller');
const roadcauseroute = require('./controllers/roadcause.controller');
const tripsummaryroute = require('./controllers/trip_summary.controller');
const offerrideroute = require('./controllers/offerride.controller');
const availableDriversroute = require('./controllers/availableDriverList.controller');
const triproute = require('./controllers/trip.controller');
const maproute=require('./controllers/map.controller')



routes.use('/login',loginroute);
routes.use('/users',userroute);
routes.use('/pay',payroute);
routes.use('/preference',preferenceroute);
routes.use('/vehicle',vehicleroute);
routes.use('/telephone',telephoneroute);
routes.use('/ratings',ratingroute);
routes.use('/roadcause',roadcauseroute);
routes.use('/tripsummary',tripsummaryroute);
routes.use('/addofferride',offerrideroute);
routes.use('/available',availableDriversroute);
routes.use('/trip',triproute);
routes.use('/map',maproute);

module.exports = routes;