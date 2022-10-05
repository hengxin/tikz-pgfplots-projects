tikz-bbox
=========

Copyright 2021 by marmotghost.
v0.1

This file may be distributed and/or modified under the 
LaTeX project public license (LPPL), version 1.3c
see
https://www.latex-project.org/lppl/lppl-1-3c/


The built-in determination of the bounding box in TikZ is not entirely accurate.
This is because, for Bezier curves, it is the smallest box that contains all
control points, which is in general larger than the box that just contains the
curve. This library determines the exact bounding box of the curve.

In order to load this library in a LaTeX document, you need to add 

\usetikzlibrary{bbox}

to the preamble after loading the tikz package. While this library might
possibly work with TeX or ConTeXt, this has never been tested. This library
loads and uses the fpu library. 
