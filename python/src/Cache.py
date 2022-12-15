import argparse
import os
import LinuxHelper as lh

def __init_argparse() -> argparse.ArgumentParser:

	parser = argparse.ArgumentParser(
		usage="%(prog)s [OPTION] [FILE]...",
		description="<program_description"
	)

	parser.add_argument(
		"-v", "--version", action="version",
		version = f"{parser.prog} version 0.01"
	)
	###
	#Add Custom arguments here with add_argument
	parser.add_argument('-u','--use-home',default=False,action='store_true',
                    help='Use Home directory')
	parser.add_argument('-c','--cache',nargs=1,default=False,
                    help='Cache directory, if not provided uses cwd')
	parser.add_argument('-f','--file',nargs=1,default=False,
                    help='File name including extension')
	parser.add_argument('-t','--time',nargs=1,type=int,default=5,
                    help='Age of cache file in mins')
	parser.add_argument('-d','--dump',default=False,action='store_true',
                    help='Dump file content')
	parser.add_argument('-w','--write',nargs=1,default=False,
					help='Content to write to file')

	###
	args = parser.parse_args()
	return args

def __validateConfig(config):
	if 'file' not in config:
		return False
	if not config['file']:
		return False
	return config

def __validateWriteConfig(config):
	if 'file' not in config:
		return False
	if not config['file']:
		return False
	if 'write' not in config:
		return False
	return config

def buildFile(config: dict) -> str:
	file = ''
	if config['home']:
		file = lh.getHomeDirectory()
	file = os.path.join(file, config['cache'], config['file'])
	return file

def writeCache(config: dict) -> dict:
	'''Using a config object writes content to a cache file
	home - boolean - use the current users home directory and combine with cache directory
	cache - string - path to find cache data
	fileName - string - name of the file to write to
	dump - boolean - return file contents if within age'''
	config = __validateWriteConfig(config)
	if not config:
		return False

	file = buildFile(config)
	
	lh.overwriteFile(file, config['write'])

	content = ''
	if config['dump']:
		content = config['write']
		
	returnJSON = {
		'valid': True,
		'content': content
	}
	return returnJSON

def fileAge(mtime: int) -> int:
	'''Uses int'''
	retVal = lh.getNow() - mtime
	return retVal

def readCache(config: dict) -> dict:
	''' Using a config object checks a cache file's existence and age and returns an object representing if the file exists and is older than the given time and the content of the file if requested. Returns either False or an object with valid:bool fileAge:int(mins) content:string|list
	home - boolean - use the current users home directory and combine with cache directory
	cache - string - path to find cache data
	fileName - string - name of the file to check
	time - int - minutes old the file should be checked against from modified time
	dump - boolean - return file contents if within age
	'''
	config = __validateConfig(config)
	if not config:
		return False

	file = buildFile(config)
	exists = lh.fileExists(file)

	age = False
	mtimeAge = 0
	# File Age
	if exists:
		mtimeAge = fileAge(lh.fileAge(file)) / 60
		age = mtimeAge < config['time']

	content = ''
	if exists and config['dump']:
		content = lh.readFile(file)

	returnJSON = {
		'valid': age,
		'fileAge': mtimeAge,
		'content': content
	}
	return returnJSON

def main() -> dict:
	args = __init_argparse()
	config = {
		'home':args.use_home,
		'cache':args.cache,
		'file':args.file,
		'time':args.time,
		'dump':args.dump,
		'write':args.write
	}

	if args.write:
		returnJSON = writeCache(config)
	else:
		returnJSON = readCache(config)
	print(returnJSON)
	return returnJSON

if __name__ == '__main__':
	main()