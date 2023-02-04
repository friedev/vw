LOWDOWN_FLAGS=--out-standalone 

MD_DIR=md
HTML_DIR=html

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
		-o '$@'

$(HTML_DIR):
	mkdir -p $(HTML_DIR)

clean:
	$(RM) -r $(HTML_DIR)
