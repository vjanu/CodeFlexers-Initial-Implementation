const express = require('express');
const router = express.Router();
const userModel=require('../models/users.model');

router.get('/',userModel.getAllUsers);
router.get('/specific/:uid',userModel.getSpecificUser);
router.post('/',userModel.addUser);
router.delete('/delete/:uid',userModel.deleteSpecificUser);
router.put('/update/:uid',userModel.updateSpecificUser);

module.exports=router;
