
run: clean
	python main.py

tests: .PHONY
	python -m unittest -v tests

docs: .PHONY
	(cd docs; make -n html)

clean:
	@find . -type d -name '__pycache__' | xargs rm -rf

build: run tests docs

REQUIREMENTS="requirements.txt"

install:
	@pip install -r $(REQUIREMENTS) | grep -v "already satisfied" || \
		echo "everything from \"$(REQUIREMENTS)\" is up-to-date"

# pseudo goal never created
.PHONY:
