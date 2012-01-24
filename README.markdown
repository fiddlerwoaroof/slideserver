## Installation


1. Get the source:

      % git clone https://github.com/fiddlerwoaroof/slideserver.git
      Cloning into slideserver...
      remote: Counting objects: 53, done.
      remote: Compressing objects: 100% (43/43), done.
      remote: Total 53 (delta 21), reused 33 (delta 8)
      Unpacking objects: 100% (53/53), done.

2. Install virtualenv:

      % sudo easy_install-2.6 virtualenv
      Password: ...
      Searching for virtualenv
      Reading http://pypi.python.org/simple/virtualenv/
      <snip>
      Installed .../virtualenv-1.7-py2.6.egg
      Processing dependencies for virtualenv
      Finished processing dependencies for virtualenv


3. Install prerequisites:

      % cd slideserver

      % source bin/activate

      % pip install -r requirements.txt
      Downloading/unpacking Mako==0.5.0 (from -r requirements.txt (line 1))
      Downloading Mako-0.5.0.tar.gz (318Kb): 318Kb downloaded
      <snip>
      Successfully installed Mako Flask Twisted markdown pyyaml MarkupSafe Werkzeug Jinja2 zope.interface argparse
      

4. From the demo directory run:

      % cd demo
      % PYTHONPATH=../.. PORT=8081 python -m slideserver.slides slideshow static

5. Navigate to <http://localhost:8081>

