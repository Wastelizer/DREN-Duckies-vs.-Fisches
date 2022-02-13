python ../source/import_csv.py
python ../source/solver.py -a 150 50

REM first to build the PDF-File
pdflatex -synctex=1 -interaction=nonstopmode Repro_Paper.tex 

REM second to create the references in the PDF-file
pdflatex -synctex=1 -interaction=nonstopmode Repro_Paper.tex 

REM delete system-files for creating the output PDF
del *.aux
del *.gz
del *.log
