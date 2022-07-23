# AWS url shortener API 

## Usage
Client sends a `POST` request to the `link` API endpoint containing the long url. The function response contains a short url. 

The `long_url` is stored together with the `url_id` in the DynamoDB table. 

GET request to the `link/{url_id}` API endpoint invokes the function that finds the matching `long_url` in the DynamoDB table and redirects the user to his `long_url`. 

## Deployment

```
$ sls deploy
```

### Example POST Request
```
curl -X POST https://xxxxxxxxxxx.amazonaws.com/dev/link -d '{"long_url": "example.com"}'
```
### Example GET Request
```
curl -X GET https://xxxxxxxxxxx.amazonaws.com/dev/link/{url_id}
```
