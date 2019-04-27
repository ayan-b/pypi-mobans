all: upstreaming

upstreaming:
	moban -m mobanfile

lint: flake8 . --exclude=.moban.d,docs --builtins=unicode,xrange,long

push:
	git config user.email "travis@travis-ci.org"
	git config user.name "traviscibot"
	git add .
	git reset HEAD =0.0.4
	git commit -m "Sync templates [skip ci]"
	git push https://ayan-b:${GITHUB_TOKEN}@github.com/ayan-b/pypi-mobans HEAD:moban -f
