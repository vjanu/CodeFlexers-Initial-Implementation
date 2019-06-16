const express = require('express');
const routes = express.Router();
const loginroute = require('./controllers/login.controller');
const userroute = require('./controllers/users.controller');
const payroute = require('./controllers/payment.controller');
const preferenceroute = require('./controllers/preference.controller');
const vehicleroute = require('./controllers/vehicle.controller');
const telephoneroute = require('./controllers/telephone.controller');
const roadcauseroute = require('./controllers/roadcause.controller');


routes.use('/login',loginroute);
routes.use('/users',userroute);
routes.use('/pay',payroute);
routes.use('/preference',preferenceroute);
routes.use('/vehicle',vehicleroute);
routes.use('/telephone',telephoneroute);
routes.use('/roadcause',roadcauseroute);


module.exports = routes;