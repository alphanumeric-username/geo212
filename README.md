# GEO212 lib

Implementation of the algorithms covered in the GEO212 class at UFBA.

## Modules

- `geo212.statistics`: Contains various statistical functions;

## Installation

### For users

```sh
pip install .
```

### For developers

```sh
# Create a Conda environment
conda env create -n geo212-dev python==3.11
# Install the required packages
pip install -r requirements-dev.txt
# Install the geo212 as an editable package
pip install -e .
```

In order to run the unit tests, enter the `tests/` directory and execute `pytest`:

```sh
cd tests
pytest
```
