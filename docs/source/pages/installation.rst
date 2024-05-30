############
Installation
############

Code
----
To install:

.. code-block:: console

   poetry install

.. note::
   :class: margin

   Use this if you want to install all of the development packages as well.

.. code-block:: console

   poetry install --with=dev


If you need to `resync` your environment try:

.. code-block:: console

   poetry install --sync

Documentation
-------------



To generate the full documentation use Sphinx [#]_.

.. code-block:: console

   nox -rs show_sphinx


To generate minimal documentation use Pdoc [#]_.

.. code-block:: console

   nox -rs show_pdoc

..
   Footnotes
.. rubric:: Footnotes

.. [#] This will generate a ``index.html`` under ``docs/build/index.html``.
.. [#] This will generate a ``index.html`` under ``save/pdocs/index.html``.
