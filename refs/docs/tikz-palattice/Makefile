latex = pdflatex
packagename = tikz-palattice
INSTALL_PATH = /usr/local/share/texmf/tex/latex
e1 = example1_linear
e2 = example2_circular
e3 = example3_coordinates
e4 = example4_labels
e5 = elsa
doc = tikz-palattice_documentation

all: doc allexamples
doc: $(doc).pdf
allexamples: $(e1).pdf $(e2).pdf $(e3).pdf $(e4).pdf $(e5).pdf


$(e1).pdf: $(e1).tex
	$(latex) $<

$(e2).pdf: $(e2).tex
	$(latex) $<

$(e3).pdf: $(e3).tex
	$(latex) $<

$(e4).pdf: $(e4).tex
	$(latex) $<

$(e5).pdf: $(e5).tex
	$(latex) $<

$(doc).pdf: $(doc).tex $(e1).pdf $(e5).pdf
	$(latex) $<


install:
	install -m 644 -p -D -v tikz-palattice.sty $(INSTALL_PATH)/$(packagename)/$(packagename).sty
	mktexlsr

clean:
	rm $(e1).pdf $(e2).pdf $(e3).pdf $(e4).pdf $(e5).pdf
