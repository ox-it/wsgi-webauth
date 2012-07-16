A WSGI-compliant implementation of WebAuth
==========================================

There's nothing here yet, but here are some useful links:

* `The protocol specification <http://webauth.stanford.edu/protocol.html>`_
* `SPIE <http://projects.oucs.ox.ac.uk/spie/>`_

Desired features
----------------

* WSGI middleware, setting ``REMOTE_USER``
* Django authentication backend

Debugging ideas
---------------

* Point ``mod_webauth`` at a local Apache instance serving HTTP, which proxies
  the Oxford WebKDC over HTTPS, allowing us to see what they're saying to each
  other.

