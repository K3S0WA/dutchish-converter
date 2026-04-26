# Dutch-ish Converter

This converts English text into a Dutch-ish phonetic spelling using the CMUdict pronunciations from the `pronouncing` package.

## Run It

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

Run the converter:

```bash
python main.py "I believe this is working."
```

You can also run it with no sentence and type one when prompted:

```bash
python main.py
```

## Run The Web App

Install the dependencies as above, then run:

```bash
streamlit run streamlit_app.py
```

For Streamlit Community Cloud, use `streamlit_app.py` as the app file.
