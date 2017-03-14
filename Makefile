#
# Makefile for Thesis
#
# Using AASTex and BibTeX
#

all : thesis.pdf

thesis.pdf : thesis.tex thesis.bib */*.tex 
	pdflatex thesis
	bibtex thesis
	pdflatex thesis
	pdflatex thesis

thesis.dvi : thesis.tex thesis.bib */*.tex 
	latex thesis
	bibtex thesis
	latex thesis
	latex thesis

thesis.ps : thesis.dvi
	dvips thesis

clean:
	rm -fr thesis.dvi thesis.ps thesis.pdf thesis.aux thesis.log \
	thesis.lof thesis.lot thesis.toc thesis.blg thesis.bbl */*.aux *~ 
