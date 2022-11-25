import LinuxHelper as lh
import Cache

appCacheDirectory = lh.getCacheDirectory() + 'appCacheTest2'

config = {
		'home': True,
		'cache': appCacheDirectory,
		'file': 'testfile.cache',
		'time': 5,
		'dump': True
	}

output = Cache.readCache(config)
print(output)
if not output['valid']:
	config['write'] = 'Test12'

	output = Cache.writeCache(config)
	print(output)