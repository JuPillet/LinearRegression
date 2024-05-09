## all:
## 	@bash pythenv3.sh
## 	@echo "L'environnement virtuelle a bien été initialiser, lancez le depuis la racine du projet avec la commande:\\nsource ./pythenv3.sh"

install:
	pip3 install --upgrade matplotlib
	pip3 install -r requirement.txt

uninstall:
	pip3 uninstall -r requirement.txt -y

inspy:
	@sudo apt update && apt install python3 python3-pip python3-tk -y

purpy:
	@sudo apt purge python3-pip python3-tk -y

exitenv:
	@deactivate

trainer:
	python3 trainer.py

predicator:
	python3 predicator.py

delete:
	rm -rf pythenv3 modelLR __pycache__

re: delete all