
tikzsymbols
===========

Overview
--------

The *tikzsymbols* package v4.12a (2021/12/14) contains symbols created using tikz.

This package provides:
 * various emoticons
 * cooking symbols
 * trees
 * other symbols (e.g. Penrose-Triangle (Triban), chair, coffeecup, etc.)
 * some tools to create your own tikzsymbol

FAQ
-------
See documentation

Changes
-------
* v1.6  Several bugs fixed and some options added.
* v1.7  New symbols and some `bugs` fixed
* v2.0
  - Bug fixed, now option `tree=on/off` is working again,
  - new symbols: `\Triban`, improved BasicTree code.
  - New option: `marvsoym` (see documentation for more details).
* v2.2
  - Included `\@ifpackageloaded`, now symbols can have negative scale,
  - Did something else, I can't remember.
* v2.25  Changed some code
* v2.5
  - New option: `draftabsolute` (symbols are replaced by text and LateX becomes faster again). Changed manual a bit.
* v3.0
  - Symbols are stored inside a save-box and are used via `\usebox`,
  - New option: `draft=absolute` (old option is still useable, but obsolete),
  - Changed output of `draft=absolute`,
  - New option: `prefix=<prefix>`, adds a `<prefix>` to all commands,
  - New option: `usebox=true/false` If false the symbols aren't stored inside a box,
  - See manual for more changes.
* v3.0a  New cooking-symbols: `\grater`, `\bottle`
* v3.0b  Deleted some non-ASCII characters.
* v3.0g
  - Removed a bug caused by me messing up with commands.
  - Removed package `calc` and replaced `\setlength` with `\pgfmathsetlength`
  - Reworked some code of the symbols.
  - Did not change the manual.
* v3.0h  Created a bug in the process of fixing the last bug, added the forgotten \\fi.
* v3.01alpha Copied the 2e code and started rewriting the code in LaTeX3.
* v3.38  Nearly finished rewriting.
* v3.40  Now everything is coded in LaTeX3.
* v3.40-v3.95 Various fixes and changes.
* v3.95  New emoticon `\(d)Changey`.
* v4.0  Finished reworking the code.
* v4.01
  - Added a known problem to the documentation.
  - New Symbol: `\rollingpin` (and of course the german equivalent `\Nudelholz`)
* v4.02
  - Added option `baseline=true/false` to fix a bug occurring with `todonotes`
  - New Symbols: `\cChangey` and `\dcChangey`
* v4.06
  - New Emoticon: `\(d)Sleepey`.
  - New Emoticon: `\SchrodingersCat`.
  - New option: `global-scale`.
  - New option: `symbol-scale`.
  - `\tikzsymbolsset` now raises a warning if a load-time option is used.
  - Some minor fixes.
* v4.07 Option `usebox` is now usable during the document.
* v4.10
  - Added FAQ.
  - All files are now derived from the .dtx file.
  - New option: `append-style`.
  - New option: `remember-picture`.
  - Internal change: `baseline`.
  - Deleted invisible sign.
  - New symbolpair: `\Knoblauchpresse` and `\garlicpress`.
  - Option `draft` and `final` now set the internal draft boolean locally.
  - Reworked sizes of the plain vanilla draft boxes.
* v4.10a Bugfix: Forgot to remove colors from `\Strichmaxerl`
* v4.10b Bugfix: Replace deprecated `\c_zero` by `0`
* v4.10c Bugfix: Added dimension to `xshift` and `yshift` for `\Fire`, `\Candle` and `\(d)Laughey`
* v4.12
  - New (public) command to define symbols: `\tikzsymbolsdefinesymbol`
  - Some other auxiliary functions `\tikzsymbolsprovideandusesavebox`, `\tikzsymbolssetscaleabs`, `\tikzsymbolsscaleabs`.
  - Continuing with `\tikzsymbols_create_draftbox:nn`, `\tikzsymbols_create_squared_draftbox:n` and `\l_tikzsymbols_if_opt_draft_bool`
  - New symbols: `\Heart` and `\dHeart`
  - New symbol: `\Maskey`
* v4.12a
  - Fixing `final` option.

Requirements
------------

 * expl3 & xparse
 * tikz
 * xcolor
 * xspace
 * l3keys2e

This file contains
------------------

 * README
 * tikzsymbols.pdf
 * tikzsymbols.dtx
 * tikzsymbols.ins

License
-------
This material is subject to the LATEX Project Public License 1.3c. See

  https://www.latex-project.org/lppl/

for the details of that license.


