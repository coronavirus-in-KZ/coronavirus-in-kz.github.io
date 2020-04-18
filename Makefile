help:
# выводит содержимое Makefile
	cat Makefile

info:
# выводит git status
	@echo
	@echo "Состояние git"
	git status
	@echo
	@echo "Текущая директория"
	pwd
	@echo
	@echo "Содержимое текущей директории"
	ls -1 -X --group-directories-first
	@echo

enter-data-in-dev:
# checkout develop
# открывает таблицу xlsx для редактирования
	git checkout develop
	xdg-open coronavirus.xlsx

html:
	pipenv run python generate_readme.py

view:
	xdg-open index.html

dev-commit-push:
# делает commit в ветке develop
	git checkout develop
	git pull
	git add .
	git commit --edit --message="Обновил таблицу"
	git push

merge-dev-into-master-push:
# делает marge develop->master
	git checkout master
	git pull
	git merge develop
	git push
