import re


def get_username_from_profile_path(path_profile:str):
    """
    Transform "/p/bmazariegos/" to "bmazariegos"
    """
    return path_profile[3:-1]

def get_username_from_avatar(avatar_url:str):
    """
    Transform "https://static.platzi.com/media/avatars/alan-isaac_vazquez_807714c1-eccc-4a11-8fd2-780569392832" to "alan-isaac_vazquez"
              "https://static.platzi.com/media/avatars/avatars/OscarAn-ca26ab2b-2e05-4d57-acc9-88182cb85dc7.png" to "OscarAn"
    """
    for pattenr in [r'.*\/(.*)_.*', r'.*\/(.*)-.*-.*-.*-.*-.*']:
        match = re.match(pattenr, avatar_url)
        if match:
            return match.group(1)

    raise ValueError(f"Cant get username from avatar url: {avatar_url}")