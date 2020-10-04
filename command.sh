#!/bin/bash/

function createpy() {
	cd ~/Projects/Python/
	mkdir $1
	cd ~/Projects/Python/$1
	python ~/Projects/Python/command_scripts/createpy.py $1
	FILENAME="$2.py"
	touch $FILENAME
	touch README.md
	touch .gitignore
	git init
	git remote add origin # remote code here
	git add README.md
	git add $FILENAME
	git commit -m "initial commit"
	git push -u origin master
	code $FILENAME
}