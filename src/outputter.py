import riff_processor

def print_riff(tablature, strings=6, measure=80):
  rows = len(tablature["E"]) / measure
  if len(tablature["E"]) % measure > 0:
    rows += 1

  for i in range(0, rows):
    start = i * measure
    end = start + measure
    for ztring in riff_processor.get_strings(strings):
      print(ztring + " |-" + tablature[ztring][start:end] + "-" * 5)
    print("\n")