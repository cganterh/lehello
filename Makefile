.DEFAULT_GOAL = report

.PHONY: install
install:
	pipenv $@ --dev

.PHONY: _test
_test: install
	flake8 .
	coverage run tests.py

.PHONY: report
report: _test
	coverage report

.PHONY: sdist bdist_wheel
sdist bdist_wheel: _test
	python setup.py $@
