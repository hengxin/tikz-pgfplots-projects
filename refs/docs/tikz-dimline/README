# Technical dimension lines in Tikz


Dimension lines are drawn segments that indicate the measurement of a
feature. The line has an arrow at both ends to show that the dimension
displayed covers the entire span of that line. The direction of the line
(vertical, horizontal or diagonal) shows the direction of the
measurement. Dimension lines are kept outside of the object illustrated,
typically connected to other lines that display the area where that
measurement applies. This keeps the illustration clear.



## Installation

To install the `tkiz-dimline` package copy its directory to either to:

- `$TEXHOME/tex/latex/`
- `$TEXMFHOME/tex/latex/`
- `~/texmf/tex/latex/`
- `~/Library/texmf/tex/latex/`

## Usage


````Tex
\begin{tikzpicture}[scale=2]
  \draw[line width=1pt]  (0,0) -- (0,4) -- (.5,4) -- (.5,5) -- (1.,5)
  -- (1.,4) -- (1.5,4) -- (1.5,0) -- cycle;

  \draw node (A) at (2.5,0) {};
  
  \dimline[line style = {line width=0.7},
    extension start length=-0.24,
    extension end length=-0.24] {(A)}{($ (A) + (0,4) $)}{$4.0$};

  \dimline[line style = {red, line width=0.7},
    extension start length=0,
    extension end length=0] {(0,2)}{(1.5, 2)}{ $\diameter 1.5$};

  \dimline[label style={above=0.5ex,},
    extension start path = {(0,6) (0,5.7) (0.5,5.4) (0.5,5.05)},
    extension end path =  {(1.5,6) (1.5,5.7) (1,5.4) (1,5.05)},]
          {(0,6)}{(1.5,6)}{$\diameter 0.5$};
\end{tikzpicture}
````

See [tikz-dimline-doc.pdf](tikz-dimline-doc.pdf) for further help.


## Example

Global dimension line

![Dimension line example 1](dimline1.png)

Normal arrow details

![Dimension line example 2](dimline2.png)

Reversed arrow details

![Dimension line example 3](dimline3.png)



## License

This program is free software. It comes without any warranty, to the extent
permitted by applicable law. You can redistribute it and/or modify it under
the terms of the Do What The Fuck You Want To Public License, Version 2, as
published by Sam Hocevar. See http://sam.zoy.org/wtfpl/COPYING for more
details.
