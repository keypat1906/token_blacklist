
# Class to blacklist the tokens
# User set data structure to store and remove token


class BlacklistToken():

    def __init__(self):
        self.jwt_set = set()

    def is_blacklisted(self, jwt):
        return jwt in self.jwt_set

    def add_jwt(self, jwt):
        self.jwt_set.add(jwt)

    def remove_jwt(self, jwt):
        if jwt in self.jwt_set:
            self.jwt_set.remove(jwt)
        
