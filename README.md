RaspberryPiBackupClient
====================================

RaspberryPiBackupClient is a project to backup certain directories from your Raspberry Pi to a WebDav server. The script was written and tested in Python 3.7.4.

[![Build status](https://ci.appveyor.com/api/projects/status/giyrqr15h5caueoo?svg=true)](https://ci.appveyor.com/project/SeppPenner/raspberrypibackupclient)
[![GitHub issues](https://img.shields.io/github/issues/SeppPenner/RaspberryPiBackupClient.svg)](https://github.com/SeppPenner/RaspberryPiBackupClient/issues)
[![GitHub forks](https://img.shields.io/github/forks/SeppPenner/RaspberryPiBackupClient.svg)](https://github.com/SeppPenner/RaspberryPiBackupClient/network)
[![GitHub stars](https://img.shields.io/github/stars/SeppPenner/RaspberryPiBackupClient.svg)](https://github.com/SeppPenner/RaspberryPiBackupClient/stargazers)
[![GitHub license](https://img.shields.io/badge/license-AGPL-blue.svg)](https://raw.githubusercontent.com/SeppPenner/RaspberryPiBackupClient/master/License.txt)
[![Known Vulnerabilities](https://snyk.io/test/github/SeppPenner/RaspberryPiBackupClient/badge.svg)](https://snyk.io/test/github/SeppPenner/RaspberryPiBackupClient) 

# Steps to use this project:
1. Make sure to install Python and Pip correctly
2. Set the execute flags:

```bash
chmod +x install.sh
chmod +x run.sh
chmod +x backup.py
```

3. Install all required pip package dependencies with:

```bash
pip install -r requirements.txt
```

4. Setup a WebDav server and create a folder to be accessible from the script.

5. Adjust your settings in the [backup.py](https://github.com/SeppPenner/RaspberryPiBackupClient/blob/master/backup.py) file:

```python
language = lang.Lang('english') # Valid ones are currently 'german' and 'english'
folders = {'examplefolder': '/var/lib/example', 'examplefolder2':'/etc/example/'}
webdavroot = 'https://someurl.com/backup/'
webdavuser = "user"
webdavpassword = "password"
```

6. Run the backup client in a cronjob, e.g.
```bash
0 6 1 * * /usr/bin/python3 /home/something/backup.py
```

to run it on each first day of the month at 6 o'clock in the morning.

7. If you do not use a self signed certificate, disable the following line

```python
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
```

# For more information see:
* https://www.quora.com/How-do-I-zip-directories-in-Python
* https://stackoverflow.com/questions/36216274/uploading-a-0-bytes-file-to-owncloud-with-python-requests-hangs
* https://crontab.guru/#0_6_1_*_*

Change history
--------------

* **Version 1.0.0.1 (2019-09-29)** : Updated python version, updated requirements.
* **Version 1.0.0.0 (2018-10-12)** : 1.0 release.