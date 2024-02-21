all:
	@bash pythenv3.sh
	@echo "L'environnement virtuelle a bien été initialiser, lancez le depuis la racine du projet avec la commande:\\nsource ./pythenv3.sh"

trainer:
	python3 trainer.sh

predicator:
	python3 predicator.sh

delete:
	rm -rf pythenv3 modelLR

re: delete all