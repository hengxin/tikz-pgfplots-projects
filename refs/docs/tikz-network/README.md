# tikz-network - A tool to visualize complex networks in LaTeX.

## Summary

**tikz-network** is an open source software project for visualizing graphs and
networks in LaTeX. It aims to provide a simple and easy tool to create,
visualize and modify complex networks. The packaged is based on the PGF/TikZ
languages for producing vector graphics from a geometric/algebraic
description. Particular focus is made on the software usability and
interoperability with other tools. Simple networks can be directly created
within LaTeX, while more complex networks can be imported from external
sources (e.g. igraph, networkx, QGIS, ...). Additionally, **tikz-network**
supports visualization of multilayer networks in two and three dimensions.

## Purpose

In recent years, complex network theory becomes more and more popular within the
scientific community. Besides a solid mathematical base on which these theories
are built on, a visual representation of the networks allow communicating
complex relationships to a broad audience.

Nowadays, a variety of great visualization tools are available, which helps to
structure, filter, manipulate and of course to visualize the networks. However,
they come with some limitations, including the need for specific software tools,
difficulties to embed the outputs properly in a LaTeX file (e.g. font type,
font size, additional equations and math symbols needed,...) and challenges
in the post-processing of the graphs, without rerunning the software tools
again.

In order to overcome this issues, the package **tikz-network*** was
created. Since LaTeX is a standard for scientific publications and widely
used, there is a high chance that users are already familiar with the syntax and
the structure of this language. Beside LaTeX, no other software tool is
needed. The commands of **tikz-network** are kept simple but allow a high
control over the produced output. Post-processing of the network (e.g. adding
drawings, images, texts, equations,...) can be done easily, due to the
compatibility with PGF/TikZ (Tantau 2015). Also, the embedding of
the network visualization into the LaTeX-environment enables the use of the
fonts, font sizes, mathematical symbols, hyperlinks, references,..., as used
in the document. Additional features are the three-dimensional visualization of
(multilayer) networks, and the compatible with other layout and visualization
tools (e.g. igraph, netwrokx, QGIS, ...).

## Additional information and examples

- The usage of the package is documented in the
  [manual](https://github.com/hackl/tikz-network/blob/master/manual.pdf)
  ([arXiv](https://arxiv.org/pdf/1709.06005.pdf)).
- The current developer version of the package is available on
  [GitHub](https://github.com/hackl/tikz-network).
- [There](https://github.com/hackl/tikz-network/tree/master/examples), also
  additional (more complex) examples can be found.
- To convert networks from Python into TikZ an API for the package is available
  under <https://pypi.org/project/network2tikz/> or
  <https://github.com/hackl/network2tikz>

## License

Copyright (c) 2019 [Juergen Hackl](mailto:hackl.j@gmx.at)

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <http://www.gnu.org/licenses/>.
