from multimethod import multimethod

class Lang:
	def __init__(self, language):
		self.language = language
		self.german = {
			'CompressingFile': 'Komprimiere {0} in {1}.zip',
			'ReadingFile': 'Einlesen der Datei {0}.zip',
			'UploadingFile': 'Hochladen der Datei {0}.zip auf den WebDav-Server.',
			'RemovingFile': 'Entferne Datei {0}.zip'
		}
		english = {
			'CompressingFile': 'Compressing {0} to {1}.zip',
			'ReadingFile': 'Reading in file {0}.zip',
			'UploadingFile': 'Uploading file {0}.zip to the web dav server.',
			'RemovingFile': 'Removing file {0}.zip'
		}

	def setLanguage(self, language: str):
		"Sets the language to the given value, currently valid: 'german' and 'english'"
		self.language = language

	@multimethod
	def getString(self, key: str):
		"Gets the text from the specified key in the specified language"
		if self.language == 'german':
			if key in self.german:
				return self.german.get(key)
			else:
				raise ValueError('Der Key wurde nicht gefunden: ' + key)
		elif self.language == 'english':
			if key in self.english:
				return self.english.get(key)
			else:
				raise ValueError('The key was not found: ' + key)
		else:
			raise ValueError('Wrong language specified.')

	@multimethod
	def getString(self, key: str, value: str):
		"Gets the text from the specified key in the specified language"
		if self.language == 'german':
			if key in self.german:
				return self.german.get(key).format(value)
			else:
				raise ValueError('Der Key wurde nicht gefunden: ' + key)
		elif self.language == 'english':
			if key in self.english:
				return self.english.get(key).format(value)
			else:
				raise ValueError('The key was not found: ' + key)
		else:
			raise ValueError('Wrong language specified.')

	@multimethod
	def getString(self, key: str, value: str, value2: str):
		"Gets the text from the specified key in the specified language"
		if self.language == 'german':
			if key in self.german:
				return self.german.get(key).format(value, value2)
			else:
				raise ValueError('Der Key wurde nicht gefunden: ' + key)
		elif self.language == 'english':
			if key in self.english:
				return self.english.get(key).format(value, value2)
			else:
				raise ValueError('The key was not found: ' + key)
		else:
			raise ValueError('Wrong language specified.')

	@multimethod
	def getString(self, key: str, value: str, value2: str, value3: str):
		"Gets the text from the specified key in the specified language"
		if self.language == 'german':
			if key in self.german:
				return self.german.get(key).format(value, value2, value3)
			else:
				raise ValueError('Der Key wurde nicht gefunden: ' + key)
		elif self.language == 'english':
			if key in self.english:
				return self.english.get(key).format(value, value2, value3)
			else:
				raise ValueError('The key was not found: ' + key)
		else:
			raise ValueError('Wrong language specified.')

	@multimethod
	def getString(self, key: str, value: str, value2: str, value3: str, value4: str):
		"Gets the text from the specified key in the specified language"
		if self.language == 'german':
			if key in self.german:
				return self.german.get(key).format(value, value2, value3, value4)
			else:
				raise ValueError('Der Key wurde nicht gefunden: ' + key)
		elif self.language == 'english':
			if key in self.english:
				return self.english.get(key).format(value, value2, value3, value4)
			else:
				raise ValueError('The key was not found: ' + key)
		else:
			raise ValueError('Wrong language specified.')

	@multimethod
	def getString(self, key: str, value: str, value2: str, value3: str, value4: str, value5: str):
		"Gets the text from the specified key in the specified language"
		if self.language == 'german':
			if key in self.german:
				return self.german.get(key).format(value, value2, value3, value4, value5)
			else:
				raise ValueError('Der Key wurde nicht gefunden: ' + key)
		elif self.language == 'english':
			if key in self.english:
				return self.english.get(key).format(value, value2, value3, value4, value5)
			else:
				raise ValueError('The key was not found: ' + key)
		else:
			raise ValueError('Wrong language specified.')

	@multimethod
	def getString(self, key: str, value: str, value2: str, value3: str, value4: str, value5: str, value6: str):
		"Gets the text from the specified key in the specified language"
		if self.language == 'german':
			if key in self.german:
				return self.german.get(key).format(value, value2, value3, value4, value5, value6)
			else:
				raise ValueError('Der Key wurde nicht gefunden: ' + key)
		elif self.language == 'english':
			if key in self.english:
				return self.english.get(key).format(value, value2, value3, value4, value5, value6)
			else:
				raise ValueError('The key was not found: ' + key)
		else:
			raise ValueError('Wrong language specified.')

	@multimethod
	def getString(self, key: str, value: str, value2: str, value3: str, value4: str, value5: str, value6: str, value7: str):
		"Gets the text from the specified key in the specified language"
		if self.language == 'german':
			if key in self.german:
				return self.german.get(key).format(value, value2, value3, value4, value5, value6, value7)
			else:
				raise ValueError('Der Key wurde nicht gefunden: ' + key)
		elif self.language == 'english':
			if key in self.english:
				return self.english.get(key).format(value, value2, value3, value4, value5, value6, value7)
			else:
				raise ValueError('The key was not found: ' + key)
		else:
			raise ValueError('Wrong language specified.')