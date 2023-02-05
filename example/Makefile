# Begin customizable options
LOWDOWN_FLAGS=--out-standalone 

CSS_FILE=

MD_DIR=md
HTML_DIR=html
# End customizable options

MD_FILES = $(wildcard md/*)
HTML_FILES = $(patsubst $(MD_DIR)/%,$(HTML_DIR)/%,$(MD_FILES:.md=.html))

.PHONY: all
all: $(HTML_FILES)

$(HTML_FILES): $(HTML_DIR)/%.html: $(MD_DIR)/%.md $(HTML_DIR)
	sed 's/\.md)/\.html)/g'\
		< '$<'\
		| lowdown\
		$(LOWDOWN_FLAGS)\
		-m "title:$$(head --lines=1 '$<' | grep '^#' | sed 's/^#*\s*//')"\
		-m 'css:$(CSS_FILE)'\
		-m "date:$$(date --iso-8601)"\
		-o '$@'

$(HTML_DIR):
	mkdir -p $(HTML_DIR)

.PHONY: clean
clean:
	$(RM) -r $(HTML_DIR)
