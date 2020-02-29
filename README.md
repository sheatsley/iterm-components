# iTerm Components

This repo contains python scripts that define [iTerm2](https://www.iterm2.com)
status bar components. Installation is straightforward: after cloning, copy (or
symlink) the desired component to:
`$Home/Library/ApplicationSupport/iTerm2/Scripts/AutoLaunch` Afterwards, the
status bar components will be available when iTerm2 starts.


## Components

### CPU Temperature

Displays CPU temperatures for macOS by calling `osx-cpu-temp` every couple
seconds. You can install `osx-cpu-temp` from
[here](https://github.com/lavoiesl/osx-cpu-temp) or through Homebrew.
