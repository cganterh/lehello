.DEFAULT_GOAL = report

.PHONY: _test
_test:
	coverage run tests.py

.PHONY: report
report: _test
	coverage report