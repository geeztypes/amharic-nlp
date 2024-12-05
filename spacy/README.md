Install https://spacy.io/usage

python -m venv .env
.env\Scripts\activate
pip install -U pip setuptools wheel
pip install -U 'spacy[transformers,lookups]'
python -m spacy download en_core_web_sm

suppress warning

- python -W ignore .\preprocess.py

download a trained model or create one (very tedious and takes a long time)

python -m spacy convert ..\data\am_att-ud-test.conllu ../corpus

create a config file

python -m spacy train config.cfg

To create this dev set, you can first split your original data into train/dev parts, and then run convert separately on each of them, calling the larger one train.spacy and the smaller one dev.spacy. As @mbrunecky suggests, an 80-20 split is usually good, but it depends on the dataset.

For example, en_core_web_sm is a small English pipeline trained on written web text (blogs, news, comments), that includes vocabulary, syntax and entities.

How do generate a small Amharic pipeline trained on written web text (blogs, news, comments), that includes vocabulary, syntax and entities.
