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

### Get information about userid and packageid 

`/resolver/resolve`

**Method:** `GET`

**Query Parameters:**

 - `path` - takes {username/pkgname}

**Returns:**
If exists username and pkgname:
```json
{
    "packageid": "<packageid>",
    "userid": "<userid>"
}
```
if there is no user, it return null:
```json
{
    "packageid": "<packageid>",
    "userid": null
}
```

