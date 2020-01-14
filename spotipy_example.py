import os
import sys
import json
import webbrowser
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

"""
Spotipy script. 
First run the $ lines in terminal:

$ export SPOTIPY_CLIENT_ID='a43cad70e5c94addbc2e8fa4a9940325'
$ export SPOTIPY_CLIENT_SECRET='026fdfee51714c37a6c2b51242bc7e26'
$ export SPOTIPY_REDIRECT_URI='http://google.com'

The username gets passed in 
with the python file at execution
$ python3 spotify.py mgallimore10872

Browser will prompt for authentication. 
Copy and paste the redirect URL string 
from the browser into terminal when prompted.

To search and retrieve information from spotify:
-use the spotipy docs to see possible functions and method formats.
-Call one of the methods on the spotify_object
-assign the output of the method to a variable name
-print the json data of the variable using the print line below
print(json.dumps(VARIABLE, sort_keys=True, indent=4))
-look at the format of the json data and index down as many levels as required

Example 1:
# create our spotify object:
spotify_object = spotipy.Spotify(auth=token)

# get user data
user = spotify_object.current_user()
print(json.dumps(user, sort_keys=True, indent=4))

# index into the data having looked at its structure in terminal
display_name = user['display_name']
followers = user['followers']['total']
"""

# get the username from terminal
username = sys.argv[1]

# erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# create our spotify object:
spotify_object = spotipy.Spotify(auth=token)

# initialise user data
user = spotify_object.current_user()
print(json.dumps(user, sort_keys=True, indent=4))
display_name = user["display_name"]
followers = user["followers"]["total"]

# menu loop
while True:
    print()
    print(">>> Welcome to Spotipy" + display_name + "!")
    print(">>> You have " + str(followers) + "followers.")
    print()
    print("0 - Search for an artist")
    print("1 - exit")
    print()
    choice = input("Enter choice: ")

    # Search for the artist
    if choice == "0":
        print()
        search_query = input("Enter artist name:")
        print()

        # Get search results
        search_results = spotify_object.search(search_query, 1, 0, "artist")
        print(json.dumps(search_results, sort_keys=True, indent=4))

        artist = search_results["artists"]["items"][0]
        print(artist["name"])
        print(f"{artist['followers']['total']} followers")
        print(f"Genre: {artist['genres'][0]}")
        print()
        webbrowser.open(artist["images"][0]["url"])
        artist_ID = artist["id"]
        # Artist id is usually
        # the first argument for the API modules

        # Album and track details
        track_URIs = []
        track_art = []
        z = 0

        # Extract Album data
        album_results = spotify_object.artist_albums(artist_ID)
        # go down one level because everything useful is in 'items'
        album_results = album_results["items"]

        for item in album_results:
            print("Album " + item["name"])
            album_ID = item["id"]
            album_art = item["images"][0]["url"]

            # Extract track data
            track_results = spotify_object.album_tracks(album_ID)
            track_results = track_results["items"]

            for item in track_results:
                print(str(z) + ": " + item["name"])
                track_URIs.append(item["uri"])
                track_art.append(album_art)
                z += 1
            print()

        # See album art
        while True:
            song_selection = input("Enter a song number to see associated artwork: ")
            if song_selection == "":
                break
            webbrowser.open(track_art[int(song_selection)])

    # End the program
    if choice == "1":
        print("Goodbye")
        break
