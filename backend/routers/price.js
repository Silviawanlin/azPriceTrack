var express = require('express')
var router = express.Router()

// define the home page route
router.get('/get', function (req, res) {
 
    res.send("asdfsdf");
})

module.exports = router


/*
// middleware that is specific to this router
router.use(function timeLog (req, res, next) {
  console.log('Time: ', Date.now())
  next()
})
*/