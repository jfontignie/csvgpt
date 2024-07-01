# CSVGPT
Petit outil pour parser un fichier CSV et ensuite demander un prompt à chatgpt sur le csv. 
Les colonnes peuvent être appelées via $<nom_colonne>

Pour lancer le script:
```
usage: script.py [-h] --csv CSV --output OUTPUT [--overwrite] [--intro INTRO] --prompt PROMPT [--delimiter DELIMITER]
```

## Exemples 

### Exemple 1
Considérer la colonne 1 et la colonne 2 et les appender
```
script.py --csv .\resources\sample.csv --output sandbox\test.csv --overwrite --prompt "concatene '$col1' avec '$col2'"
```

### Exemple 2
Répondre à la question du champ question
```
script.py --csv .\resources\sample.csv --output sandbox\test.csv --overwrite --prompt "Answer to the question '$question'"
```


## Configuration

Créer un fichier config.yaml avec le contenu suivant
```
openai:
  api_key: Clef de chat gpt
  simulate: False #For unit test: Set to true
```