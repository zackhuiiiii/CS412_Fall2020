var express = require('express');
var router = express.Router();
const axios = require('axios').default;
require('dotenv').config()

/* GET form page. */
router.get('/', function (req, res, next) {
  res.render('form', { title: 'Weather' });
});

/* POST city weather condition. */
router.post('/weather', async function (req, res, next) {
  // res.send('respond with a resource');
  // GET
  // const city_name = req.params.city_name
  // POST
  const city_name = req.body.city_name
  try {
    const url = `${process.env.URL_ENDPOINT}?q=${city_name}&appid=${process.env.API_KEY}`
    const r = await axios.get(url);
    // console.log(r)
    // console.log(r.data)
    res.render('weather', { title: 'Weather', city_name, data: r.data });
  } catch (err) {
    // console.log(err)
    // console.log(err.response)
    // console.log(err.response.status)
    // console.log(err.response.data)
    if (err.response && err.response.data) {
      res.render('weather', { title: 'Express', city_name, data: err.response.data });
    } else {
      return next(err)
    }
  } finally {

  }
});

module.exports = router;