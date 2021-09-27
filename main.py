
import riff_processor

def pytab_run():
  try:
    strings = int(raw_input("Enter number of strings: "))
  except ValueError:
    strings = 6

  tablature = riff_processor.build_tabs(raw_input(
    "Enter a riff (strings:" + 
    str([ele for ele in reversed(riff_processor.get_strings(strings))]) +
    ")\n"), strings)

  print_riff(tablature, strings)

def print_riff(tablature, strings):
  try: 
    measure = int(raw_input("Enter max size of measure: "))
    measure *= 2
  except ValueError:
    measure = 80
  print("Max measure size: " + str(measure) + "\n")

  rows = len(tablature["E"]) / measure
  if len(tablature["E"]) % measure > 0:
    rows += 1

  for i in range(0, rows):
    start = i * measure
    end = start + measure
    for ztring in riff_processor.get_strings(strings):
      print(ztring + " |-" + tablature[ztring][start:end] + "-" * 5)
    print("\n")

if __name__ == "__main__":
    pytab_run()