DOCS_DIR=./docs/

init:
	pip install -r requirements.txt

render: assets
	mkdir -p $(DOCS_DIR)
	python3 render.py

clean::
	rm -rf $(DOCS_DIR)


local: assets
	mkdir -p $(DOCS_DIR)
	python3 render.py --local

STATIC_DIR := docs
LOCAL_FRONTEND :=../frontend

assets/css:
	mkdir -p $(STATIC_DIR)/stylesheets
	cd $(LOCAL_FRONTEND) && gulp stylesheets
	rsync -r $(LOCAL_FRONTEND)/digital_land_frontend/static/stylesheets/ $(STATIC_DIR)/stylesheets/

assets/js:
	mkdir -p $(STATIC_DIR)/javascripts
	cd $(LOCAL_FRONTEND) && gulp js
	rsync -r $(LOCAL_FRONTEND)/digital_land_frontend/static/javascripts/ $(STATIC_DIR)/javascripts/

assets:: assets/css assets/js