from mojang import MojangAPI

def uuid(username):
        return(MojangAPI.get_uuid(username))