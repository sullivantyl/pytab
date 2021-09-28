import re

ZTRINGS = {
  'standard': ["e", "b", "G", "D", "A", "E", "B"],
  'halfstep': ["eb", "bb", "Gb", "Db", "Ab", "Eb", "Bb"],
  'dropd': ["e", "b", "G", "D", "A", "D"],
  'd': ["d", "a", "F", "C", "G", "D"],
  'dropc': ["d", "a", "F", "C", "G", "C"],
  'c': ["c", "g", "Eb", "Bb", "F", "C"],
  'baritone': ["b", "F#", "D", "A", "E", "B"],
  'dropa': ["e", "b", "G", "D", "A", "E", "A"]
}

def get_strings(strings, tuning):
  if tuning == 'dropa':
    strings = 7

  if strings == 7:
    if tuning == 'dropd' or tuning == 'dropc' or tuning == 'c' or tuning == 'd':
      strings = 6
    else:
      return ZTRINGS[tuning]

  if strings == 4:
    return ZTRINGS[tuning][2:6]

  if strings == 5:
    return ZTRINGS[tuning][2:7]

  return ZTRINGS[tuning][0:6]

def build_tabs(riff, strings, tuning):
  tablature = dict()
  ztrings = get_strings(strings, tuning)
  for ztring in ztrings:
    tablature[ztring] = ""
  curr_ztring = ztrings[-1];
  for note in riff.split():
    if note.startswith("::"):
      for ztring in ztrings:
        if ztring == ztrings[-1]:
          tablature[ztring] += note[2:]
        else:
          tablature[ztring] += "-" * len(note[2:])
        tablature[ztring] += "-"
    elif note.startswith(":"):
      for ztring in ztrings:
        if ztring in note:
          chordal_fragment = re.search(r'(?:[' + ztring +
            '])([^' +
            "".join(ztrings) +
            ']*)', note).group(1)
          tablature[ztring] += chordal_fragment + "-" * (3 - len(chordal_fragment))
        else:
          tablature[ztring] += "-" * 3
    elif note in ztrings:
      curr_ztring = note
      continue
    else:
      for ztring in ztrings:
        if ztring == curr_ztring:
          tablature[ztring] += note
        else:
          tablature[ztring] += "-" * len(note)
        tablature[ztring] += "-"
  return tablature

