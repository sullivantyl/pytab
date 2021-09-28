import riff_processor

def print_riff(tablature, strings, measure, tuning):
  length_of_tab = len(tablature[list(tablature.keys())[0]])
  rows = length_of_tab / measure
  if length_of_tab % measure > 0:
    rows += 1

  for i in range(0, rows):
    start = i * measure
    end = start + measure

    print("output...\n")
    for ztring in riff_processor.get_strings(strings, tuning):
      print(ztring + " " * (2 - len(ztring)) + " |-" + tablature[ztring][start:end] + "-" * 5)
