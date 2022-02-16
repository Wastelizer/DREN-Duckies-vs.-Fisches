#!/bin/bash

python3 ./source/data_visualization.py
python3 ./source/solver.py -a 150 50

cd paper
pdflatex  -synctex=1 -interaction=nonstopmode Repro_Paper.tex
pdflatex  -synctex=1 -interaction=nonstopmode Repro_Paper.tex

rm *.aux
rm *.gz
rm *.log
