To Install
      
      % cd /path/to/slideserver
      % virtualenv -p python2.7 .
      % source bin/activate
      % pip install -r requirements.txt

From the demo directory run:

      % PYTHONPATH=../.. PORT=8081 python -m slideserver.slides slideshow static

The demo slideshow will be served at <http://localhost:8081>