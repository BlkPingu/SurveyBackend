# Backend

- [How to build a RESTful API in Python](https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way)
- [JWT as pyjwt](https://realpython.com/token-based-authentication-with-flask/)
- [https](https://stackoverflow.com/questions/29458548/can-you-add-https-functionality-to-a-python-flask-web-server)
- [logging](https://code-maven.com/python-flask-logging)


### Get Started

```bash
python3 -m venv /foo/bar/
```
```bash
cd /foo/bar/
```
```bash
git clone git@github.com:BlkPingu/SurveyBackend.git
```
```bash
source bin/activate
```
```bash
pip3 install -r requirements.txt
```
```bash
python3 SurveyBackend/app.py
```


### API setup

**routes**

`BASE_URL/api/meta: http put`

- meta.json
  - string: sessionid
  - list: metadata
    - int: alter
    - string: geschlecht
    - string: native language
    - boolean: dsgvo accept



`BASE_URL/api/soundfile: http put`

- soundfile name: `<sessionid>_<questionid>.wav`





**metadaten**

- geschlecht
- muttersprache
- alter




INFO SERVER:



[Server setup, nginx and flask](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04):

- `sudo systemctl restart nginx`: Start Nginx Server
- `sudo systemctl start SurveyBackend`: Start uWSGI Server (Flask)
- `sudo systemctl status myproject`: Status von uWSGI
- `sudo less /var/log/nginx/error.log`: checks the Nginx error logs.
- `sudo less /var/log/nginx/access.log`: checks the Nginx access logs.
- `sudo journalctl -u nginx`: checks the Nginx process logs.
- `sudo journalctl -u myproject`: checks your Flask app’s uWSGI logs.


