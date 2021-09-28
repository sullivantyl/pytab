# Riff Memo (pytab)

run with python or with bash script
```
python src/main.py 

./btab 

usage: main.py [-h] [--riff RIFF] [--file FILE] [--measure MEASURE]
               [--strings STRINGS] [--tuning TUNING]

optional arguments:
  -h, --help            show this help message and exit
  --riff RIFF, -r RIFF  eg "E 1 2 4"
  --file FILE, -f FILE  A .riff file
  --measure MEASURE, -m MEASURE
                        The measure length
  --strings STRINGS, -s STRINGS
                        The amount of strings (default: 6)
                        options: 4, 5, 6, 7
  --tuning TUNING, -t TUNING
                        The tuning of the instrument (default: standard)
                        options: standard, halfstep dropd, d, dropc, c, baritone, dropa

```
## File Parsing
You can pass a file with the -f (--file) option. The files first line is the `strings` value, the second line is the `tuning` value, and the third is the `measure` value. All subsequent lines are parsed into the `riff`. This is a good way to recreate output as well as do line by line riffs to keep track of longer runs.

Use `example.riff` to see what this looks like.

## Interactive Mode
If you do not pass a file, you can set the parameters for the riff interactively.

Enter the number of strings.

Enter the tuning for the instrument.

Once entering a riff, if no string is specified, notes will be on the low E string.

To change strings, type the letter of a string followed by a space.

Frets are separated by spaces as well.

eg. 1 4 A 1 4 5  will output:
```
e  |----------------
b  |----------------
G  |----------------
D  |----------------
A  |-----1-4-5------
E  |-1-4------------

```

To type a chord, start with the `:` key and follow it with no spaces by {STRING}{FRET}.

eg. :E1D3 :E3D5  will output:
```
e  |------------
b  |------------
G  |------------
D  |-3--5-------
A  |------------
E  |-1--3-------

```

To add a voice chord, start with `::` and type what you'd like output. It will display on the lowest string of the meter.

eg. :E1D3 :E3D5 - ::Gmaj  will output:
```
e  |-------------------
b  |-------------------
G  |-------------------
D  |-3--5--------------
A  |-------------------
E  |-1--3----Gmaj------

```

String letters are protected, but any other characters go. You can even use the `-` key to create space in the output

eg. 1 2 3 -- 4 /5 h7 -- x x x -- D 5\3 3\2 -- :EXAXDXGX  outputs:
```
e  |-------------------------------------------------
b  |-------------------------------------------------
G  |-----------------------------------------X-------
D  |------------------------------5\3-3\2----X-------
A  |-----------------------------------------X-------
E  |-1-2-3----4-/5-h7----x-x-x---------------X-------

```

After inputing the riff you choose the size of the measure. The default is `60` and is based on character length.
