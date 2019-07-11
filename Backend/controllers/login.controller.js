const express = require('express');
const router = express.Router();
const loginModel=require('../models/login.model');

//controller to get all users
router.get('/',loginModel.getUsers);
//controller to validate users
router.get('/validate/:uname',loginModel.getSpecificUserName);
//controller to add users
router.post('/',loginModel.addUser);
//controller to add spouse
router.post('/spouse',loginModel.addSpouse);
//controller to get user's username and passwords
router.get('/specific/:username/:password',loginModel.getSpecificUser);
//delete users
router.delete('/delete/:id',loginModel.deleteSpecificUser);

module.exports=router;
