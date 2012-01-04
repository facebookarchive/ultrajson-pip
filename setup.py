
from distutils.core import setup, Extension
import distutils.sysconfig
import shutil
import os.path
import subprocess
import re

try:
	shutil.rmtree("./build")
except(OSError):
	pass

module1 = Extension('ujson',
                    sources = ['ultrajson/python/ujson.c', 'ultrajson/python/objToJSON.c', 'ultrajson/python/JSONtoObj.c', 'ultrajson/ultrajsonenc.c', 'ultrajson/ultrajsondec.c'],
                    headers = ['ultrajson/python/version.h'],
                    include_dirs = ['ultrajson/', 'ultrajson/python'])

def get_version():
	filename = os.path.join(os.path.dirname(__file__), 'ultrajson/python/version.h')
	file = None
	try:
		file = open(filename)
		header = file.read()
	finally:
		if file:
			file.close()
	m = re.search(r'#define\s+UJSON_VERSION\s+"(\d+\.\d+(?:\.\d+)?)"', header)
	assert m, "version.h must contain UJSON_VERSION macro"
	return m.group(1)


subprocess.call(["git", 'submodule', 'init'])
subprocess.call(["git", 'submodule', 'update'])

setup (name = 'ujson',
		version = get_version(),
		description = 'Ultra fast JSON encoder and decoder for Python',
		ext_modules = [module1],
		author = "Jonas Tarnstrom",
		author_email = "jonas.tarnstrom@esn.me",
		maintainer = "Jonas Tarnstrom",
		maintainer_email = "jonas.tarnstrom@esn.me",
		license = "BSD")
