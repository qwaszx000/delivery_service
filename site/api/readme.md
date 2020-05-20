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
 * -3 permission denied
 * -4 bad params
 * -5 user not found

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

* ### /api/type/check/
#### Returns json response with result "code" and "msg".
#### Msg contains current user type(manager|courier|client)

* ### /api/type/set/
#### POST data: 
##### username: String
##### type: String
#### Changes user type
#### Returns json response with result "code", "msg" and "type".
