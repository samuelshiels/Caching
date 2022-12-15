# Caching
Caching processes

![Process Flow](https://github.com/samuelshiels/Caching/blob/Caching.png "Process Flow")

# Usage 

```python
import Cache
config = {
		'home': True,
		'cache': appCacheDirectory,
		'file': 'testfile.cache',
		'time': 5,
		'dump': True
	}
output = Cache.readCache(config)
if not output['valid']:
	config['write'] = 'test_cache_content'
	output = Cache.writeCache(config)
```

Output is a dict with properties 'valid' and 'content'. Valid represents if the file's age is within the minutes specified in the config input and the content is provided if the 'dump' property is set to true
```json
{
	"valid":true,
	"content":"123 Test"
}
```