# Makefile for Physics Laboratory III Experiments

.PHONY: help clean all-reports experiment1 experiment2 experiment3 experiment4 experiment5 experiment6 experiment7 experiment8

help:
	@echo "Physics Laboratory III - Makefile"
	@echo "Available commands:"
	@echo "  help         - Show this help message"
	@echo "  clean        - Clean all generated files"
	@echo "  all-reports  - Generate all PDF reports"
	@echo "  experimentX  - Generate report for experiment X (1-8)"
	@echo ""
	@echo "Usage examples:"
	@echo "  make experiment2  # Generate report for viscosity experiment"
	@echo "  make all-reports  # Generate all reports"

clean:
	@echo "Cleaning generated files..."
	@find . -name "*.aux" -delete
	@find . -name "*.log" -delete
	@find . -name "*.pdf" -delete
	@find . -name "*.toc" -delete
	@find . -name "*.out" -delete
	@find . -name "*.synctex.gz" -delete
	@echo "Clean completed."

experiment1:
	@echo "Generating report for Experiment 1..."
	@cd 1 && python data.py && pdflatex report.tex

experiment2:
	@echo "Generating report for Experiment 2..."
	@cd 2 && python data.py && pdflatex report.tex

experiment3:
	@echo "Generating report for Experiment 3..."
	@cd 3 && python data.py && pdflatex report.tex

experiment4:
	@echo "Generating report for Experiment 4..."
	@cd 4 && python data.py && pdflatex report.tex

experiment5:
	@echo "Generating report for Experiment 5..."
	@cd 5 && python data.py && pdflatex report.tex

experiment6:
	@echo "Generating report for Experiment 6..."
	@cd 6 && python data.py && pdflatex report.tex

experiment7:
	@echo "Generating report for Experiment 7..."
	@cd 7 && python data.py && pdflatex report.tex

experiment8:
	@echo "Generating report for Experiment 8..."
	@cd 8 && python data.py && pdflatex report.tex

all-reports: experiment1 experiment2 experiment3 experiment4 experiment5 experiment6 experiment7 experiment8
	@echo "All reports generated successfully!"
