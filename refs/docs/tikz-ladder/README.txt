Copyright (C) 2018 by Luis Paulo Laus, <laus@utfpr.edu.br>
------------------------------------------------------------

The tikz-ladder package may be distributed and/or modified
under the conditions of the LaTeX Project Public License, 
either version 1 of this license or (at your option) any later
version. The latest version of this license is in: 
  http://www.latex-project.org/lppl.txt and version 1 or
later is part of all distributions of LaTeX version 1999/12/01
or later.

 Version 1.3 2022-04-10


------------------------------------------------------------

Ladder diagram (LD) is a graphical programming language
that has evolved from electrical wiring diagrams for relay
control systems used with programmable controllers (PLC)
as described in the international standard IEC-61131-3. A
LD program enables the programmable controller to test
and modify data by means of standardized graphic symbols.
These symbols are laid out in networks in a manner similar
to a ``rung'' of a relay ladder logic diagram. This library
provides TikZ symbols to draw high quality ladder diagrams.
All standard and some non-standard symbols are possible,
including all kinds of contacts, coils and blocks. I decided
to write this package, despite of the fact that there is
available another package named `ladder' that also uses TikZ
to typeset ladder diagrams, because that package seems to
lack support for blocks. The tikz-ladder, on the contrary,
supports all features described in IEC-61131-3, namely,
blocks (for functions and function blocks), contacts and coils.

------------------------------------------------------------

If you are interest in generating the documentation departing
from tikz-ladder-doc.tex you are going to need pgfmanual-en-macros
available at 
https://mirrors.ctan.org/graphics/pgf/contrib/sa-tikz/doc/macros/pgfmanual-en-macros.tex

------------------------------------------------------------
