#Better PEP8

Better PEP8 is a Sublime plugin which uses the `pep8` or `flake8` command line tool and displays the results. It can be configured to use any other external tool.

![Screenshot](https://raw.github.com/jeremija/BetterPEP8/screenshots/screenshot.png)

**Prerequisites:** [pep8](https://pypi.python.org/pypi/pep8) or [flake8](https://pypi.python.org/pypi/flake8)

##Installation of prerequisites (ubuntu):

    $ apt-get install pep8 python-flake8

or via PIP:

    $ pip install pep8 flake8

##Installation of the plugin itself (linux):

Clone the this repository to the `$SUBLIME_SETTINGS/Packages` folder, where `$SUBLIME_SETTINGS` is the sublime settings path. So on a linux machine this would be:

    $ cd ~/.config/sublime-text-2/Packages/
    $ git clone https://github.com/jeremija/BetterPEP8.git

##Usage

- `Control`-`7` runs the defined command line tool on the current active file
- `F4` jumps to next error
- `Shift`-`F4` jumps to previous error

Multiple directories/files are supported via the Side Bar's Context Menu.

##Default configuration file

	{
		"binary" : "pep8",
		"flags" : {
			"--max-line-length" : "99",
			"--ignore" : "E126,E127,E128"
		},
		"file-regex" : "(.*):([0-9]*):([0-9]*):[ ](.*)"
	}

 - `binary` the command line tool to launch
 - `flags` add your options for the command line tool here

Optional property is `line-regex`. The `file-regex` or `line-regex` properties should not be modified if you plan to use pep8 or flake8. Changeg the `binary` property to `flake8` if you wish to use flake8 instead of `pep8`.

##Note

This has been tested to work on
* Sublime Text build 2221
* Sublime Text build 3059
