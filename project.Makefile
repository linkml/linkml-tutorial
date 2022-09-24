SHEET_MODULE = linkml_tutorial

compile-sheets-manually:
	$(RUN) sheets2linkml --gsheet-id $(SHEET_ID) $(SHEET_TABS) > $(SHEET_MODULE_PATH).tmp && mv $(SHEET_MODULE_PATH).tmp $(SHEET_MODULE_PATH)

## Add your own custom Makefile targets here
