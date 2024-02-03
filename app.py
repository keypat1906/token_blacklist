from flask import Flask, jsonify, Response, request
from .blacklist import BlacklistToken
from .utils import validate_token

black = BlacklistToken()

app = Flask(__name__) 


@app.route("/info")
def info() -> Response:
    '''
    Function return the status of the token
    Success - True if token is not blacklisted
    Sucesss - False if token is blacklisted
    '''    
    header = request.headers.get("Authorization")
    token = header.split()[1]
     
    if black.is_blacklisted(token):
        return jsonify({"success": False, "token": token, \
                        "info":"Token is blacklisted" })
    
    decoded, msg = validate_token(token)
    if not decoded:
        return msg
    
    return jsonify({"success": True, "token": token, "decoded_token": decoded})



@app.route("/blacklist",methods=['DELETE', 'POST'])
def blacklist() -> Response:
    '''
    POST - blacklist the token. 
    DELETE - remove the token from blacklist
    '''
    if request.method == 'POST':
        header = request.headers.get("Authorization")
        token = header.split()[1]

        # validate token
        decoded, msg = validate_token(token)
        if not decoded:
            return msg
    
        black.add_jwt(token)
        return jsonify({"success": True, "token": token, \
                         "info":"Token is blacklisted"})
    
    if request.method == 'DELETE':
        header = request.headers.get("Authorization")
        token = header.split()[1]
        
        # validate token
        decoded, msg = validate_token(token)
        if not decoded:
            return msg
    
        black.remove_jwt(token)
        return jsonify({"success": True, "token": token, \
                        "info":"Token is removed from blacklist"})








