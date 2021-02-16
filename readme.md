# StriPDF

A web application that strips write and print protections from a readable PDF.

# Usage

## Requirements

* flask
* flask-wtf
* pikepdf

## Starting the Server

Start the server with `run.py`. By default it will be accessible at `localhost:9999`. To
make the server world-accessible or for other options, see `run.py -h`.

If you're having trouble configuring your sever, I wrote a
[blog post](http://blog.spurll.com/2015/02/configuring-flask-uwsgi-and-nginx.html)
explaining how you can get Flask, uWSGI, and Nginx working together.

# Thanks

This is basically just a web wrapper for [pikepdf](https://github.com/pikepdf/pikepdf). So thanks to to folks who made that!

# License Information

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

Like [pikepdf](https://github.com/pikepdf/pikepdf) (which does all of the heavy lifting here), this work is licensed under [MPL 2.0](https://www.mozilla.org/en-US/MPL/2.0/).

Remember: [GitHub is not my CV.](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/)
