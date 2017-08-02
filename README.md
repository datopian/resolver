Resolver is a DataHub microservice for resolving datapackage URLs into more human readable ones

[![Build Status](https://travis-ci.org/datahq/resolver.svg?branch=master)](https://travis-ci.org/datahq/resolver)

## Quick Start

# Clone the repo and install

`make install`

# Run tests

`make test`

# Run server

`python server.py`


## API

### Resolves username to userid 

`/resolver/resolve`

**Method:** `GET`

**Query Parameters:**

 - `path` - takes {username/pkgname}

**Returns:**
if user found in the system::
```json
{
    "packageid": "<packageid>",
    "userid": "<userid>"
}
```
If user not found:
```json
{
    "packageid": "<packageid>",
    "userid": null
}
```

