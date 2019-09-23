# Print HTTP Request

This is a small python server that will print the headers sent with each request.
This can be useful to inspect the requests made by your applications, browser, scraper, etc.

Setup your environment:
```
conda create --name print-http-request --yes python=3.6
conda activate print-http-request
pip install -r requirements.txt
```

Run the server:
```
FLASK_APP=server.py flask run
```

Send a request:
```
curl --header "Foo: bar" http://127.0.0.1:5000/
```

The server should print something like
```
Headers
=======
Host: 127.0.0.1:5000
User-Agent: curl/7.64.0
Accept: */*
Foo: bar
```
