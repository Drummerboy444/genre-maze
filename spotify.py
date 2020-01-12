import os
import sys
import json
import webbrowser
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

# get the username from terminal
username = sys.argv[1]

# User ID: mgallimore10872
# The username gets passed in with the python file at terminal
# To run this script type
# python3 spotify.py mgallimore10872 
# into terminal

# spotify:user:mgallimore10872
# https://open.spotify.com/user/mgallimore10872?si=hMoXpjtyQJWcBJ_4VgBOlw


# erase cache and prompt for user permission

try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# create our spotify object:

spotify_object = spotipy.Spotify(auth=token)


# in terminal type:

# export SPOTIPY_CLIENT_ID='a43cad70e5c94addbc2e8fa4a9940325'
# export SPOTIPY_CLIENT_SECRET='026fdfee51714c37a6c2b51242bc7e26'
# export SPOTIPY_REDIRECT_URI='http://google.com'

user = spotify_object.current_user()
print(json.dumps(user, sort_keys=True, indent=4))

#print(json.dumps(VARIABLE, sort_keys=True, indent=4))