# Riff Memo (pytab)

run with python or with bash script
```
python src/main.py 

./btab 

optional arguments:
  -h, --help            show this help message and exit
  --riff RIFF, -r RIFF  "E 1 2 4"
  --file FILE, -f FILE  /path/to/riff.riff
  --measure MEASURE, -m MEASURE
                        The measure length
  --strings STRINGS, -s STRINGS
                        The number of strings

```
## File Parsing
You can pass a file with the -f (--file) option. The files first line is the `strings` value and the second is the `measure` value. All subsequent lines are parsed into the `riff`. This is a good way to recreate output as well as do line by line riffs to keep track of longer runs.

## Interactive Mode
If you do not pass a file, you can set the parameters for the riff interactively.

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
