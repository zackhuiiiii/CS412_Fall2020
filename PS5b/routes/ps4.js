var express = require('express');
var router = express.Router();
const axios = require('axios').default;
require('dotenv').config()
const redis = require("redis");

const client = redis.createClient({ port: 6379, host: '127.0.0.1' });
client.on("error", function (error) {
  console.error(error);
});

/* GET form page. */
router.get('/', function (req, res, next) {
  res.render('form', { title: 'Weather' });
});

/* POST city weather condition. */
router.post('/weather', async function (req, res, next) {
  const city_name = req.body.city_name.trim().toLowerCase()
  client.get(city_name, async function (err, reply) {
    // console.log(err)
    if (reply) {
      console.log(reply)
      res.json(Object.assign({}, JSON.parse(reply), { cache: true }))
    } else {

      try {
        const url = `${process.env.URL_ENDPOINT}?q=${city_name}&appid=${process.env.API_KEY}`
        const r = await axios.get(url);
        const data = r.data;
        // console.log(r)
        // console.log(r.data)
        // client.set(city_name, JSON.stringify(data), redis.print);
        client.setex(city_name, 15, JSON.stringify(data), redis.print);
        res.json(Object.assign({}, data, { cache: false }))
      } catch (err) {
        // console.log(err)
        // console.log(err.response)
        // console.log(err.response.status)
        // console.log(err.response.data)
        if (err.response && err.response.data) {
          res
            // .status(err.response.status)
            .json(Object.assign({}, err.response.data, { cache: false }))
        } else {
          // return next(err)
          const statusCode = err.status || 500
          res
            // .status(statusCode)
            // .send(err.message)
            .json({ cod: statusCode, message: err.message, cache: false })
        }
      } finally {

      }
    }
  });
});

module.exports = router;