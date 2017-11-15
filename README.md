# Kodi Linux Remote

Born out of my personal need to have a simple remote for controlling Kodi server, KodiLinuxRemote attempts to have a simple GUI carrying basic controls for operating Kodi.

## Supported Controls

In its current iteration, it supports following controls. All these can be controlled using keyboard as well.

- Increase (Minus) and Decrease (Plus) volume
- Navigation (Up, Down, Left, and Right) (Arrow up, down, left, right respectively)
- Media selection (Enter)
- Play/Pause (Spacebar)

## Screenshots

![Remote Screen](https://github.com/ParitoshBh/KodiLinuxRemote/raw/master/screenshots/remote-screen.png)

![Setup Screen](https://github.com/ParitoshBh/KodiLinuxRemote/raw/master/screenshots/setup-screen.png)

## Using KodiLinuxRemote

Since I am just starting with its development, there aren't any builds available to install. However, getting it up and running is quite easy provided following requirements are met,

- Python 3
- Fedora 25/26 (Untested on other linux distributions)
- `requests` package (Python)

Getting the code and running is the easiest part,

1. Clone the repository
2. Change directory to cloned respository
3. Install dependencies by executing `pip3 install -r requirements.txt`
4. Execute `python3 main.py`
5. That's it! You should see the setup screen.

## Feature Requests

As of now, the app is bare bones at best and now where near what the web interface does or its android counterpart. The aim is to have a solid base going and then build on it based on feature requests from community.

This desktop app is being developed in the free time I have from the day job and thus there's less time for testing, enhancement, and feature implementation. And thus if you have some time to spare and are interested in seeing it grow, I encourage you to take it up for spin and file issues, feature requests [here]((https://github.com/ParitoshBh/KodiLinuxRemote/issues/new)) !

## API Reference

`http://192.xxx.xxx.xxx:xxxx/jsonrpc`