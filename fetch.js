var request = require("request")

url = "http://finance.google.com/finance/info?client=ig&q=" + process.argv[2]

request({
    url: url,
    json: true
}, function (error, response, body) {
    if (!error && response.statusCode === 200) {
    }
})

// res = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8').replace("//",""))
// print(datetime.date.today())
// print(datetime.datetime.utcnow())
// print(sys.argv[1])
// print(sys.argv[2])
// print(res[0]["l"])