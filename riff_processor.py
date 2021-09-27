import re

ZTRINGS = ["e", "b", "G", "D", "A", "E", "B"]

def get_strings(strings=6):
  if strings == 7:
    return ZTRINGS
  elif strings == 4:
    return ZTRINGS[2:6]
  elif strings == 5:
    return ZTRINGS[2:7]
  else:
    return ZTRINGS[0:6]

def build_tabs(riff, strings):
  tablature = dict()
  for ztring in get_strings(strings):
    tablature[ztring] = ""
  curr_ztring = 'E'
  for note in riff.split():
    if note.startswith(":"):
      for ztring in get_strings(strings):
        if ztring in note:
          chordal_fragment = re.search(r'(?:[' + ztring + '])([^BEADGbe]*)', note).group(1)
          tablature[ztring] += chordal_fragment + "-" * (3 - len(chordal_fragment))
        else:
          tablature[ztring] += "-" * 3
    elif note in get_strings(strings):
      curr_ztring = note
      continue
    else:
      for ztring in get_strings(strings): 
        if ztring == curr_ztring:
          tablature[ztring] += note
        else:
          tablature[ztring] += "-" * len(note)
        tablature[ztring] += "-"
  return tablature

