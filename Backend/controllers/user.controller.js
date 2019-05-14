const express = require('express');
const router = express.Router();
const userModel=require('../models/user.model');

//controller to get all users
router.get('/',userModel.getUsers);
//controller to validate users
router.get('/validate/:uname',userModel.getSpecificUserName);
//controller to add users
router.post('/',userModel.addUser);
//controller to get user's username and passwords
router.get('/specific/:username/:password',userModel.getSpecificUser);
//delete users
router.delete('/delete/:id',userModel.deleteSpecificUser);

module.exports=router;
