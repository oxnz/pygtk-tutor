pygtk-tutor_zh_CN.pdf: pygtk-tutor_zh_CN.tex preamble.tex chapter1.tex chapter2.tex
	xelatex $<
test: pygtk-tutor_zh_CN.pdf
	evince $<
clean:
	rm -rf *.toc
	rm -rf *.dvi
	rm -rf *.log
	rm -rf *.aux
.PHONY: clean test
