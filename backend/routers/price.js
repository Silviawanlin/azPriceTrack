var express = require('express')
var Price = require('../models/price');
var router = express.Router()

// define the home page route
router.get('/get', async (req, res) => {
  
    let price = new Price();
    let priceInfo = await price.getPrice(req.query.url);    
    res.send(priceInfo);
})

module.exports = router


/*
// middleware that is specific to this router
router.use(function timeLog (req, res, next) {
  console.log('Time: ', Date.now())
  next()
})
*/