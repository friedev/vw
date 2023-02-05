# Begin customizable options
LOWDOWN_FLAGS=--out-standalone --html-no-skiphtml --html-no-escapehtml

# Make sure to use the --html-no-skiphtml and --html-no-escapehtml flags
# If you want to include a custom <head>, remove --out-standalone
HEADER_HTML=
FOOTER_HTML=

MD_DIR=md
HTML_DIR=html

# Make sure to use a path relative to files in HTML_DIR
CSS_FILE=
# End customizable options

MD_FILES = $(wildcard md/*)
# md/article.md -> html/article.html
HTML_FILES = $(patsubst $(MD_DIR)/%,$(HTML_DIR)/%,$(MD_FILES:.md=.html))

.PHONY: all
all: $(HTML_FILES)

# html/article.html -> md/article.md
$(HTML_FILES): $(HTML_DIR)/%.html: $(MD_DIR)/%.md
	mkdir -p $(HTML_DIR)
	TITLE=$$(\
		head --lines=1 '$<'\
		| grep '^#'\
		| sed 's/^#*\s*//'\
	);\
	DATE=$$(date --iso-8601);\
	sed 's/\.md)/\.html)/g'\
		< '$<'\
		| cat $(HEADER_HTML) - $(FOOTER_HTML)\
		| lowdown\
		$(LOWDOWN_FLAGS)\
		-m "title:$$TITLE"\
		-m 'css:$(CSS_FILE)'\
		-m "date:$$DATE"\
		-o '$@'

.PHONY: clean
clean:
	$(RM) -r $(HTML_DIR)
