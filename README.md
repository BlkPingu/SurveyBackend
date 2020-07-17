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