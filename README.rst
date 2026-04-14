Python iTunes
=============

A simple Python wrapper to access `iTunes Search API`_.

.. _iTunes Search API: https://performance-partners.apple.com/search-api

Installation
------------

The library is distributed `on PyPI`_,
and can be installed into a `virtual environment`_ for your project
with ``pip``:

.. code-block:: sh

  $ pip install python-itunes

To install the latest development version,
``pip`` can fetch the source from the Git repository:

.. code-block:: sh

  $ pip install git+https://github.com/ocelma/python-itunes

Usually, you would list this dependency in your ``pyproject.toml``:

.. code-block:: toml

  [project]
  # ...
  dependencies = [
    "python-itunes",
    # or
    "python-itunes @ git+https://github.com/ocelma/python-itunes",
  ]

.. _on PyPI: http://pypi.python.org/pypi/python-itunes
.. _virtual environment: https://docs.python.org/3/library/venv.html

Development
-----------

To hack on the library itself,
create a venv,
and make an *editable* install of the library,
along with development tools:

.. code-block:: sh

  $ git clone https://github.com/ocelma/python-itunes
  $ cd python-itunes
  $ python3 -m venv env
  $ . env/bin/activate
  $ pip install --editable ".[dev]"

If you get an error like this::

  ERROR: File "setup.py" or "setup.cfg" not found. Directory cannot be installed in editable mode: /path/to/python-itunes
  (A "pyproject.toml" file was found, but editable mode currently requires a setuptools-based build.)

...your ``pip`` is too old.
Upgrading the version installed in your venv
will resolve the problem:

.. code-block:: sh

  $ pip install --upgrade pip

Whenever you open a new terminal,
don't forget to re-activate the venv:

.. code-block:: sh

  $ cd python-itunes
  $ . env/bin/activate

Then, when you ``import itunes`` in a Python REPL,
changes made to the library source
are available immediately without reinstalling the package.

Examples
--------

Search
~~~~~~

.. code-block:: python

  import itunes

  # Search band U2
  artist = itunes.search_artist('u2')[0]
  for album in artist.get_albums():
      for track in album.get_tracks():
          print album.get_name(), album.get_url(), track.get_name(), track.get_duration(), track.get_preview_url()

  # Search U2 videos
  videos = itunes.search(query='u2', media='musicVideo')
  for video in videos:
      print video.get_name(), video.get_preview_url(), video.get_artwork()

  # Search Volta album by Björk
  album = itunes.search_album('Volta Björk')[0]

  # Global Search 'Beatles'
  items = itunes.search(query='beatles')
  for item in items:
      print '[' + item.type + ']', item.get_artist(), item.get_name(), item.get_url(), item.get_release_date()

  # Search 'Angry Birds' game
  item = itunes.search(query='angry birds', media='software')[0]
  item.get_version()
  item.get_price()
  item.get_url()
  item.get_seller_url()
  item.get_screenshots()
  item.get_languages()
  item.get_avg_rating()
  item.get_num_ratings()

Lookup
~~~~~~

.. code-block:: python

  import itunes

  # Lookup Achtung Baby album by U2
  U2_ACHTUNGBABY_ID = 475390461
  album = itunes.lookup(U2_ACHTUNGBABY_ID)

  print album.get_url()
  print album.get_artwork()

  artist = album.get_artist()
  tracks = album.get_tracks()

  # Lookup song One from Achtung Baby album by U2
  U2_ONE_ID = 475391315
  track = itunes.lookup(U2_ONE_ID)

  artist = track.get_artist()
  album = track.get_album()

Caching JSON results
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

  import itunes

  if not itunes.is_caching_enabled():
      itunes.enable_caching('/tmp/itunes_cache') #If no param given it creates a folder in /tmp

  #From now on all JSON results are cached here:
  print itunes.__cache_dir

Tests
-----

.. code-block:: sh

  $ pytest
