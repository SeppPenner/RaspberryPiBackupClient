import traceback
import shutil
import requests
import urllib3
import datetime
import os
from bin import lang

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

language = lang.Lang('english') # Valid ones are currently 'german' and 'english'
folders = {'examplefolder': '/var/lib/example', 'examplefolder2':'/etc/example/'}
webdavroot = 'https://someurl.com/backup/'
webdavuser = "user"
webdavpassword = "password"

def iterateFolders():
	"Iterates over the given folders, zips them and backups the zip files to a webdav server"
	try:
		for fileName, folder in folders.items():
			print(language.getString('CompressingFile', folder, fileName))
			shutil.make_archive(fileName, 'zip', folder)
			with open('./' + fileName + '.zip', 'rb') as file:
				print(language.getString('ReadingFile', fileName))
				fileContent = file.read()
				print(language.getString('UploadingFile', fileName))
				dateTime = getCurrentDateTimeFormatted()
				response = requests.put(webdavroot + fileName + '_' + dateTime + '.zip', auth=(webdavuser, webdavpassword), data=fileContent, verify=False)
				print(response)
				#print(response.content)
			print(language.getString('RemovingFile', fileName))
			os.remove('./' + fileName + '.zip')
	except Exception as e:
		traceback.print_exc()

def getCurrentDateTimeFormatted():
	"Returns a string for the output file with the current date"
	return datetime.datetime.now().strftime('%Y_%m_%d')

iterateFolders()