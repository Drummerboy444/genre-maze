import os
import sys
import json
import random
import url_mp3play
import spotipy
import webbrowser
import genre_picker
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

when querying new endpoints use this print statement 
to display the json data in a format we humans can parse
print(json.dumps(VARIABLE, sort_keys=True, indent=4))

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
display_name = user["display_name"]
followers = user["followers"]["total"]

# initialise genre picker object
genre_object = genre_picker.GenrePicker()

print()
print("Welcome to Spotipy" + display_name + "!")
print()
print("0 - Search for a genre")
print("1 - random genre")
print("2 - exit")
print()

# MENU LOOP
while True:
    choice = input("Enter choice: 0 = choose, 1 = random, 2 = quit ")

    # End the program
    if choice == "2":
        print("Goodbye")
        break

    # get the genre from the user
    elif choice == "0":
        print()
        genre = input("Enter genre name:")
        print()
    elif choice == "1":
        genre = genre_object.random_genre()

    # Get search results. 'items' is a list of length limit.
    # This is where the requested content (track data) is stored
    num_of_tracks = 10
    search_results = spotify_object.search(
        f'* genre:"{genre}"', limit=num_of_tracks, offset=0, type="track"
    )
    search_results = search_results["tracks"]["items"]
    if len(search_results) == 0:
        print("Not a genre")
        continue

    # Some of the tracks don't have a preview and return null. This is the workaround:
    # Enumerate the items and make a list of only the items with a valid preview URL.
    # Store each URL as a tuple with its original positon in the items list so we can
    # retrieve the artist name and track title later from search results object.
    # This should be made simpler by appending the artist and track data
    # in the tuple at this point.
    track_urls = []
    for item in enumerate(search_results):
        if item[1]["preview_url"] != None:
            track_urls.append((search_results[item[0]]["preview_url"], item[0]))
    print("________________________________________________________")

    # pick a random track from the tracks which have previews
    picker = random.randint(0, len(track_urls) - 1)
    sample_url = track_urls[picker]

    # play the sample and display track info
    # webbrowser.open(sample_url[0])
    print(f"This is {genre}!")
    print()
    print(
        f"Artist: {json.dumps(search_results[sample_url[1]]['album']['artists'][0]['name'], indent=4)}"
    )
    print(
        f"Track: {json.dumps(search_results[sample_url[1]]['name'], sort_keys=True, indent=4)}"
    )

    # Play the mp3
    player = url_mp3play.Player(sample_url[0])
    player.play()
