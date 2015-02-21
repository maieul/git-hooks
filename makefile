all:
	python export-ctan.py
	cp pre-commit-latex hook-pre-commit-pkg/
	zip -r ../hook-pre-commit-pkg.zip hook-pre-commit-pkg
