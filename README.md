# Ping Route

Small CLI to make test requests.

## Commands:

**help**: get help for available commands.

**check**: ping all services listed in JSON input file.

```shell
pingr check file.json
```

JSON input file template:

```json
[
  {
    "name": "Some service",
    "protocol": "http",
    "host": "localhost",
    "port": 8080,
    "routes": [
      "/health/ping",
      "/health/status"
    ]
  }
]
```
