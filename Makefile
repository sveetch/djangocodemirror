FOUNDATION_VERSION=5.5.3

.PHONY: help clean delpyc tests flake quality

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  delpyc              -- to remove all *.pyc files, this is recursive from the current directory"
	@echo "  clean               -- to clean local repository from all stuff created during development"
	@echo
	@echo "  flake               -- to launch Flake8 checking on boussole code (not the tests)"
	@echo "  tests               -- to launch tests using py.test"
	@echo "  quality             -- to launch Flake8 checking and tests with py.test"
	@echo "  release             -- to release new package on Pypi (WARNING)"
	@echo
	@echo "  server              -- to launch a Django instance on 0.0.0.0:8001"
	@echo

delpyc:
	find . -name "*\.pyc"|xargs rm -f

clean: delpyc
	rm -Rf dist .tox djangocodemirror.egg-info .cache project_test/.cache/ project_test/tests/__pycache__/

flake:
	flake8 --show-source djangocodemirror

tests:
	py.test -vv --exitfirst project_test/

quality: tests flake

server:
	cd project_test && ./manage.py runserver 0.0.0.0:8001 --settings=project.settings_demo

release:
	python setup.py sdist
	python setup.py sdist upload

install-foundation:
	rm -Rf foundation5
	foundation new foundation5 --version=$(FOUNDATION_VERSION)
	@echo "Foundation v$(FOUNDATION_VERSION) sources has been installed, now you should synchronize assets using 'syncf5' action"

syncf5:
	@echo "* Updating jQuery sources"
	cp foundation5/bower_components/jquery/dist/jquery.js foundation5/bower_components/foundation/js/vendor/jquery.js
	@echo "* Updating Foundation static files"
	rm -Rf project_test/project/static/js/foundation5
	cp -r foundation5/bower_components/foundation/js project_test/project/static/js/foundation5
	@echo "* Cleaning vendor libs"
	rm -Rf project_test/project/static/js/foundation5/vendor
	mkdir -p project_test/project/static/js/foundation5/vendor
	@echo "* Getting the real sources for updated vendor libs"
	cp foundation5/bower_components/fastclick/lib/fastclick.js project_test/project/static/js/foundation5/vendor/
	cp foundation5/bower_components/foundation/js/vendor/jquery.js project_test/project/static/js/foundation5/vendor/
	cp foundation5/bower_components/jquery-placeholder/jquery.placeholder.js project_test/project/static/js/foundation5/vendor/
	cp foundation5/bower_components/jquery.cookie/jquery.cookie.js project_test/project/static/js/foundation5/vendor/
	cp foundation5/bower_components/modernizr/modernizr.js project_test/project/static/js/foundation5/vendor/
	@echo "* Updating Foundation SASS sources"
	rm -Rf sass/foundation5
	cp -r foundation5/bower_components/foundation/scss sass/foundation5
