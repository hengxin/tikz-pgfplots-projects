Copyright (C) 2017-2022 by Luis Paulo Laus, <laus@utfpr.edu.br>
------------------------------------------------------------

The tikz-karnaugh package may be distributed and/or modified under the conditions of the LaTeX Project Public License, either version 1 of this license or (at your option) any later version. The latest version of this license is in: 
  http://www.latex-project.org/lppl.txt and version 1 or
later is part of all distributions of LaTeX version 1999/12/01 or later.

 Version 1.5 of 15 February 2022

------------------------------------------------------------

The tikz-karnaugh package is a LaTeX package used to draw Karnaugh maps. It uses TikZ to produce high quality graph from 1 to 12 variables, but this upper limit depends on the TeX memory usage and can be different for you. It is very good for presentation since TikZ allows for a better control over the final appearance of the map. You can control colour, styles and distances.

It can be considered an upgrade and extension of Andreas W. Wieland's karnaugh package towards TikZ supporting. Upgrade because uses TikZ for more option on typesetting and overall higher quality. Extension because it also supports American style and inputting the values as they would appear in the map or in the truth table. Complex maps with solution (implicants) pointed out can be generated with external java software (see documentation for details).

It supports both American and traditional (simplified labels) styles and from version 1.3 on American style is natively supported, therefore, no more addition work is required to typeset Gray coded labels, variable names etc. From version 1.4, two new macros allow typesetting a map much more similarly as it should appear. Original order, as the values appear in the truth table, still being supported. 

------------------------------------------------------------

If you are interest in generating the documentation departing from tikz-karnaugh-doc.tex you are going to need pgfmanual-en-macros available at ctan:/graphics/pgf/base/doc/macros/pgfmanual-en-macros.tex
https://mirrors.ctan.org/graphics/pgf/contrib/sa-tikz/doc/macros/pgfmanual-en-macros.tex

------------------------------------------------------------
