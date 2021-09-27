# Riff Memo (pytab)

run with python for now
```
python src/main.py

```

Enter the number of strings (default 6 - supports 4,5,6,7).

Once entering a riff, if no string is specified, notes will be on the low E string.

To change strings, type the letter of a string followed by a space.

Frets are separated by spaces as well.

eg. 1 4 A 1 4 5  will output:
```
e |----------------
b |----------------
G |----------------
D |----------------
A |-----1-4-5------
E |-1-4------------

```

To type a chord, start with the `:` key and follow it with no spaces by {STRING}{FRET}.

eg. :E1D3 :E3D5  will output:
```
e |------------
b |------------
G |------------
D |-3--5-------
A |------------
E |-1--3-------

```

String letters are protected, but any other characters go.

eg. 1 2 3 4 /5 h7 x x x D 5\3 3\2 :EXAXDXGX  outputs:
```
e |-------------------------------------
b |-------------------------------------
G |-----------------------------X-------
D |---------------------5\3-3\2-X-------
A |-----------------------------X-------
E |-1-2-3-4-/5-h7-x-x-x---------X-------

```

After inputing the riff you choose the size of the measure. Default is `80` based on char length
