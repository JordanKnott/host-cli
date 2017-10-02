# Hosts CLI #

A simple python script that allows you to easily add, remove, or view rules
found in the Window's host file. 

Useful for developing sites locally that need an IP address. Just use the
```add``` command to map a local IP address to a domain.

![screenshot](https://github.com/jordanknott/host-cli/raw/master/www/screenshot.png "Screenshot")

# Installation & Requirements #

Requires Python 3.6+ (Untested on older versions)

Will only work if used from within an admin level command prompt.

An easy way to get one is to click on start -> type in "cmd" -> press
Control+Shift+Enter. Accept the UAC prompt if one appears. 

Once in a command prompt navigation, download the script. The preferred method
is through Git:

``` shell
git clone https://github.com/jordankott/host-cli
```

You can view a list of available commands through:

``` shell
python vhost.py --help
```

You also view help for individual commands my appending "--help" after any of
the commands. For example, to get help for the add command, type:

``` shell
python vhost.py add --help
```

# LICENSE #

MIT License. A copy can be found in the root directory of this repository.

