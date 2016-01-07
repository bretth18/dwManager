import spotify
import sys
import threading

#handle login params
userName = raw_input('enter username: ')
passName = raw_input('enter password: ')
playList = raw_input('enter playlist URI: ')

#start session
session = spotify.Session()
session.login(userName, passName)
loop = spotify.EventLoop(session)
loop.start()

#load playlist, display subs
playlist = session.get_playlist(playList)
playlist.load().update_subscribers()
print(playlist.load().subscribers)
