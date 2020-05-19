# api docs

### models 
 - can be found in models.

### api urls
 - can be found in urls.py

### api controllers
 - see views/ folder

### codes:
 * 1 success
 * -1 bad request method
 * -2 login required

## api methods:

* ### /api/login/ 
#### POST data: 
##### username: String 
##### password: String
#### Returns json response with result "code", "msg" and "sessionid".
#### Also setups cookie "sessionid"

* ### /api/logout/ 
#### Returns json response with result "code" and "msg".
#### Removes cookie "sessionid" so user is logged out

* ### /api/check/
#### Returns json response with result "code" and "msg".
#### Msg contains current user type(manager|courier|client)