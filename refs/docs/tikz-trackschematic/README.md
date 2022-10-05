# TikZ-trackschematic

[![License: ISC](https://img.shields.io/badge/license-ISC-green.svg)](https://opensource.org/licenses/ISC) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5539844.svg)](https://doi.org/10.5281/zenodo.5539844) [![continuous integration test](https://github.com/railtoolkit/tikz-trackschematic/actions/workflows/testing.yml/badge.svg)](https://github.com/railtoolkit/tikz-trackschematic/actions/workflows/testing.yml)

------------

# Installation


The tikz library is contained in the files:
* tikz-trackschematic.sty
* tikzlibrarytrackschematic.code.tex,
* tikzlibrarytrackschematic.topology.code.tex,
* tikzlibrarytrackschematic.trafficcontrol.code.tex,
* tikzlibrarytrackschematic.vehicles.code.tex,
* tikzlibrarytrackschematic.constructions.code.tex,
* tikzlibrarytrackschematic.symbology.code.tex,
* tikzlibrarytrackschematic.electrics.code.tex, and
* tikzlibrarytrackschematic.measures.code.tex.

These files should be copied wherever TeX can find it, for example in your $TEXMF folder.

Alternatively, the tikz library is provided by CTAN as "[tikz-trackschematic](https://ctan.org/pkg/tikz-trackschematic)" and is thus part of the TeX Live distribution or can be installed via MiKTeX.

The library can then be loaded through the command
```TeX
\usepackage{tikz-trackschematic}
```
in any LaTeX file.

The library can also be used in [Overleaf](https://www.overleaf.com/read/crrxfcdzbhbd).

------------

# Minimal working example

```TeX
\documentclass{standalone} % LaTeX
\usepackage{tikz-trackschematic} % loading the library

\begin{document}
  \begin{tikzpicture}

    % TikZ command: specify coordinates
    \coordinate (A)   at (0,0);
    \coordinate (B)   at (6,0);
    \coordinate (T)   at (5,0);

    % draw a track
    \maintrack (A) -- (B);

    % place a train on the track
    \train[forward] at (T) label ();

  \end{tikzpicture}
\end{document}
```
results in:

![train on a track](https://raw.githubusercontent.com/railtoolkit/tikz-trackschematic/master/doc/examples/minimal_working_example.png "train on a track")

------------

# Symbology and meaning

Please consult the [symbology table](https://github.com/railtoolkit/tikz-trackschematic/blob/master/doc/symbology-table.pdf) for further information regarding meaning of the symbols.

------------

# Roadmap

  * rethink syntax
  * provide option for internationalziation (i18n)
  * rewrite library with better coding skills
  * include support for glossaries package

------------

# Acknowledgement

  This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No. 826347.

------------

# License
  
  [![Open Source Initiative Approved License logo](https://opensource.org/files/OSIApproved_100X125.png "Open Source Initiative Approved License logo")](https://opensource.org)

  Copyright (c) 2018 - 2022, Martin Scheidt \<m.scheidt@tu-bs.de\> (ISC License)

  Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

  THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.