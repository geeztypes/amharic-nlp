from spacy.cli.train import train

train("./config.cfg", overrides={"paths.train": "./train.spacy", "paths.dev": "./dev.spacy"})
