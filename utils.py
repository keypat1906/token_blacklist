
from flask import jsonify 
import jwt


def validate_token(token):
    '''
    function validate the token signature, iss and expiration
    '''
    try:
        decoded = jwt.decode(token, "admin", algorithms="HS256")
    
    except jwt.ExpiredSignatureError as e :
        return (None, jsonify({"success": False,"info":f"Invlid Signature - {e}"}))
    
    except jwt.DecodeError as e: 
        return (None, jsonify({"success": False,"info":f"Decode Error - {e}"}))
    
    except jwt.InvalidTokenError as e :
        return (None, jsonify({"success": False,"info":f"Invlid Token - {e}"}))
    
    if decoded["iss"] != "https://www.arc.com/":
        return (None, jsonify({"success": False, "info":"Invlid Issuer"}))
   
    return decoded, ""
