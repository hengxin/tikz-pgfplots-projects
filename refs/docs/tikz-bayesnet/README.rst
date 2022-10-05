BayesNet
========

TikZ library for drawing Bayesian networks, graphical models and (directed) factor
graphs in LaTeX.

Contents
--------

Provides the following node styles:

* :code:`latent`

* :code:`obs`

* :code:`det`

* :code:`const`

* :code:`factor`

* :code:`plate`

* :code:`gate`

Provides the following commands (note that any of the arguments can be
empty):

* :code:`\factor [options] {name} {caption} {inputs} {outputs}`

* :code:`\plate [options] {name} {fitlist} {caption}`

* :code:`\gate [options] {name} {fitlist} {inputs}`

* :code:`\vgate {name} {fitlist-left} {caption-left} {fitlist-right}
  {caption-right} {inputs}`

* :code:`\hgate {name} {fitlist-top} {caption-top} {fitlist-bottom}
  {caption-bottom} {inputs}`

* :code:`\edge [options] {inputs} {outputs}`

* :code:`\factoredge [options] {inputs} {factors} {outputs}`

Usage
-----

Install the package by copying tikzlibrarybayesnet.code.tex to your
LaTeX system or copy the file into projects that are using it.  To use
the library in your LaTeX file

.. code-block:: python

   \usepackage{tikz}
   \usetikzlibrary{bayesnet}

Compile the LaTeX example:

.. code-block:: none

   pdflatex example.tex

and see the resulting PDF file example.pdf.

Example
-------

.. figure:: http://i.imgur.com/CzNyk.png
   :align: center
   :alt: Bayesian network.

   PCA model as a Bayesian network and a directed factor graph.

.. figure:: http://i.imgur.com/CBZqL.png
   :align: center
   :alt: Citation influence model

   Directed factor graph of the citation influence model.


Related projects
----------------

This library is derived from a technical report "Directed Factor Graph
Notation for Generative Models" and the accompanying TikZ macros by
Laura Dietz 2010 (http://people.cs.umass.edu/~dietz/).

GraphViz (http://www.graphviz.org/) is a more general open source
graph visualization software.  It uses DOT file format to describe the
structure of the graph.  The DOT file can be converted to LaTeX using
:code:`dot2tex` (http://www.fauskes.net/code/dot2tex/).

UAI (http://graphmod.ics.uci.edu/uai08/FileFormat) is a simple text
file format to describe Markov networks. The UAI file format can be
converted to DOT file format using :code:`uai2dot`
(https://github.com/drewfrank/uai2dot).

License
-------

| Copyright (C) 2010-2011 Laura Dietz
| Copyright (C) 2012 Jaakko Luttinen jaakko.luttinen@aalto.fi

This work may be distributed and/or modified under the conditions of
the LaTeX Project Public License, either version 1.3 of this license
or (at your option) any later version.  The license is in the file
LICENSE_LPPL and the latest version of this license is in
http://www.latex-project.org/lppl.txt and version 1.3 or later is part
of all distributions of LaTeX version 2005/12/01 or later.

This work is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.  This work is distributed in the hope that
it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See
the GNU General Public License for more details.  See the license in
the file LICENSE_GPL or visit <http://www.gnu.org/licenses/>.


