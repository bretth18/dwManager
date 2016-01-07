##script.py
##2016 bretth18
from __future__ import unicode_literals
from sys import platform as _platform

import sys
import logging
import spotify
import threading

#setup logging
logging.basicConfig(level = logging.DEBUG)


#call that session


#config = spotify.Config()
#config.user_agent =
#config.tracefile =

session = spotify.Session()

loop = spotify.EventLoop(session)
loop.start()

#events for coordination
logged_in = threading.Event()


#update connection state to logged in
def on_connection_state_updated(session):
    if session.connection.state is spotify.ConnectionState.LOGGED_IN:
        logged_in.set()

#register event listeners
session.on(
    spotify.SessionEvent.CONNECTION_STATE_UPDATED,
    connection_state_listener)
session.connection.state

while not logged_in_event.wait(0.1):
    session.process_events()

#login to session

userName = raw_input("Gimme dat username")
passName = raw_input("Gimme dat password")

session.login(userName, passName)


#call input for dwPlaylist
dwPlaylist = raw_input("input discover weekly playlist URI")

#load DW playlist
len(session.playlist_container)
playlist = session.playlist_container[0]
playlist.load('dwPlaylist')


def container_loaded(playlist_container):
    print('Playlist container loaded...')


#show subs option
subView = raw_input("Show Playlist Subscribers? Y/N")
if (subView == 'Y'):
    playlist.load().update_subscribers()
    playlist.load().subscribers
else :
    return
