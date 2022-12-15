import LinuxHelper as lh
import Cache

appCacheDirectory = lh.getCacheDirectory() + 'appCacheTest2'

def test1():
	"""Tests reading the cache with a minimal config object"""
	cacheData = ''
	appCacheDirectory = lh.getCacheDirectory() + 'appCacheTest2'
	config = {
		'home': True,
		'cache': appCacheDirectory,
		'file': 'test1-testfile.cache',
		'time': 5,
		'dump': True
	}
	return

def test2():
	"""Tests writing a cache with a minimal config object"""
	cacheData = ''
	appCacheDirectory = lh.getCacheDirectory() + 'appCacheTest'
	config = {
		'home': True,
		'cache': appCacheDirectory,
		'file': 'test2-testfile.cache',
		'time': 5,
		'dump': True
	}
	output = Cache.readCache(config)
	return

def test3():
	"""Tests writing to the cache and reading the cache back"""
	cacheData = ''
	appCacheDirectory = lh.getCacheDirectory() + 'appCacheTest'
	config = {
		'home': True,
		'cache': appCacheDirectory,
		'file': 'test3-testfile.cache',
		'time': 5,
		'dump': True
	}
	return

def test4():
	"""Tests the age of the file check"""
	cacheData = ''
	appCacheDirectory = lh.getCacheDirectory() + 'appCacheTest'
	config = {
		'home': True,
		'cache': appCacheDirectory,
		'file': 'test4-testfile.cache',
		'time': 2,
		'dump': True
	}
	return