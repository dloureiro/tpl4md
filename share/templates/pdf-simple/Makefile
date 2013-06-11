SOURCE_FILE_NAME = `python ./bin/config_parsing source_file_name`
BOOK_FILE_NAME = `python ./bin/config_parsing destination_file_name`

PDF_BUILDER = pandoc
PDF_BUILDER_SIMPLE_FLAGS = \
        --latex-engine xelatex \
		--listings \
        --template pdf-template-gen.tex

pdf-simple:
	python ./bin/generate_files
	$(PDF_BUILDER) $(PDF_BUILDER_SIMPLE_FLAGS) $(SOURCE_FILE_NAME) -f markdown -o $(BOOK_FILE_NAME).pdf
	rm -rf ./pdf-template-gen.tex
clean:
	rm -f $(BOOK_FILE_NAME).pdf
	rm -f pdf-template-gen.tex