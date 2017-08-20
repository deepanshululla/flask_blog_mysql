#!/usr/bin/python3

import os
import sys

# Set the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from flask.ext.script import Manager, Server
from flask.ext.migrate import MigrateCommand
from flask_blog import app
from flask import Flask, url_for


# the below two functions ensure always the latest css file is served thus eliminating css caching
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Turn on debugger by default and reloader
manager.add_command("runserver",Server(
    use_debugger = True,
    use_reloader = True,
    host = os.getenv('IP','0.0.0.0'),
    port = int(os.getenv('PORT', 5000))
))

if __name__ == "__main__":
    manager.run()    
