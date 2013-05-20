SOURCE_FILE_NAME = `python ./bin/config_parsing source_file_name`
BOOK_FILE_NAME = `python ./bin/config_parsing destination_file_name`

EPUB_BUILDER = pandoc
EPUB_BUILDER_FLAGS = \
	--toc

epub:
	python ./bin/generate_files
	$(EPUB_BUILDER) $(EPUB_BUILDER_FLAGS) title-gen.txt $(SOURCE_FILE_NAME) -o $(BOOK_FILE_NAME).epub
	rm -rf title-gen.txt

clean:
	rm -f $(BOOK_FILE_NAME).epub
	rm -f title-gen.txt