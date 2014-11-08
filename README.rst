Daemonify
=========

.. image:: https://github.com/amiralis/daemonify/blob/master/include/daemonify.jpg


Python Daemon Class based on `jejik.com <http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/>`_.

It work on Linux/Unix/Mac, and supports start|stop|restart|status.


Usage
-----

.. code-block:: python

  from daemonify import Daemon
  class App(Daemon):
    def run(self):
      # main logic goes here
      pass

  if __name__ == '__main__':
    app = App('PID')
    app.start()

Installation
------------

To install daemonify, simply: ::

    $ pip install daemonify