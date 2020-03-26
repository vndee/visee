var unirest = require('unirest');
var req = unirest('POST', 'http://127.0.0.1:8001/api/rest/search/')
  .headers({
    'api_key': 'h$+wt&%3BtH*6rA^KfPzMKDm**GdH_wQaQebd&X9!h=nNVjrt+pn8GNB5%-_ug-U',
    'Content-Type': ['application/json', 'text/plain']
  })
  .send("{\"engine\": \"text\",\"query\": \"thuốc\"}")
  .end(function (res) {
    if (res.error) throw new Error(res.error);
    console.log(res.raw_body);
  });
