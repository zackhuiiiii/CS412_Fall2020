var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
  // Return our render pug template
  res.render('ps3', { stringToDisplay: 'Hello' });
});
router.post('/', function(req, res, next) {
  // Grab our string from the requests and calculate its length
  let newString = req.body.stringParam
  if (newString == undefined) {
    res.render('ps3Error')
    return
  }
  let lengthOfNewString = newString.length
  res.render('ps3Post', { stringToDisplay: newString, lengthOfNewString: lengthOfNewString });
});

module.exports = router;
