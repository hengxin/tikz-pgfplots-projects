rem to externalize a figure, un-rem the figure you wish, and run this batch file.

pdflatex --jobname=Figures/threedsurfaceplot tikz-3dplot_documentation.tex
pdflatex --jobname=Figures/examplesurfaceplot  tikz-3dplot_documentation.tex
pdflatex --jobname=Figures/examplesurfaceplotrange  tikz-3dplot_documentation.tex
pdflatex --jobname=Figures/exampleshowargcolorguide  tikz-3dplot_documentation.tex
pdflatex --jobname=Figures/alphabetagamma  tikz-3dplot_documentation.tex
