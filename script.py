##script.py
##2016 bretth18
from __future__ import unicode_literals
from sys import platform as _platform

import sys
import logging
import spotify
import threading
import getpass

#setup logging
logging.basicConfig(level = logging.DEBUG)


#begin session with appkey in root dir
session = spotify.Session()

#process events
loop = spotify.EventLoop(session)
loop.start()

#add threading events
logged_in = threading.Event()

def on_connection_state_updated(session):
    if session.connection.state is spotify.ConnectionState.LOGGED_IN:
        logged_in.set()
        load_dw_playlist()

#register event listeners
session.on(
        spotify.SessionEvent.CONNECTION_STATE_UPDATED, on_connection_state_updated)


#login to session

userName = raw_input("Gimme dat username: ")
passName = getpass.getpass("Gimme dat password: ")

session.login(userName, passName)
session.connection.state
logged_in.wait()

#call to process
#while not logged_in.wait(0.1):
#    session.process_events()

#define sessionUser
session.user

def load_dw_playlist(dwPlaylist):
    #call input for dwPlaylist
    dwPlaylist = raw_input("input discover weekly playlist URI: ")

    #load DW playlist
    len(session.playlist_container)
    #playlist = session.playlist_container[0]
    #playlist.load(dwPlaylist)
    playlist = session.get_playlist(dwPlaylist)
    container.insert(1, playlist)


#store playlist.tracks in an array to copy to new playlist

    if playlist.is_loaded = True:
        playlist.tracks[0]

def tracks_added(playlist, tracks, index):
    print('dw tracks added to archive')

def container_loaded(playlist_container):
    print('Playlist container loaded...')


#show subs option
#subView = raw_input("Show Playlist Subscribers? Y/N")
#if (subView == 'Y'):
#    playlist.load().update_subscribers()
#    playlist.load().subscribers
#else :
#    return
