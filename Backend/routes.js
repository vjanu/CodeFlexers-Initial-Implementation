const express = require('express');
const routes = express.Router();
const userroute = require('./controllers/user.controller');


routes.use('/users',userroute);


module.exports = routes;