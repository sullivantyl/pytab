
import sys, argparse
import riff_processor, outputter

def pytab_run():
  parser=argparse.ArgumentParser()
  parser.add_argument('--riff', '-r', help='eg "E 1 2 4"')
  parser.add_argument('--file', '-f', help='A .riff file')
  parser.add_argument('--measure', '-m', help='The measure length')
  parser.add_argument('--strings', '-s', help='The amount of strings')

  args=parser.parse_args()

  if args.file:
    f = open(args.file, 'r')
    strings = int(f.readline())
    measure = int(f.readline())
    riff = " ".join(f.readlines()).replace('\n', ' ')
  else:
    if args.strings:
      strings = int(args.strings)
    else:
      try:
        strings = int(raw_input("Enter number of strings: "))
      except ValueError:
        strings = 6
    if args.measure:
      measure = int(args.measure)
    else:
      try: 
        measure = int(raw_input("Enter max size of measure: "))
        measure *= 2
      except ValueError:
        measure = 80

    if args.riff:
      riff = args.riff
    else:
      riff = raw_input(
        "Enter a riff (strings:" + 
        str([ele for ele in reversed(riff_processor.get_strings(strings))]) +
        ")\n")

  tablature = riff_processor.build_tabs(riff, strings)
  print("output...\n")
  outputter.print_riff(tablature, strings, measure)

if __name__ == "__main__":
    pytab_run()