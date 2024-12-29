familytreemaker
===============

This program creates family tree graphs from simple text files.

The input file format is very simple, you describe persons of your family line
by line, children just have to follow parents in the file. Persons can be
repeated as long as they keep the same name or id. An example is given in the
file `LouisXIVfamily.txt`.


Installation
------------

1. Clone the repo.
2. Create and activate a virtual environment

    ```bash
    python3.12 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the local Python package using pip in editable mode: 
    ```bash
    pip install --editable .
    ```

Usage
-----

The sample family descriptor `LouisXIVfamily.txt` is here to show you the
usage. With the activated environment, simply run:

```bash
python scripts/create.py -a 'Louis XIV' familytreemaker/examples/LouisXIVfamily.txt | dot -Tpng -o familytreemaker/examples/LouisXIVfamily.png
```
It will generate the tree from the infos in `LouisXIVfamily.txt`, starting from
*Louis XIV* and saving the image in `LouisXIVfamily.png`.

You can do both steps seperately, as well:
```bash
python scripts/main.py -a 'Louis XIV' familytreemaker/examples/LouisXIVfamily.txt
dot familytreemaker/examples/LouisXIVfamily.dot -Tpng -o familytreemaker/examples/LouisXIVfamily.png
```
This script outputs a graph descriptor in DOT format. To make the image
containing the graph, you will need a graph drawer such as [GraphViz][1].

You can see the result:

![result: LouisXIVfamily.png](/LouisXIVfamily.png)
