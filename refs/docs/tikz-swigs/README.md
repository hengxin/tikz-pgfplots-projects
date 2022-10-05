Ti*k*Z-SWIGs
=============================================================

The `tikz-swigs` package provides horizontally and vertically split elliptical (pairs of) nodes in Ti*k*Z.

The two new multi-part shapes are `swig hsplit` and `swig vsplit`. These build on and extend the existing `ellipse split` shape provided in the `shapes.multipart` Ti*k*Z library in the following ways:

- Space can be introduced physically separating the two sub-parts.
- The cut that divides the ellipse can be horizontal `hsplit` or vertical `vsplit`.
- The enclosing lines for each sub-part can be colored differently or can be double lines.
- With `vsplit` the position of the dividing line relative to the original undivided ellipse is determined based on the relative size of the label text for the two pieces.
- Anchors determined by angles are supported, for example `mynode.170`.

The package name derives from the fact that split ellipses of this type are used to represent Single-World Intervention Graph (SWIG) models which are used in counterfactual causal inference.

The tikz-swigs package is licensed under the The LaTeX Project Public License 1.3c and the
GNU General Public License, version 2.

Thanks to Robin J. Evans, F. Richard Guo and Ilya Shpitser for providing guidance, motivation and encouragement.

 -- Thomas Richardson <thomasr@uw.edu>  9 July 2021

