# Ping Route

Small CLI to make test requests.

JSON input file template:

```json
[
  {
    "name": "Some service",
    "protocol": "http",
    "host": "localhost",
    "port": 8080,
    "path_list": [
      "/health/ping",
      "/health/status"
    ]
  }
]
```
