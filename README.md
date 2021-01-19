# Single-Sign-on
Single Sign-On ( SSO ) with Django

# Setup

1) Installing Required Files

#### `For Windows:`

```javascript
pip install -r requirements.txt
```
#### `For Linux/Mac:`

```javascript
pip3 install -r requirements.txt
```

3) Run the devlopment server:
   (Use python instead of python3 if you are on windows)

#### `For User Server:`

```javascript
cd UserServer/
python3 manage.py runserver
```

#### `For User Client:`

```javascript
cd UserClient/
python3 manage.py runserver 9000
```

4) Go to the url shown in terminal for UserServer say, 127.0.0.1:8000/admin and use following username and password:

```javascript
username: gituser
password: gituser
```

5) Then go to UserClient Server, 127.0.0.1:9000/

hey you got it! HAPPY SURFING :)

## License
MIT - [See LICENSE](./LICENSE)

###### This repository is just a small subset of work put together by a much larger pool of voluntary efforts contributed by generous people all around the world. Reach out to us through itechindrustries@gmail.com