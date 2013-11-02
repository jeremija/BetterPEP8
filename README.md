#Better PEP8

Better PEP8 is a Sublime plugin which uses the `pep8` or `flake8` command line tool and displays
 the results.

It can be configured to use any other external tool.

**Prerequisites:** [pep8](https://pypi.python.org/pypi/pep8) or [flake8](https://pypi.python.org/pypi/flake8)

**Installation (ubuntu):**

    $ apt-get install pep8 python-flake8

or via PIP:

    $ pip install pep8 flake8

##Installation

**Ubuntu:** `sudo apt-get install pep8 python-flake8`

##Usage

Default command is bind to `CTRL+8`. You can also start it from the sidebar's context menu.
Multiple directories/files are supported.

##Default configuration file

	{
		"flags" : {
			"--max-line-length" : "99",
			"--ignore" : "E126,E127,E128"
		},
		"binary" : "pep8",
		"file-regex" : "(.*):([0-9]*):([0-9]*):[ ](.*)"
	}

Optional property is `line-regex`. The `file-regex` or `line-regex` properties should not be modified if you plan to use pep8 or flake8. Changeg the `binary` property to `flake8` if you wish to use flake8 instead of `pep8`.

##Note

This has been tested to work on Sublime Text 2 and Python 2.7.5+