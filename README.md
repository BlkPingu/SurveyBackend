# Backend

- [How to build a RESTful API in Python](https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way)
- [JWT as pyjwt](https://realpython.com/token-based-authentication-with-flask/)
- [https](https://stackoverflow.com/questions/29458548/can-you-add-https-functionality-to-a-python-flask-web-server)
- [logging](https://code-maven.com/python-flask-logging)





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