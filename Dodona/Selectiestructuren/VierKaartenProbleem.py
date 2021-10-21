waarde = str(input())
kleur = input()
omdraaien = str(input())

def Wason(waarde,kleur,omdraaien):
  """checking if the problem of Wason-cards is correctly solved"""
  if waarde == "kleur":
      if kleur == "rood":
        if omdraaien == "ja":
          print(f"Fout: kaarten met kleur rood moeten niet gedraaid worden.")
        else:
          print(f"Juist: kaarten met kleur rood moeten niet gedraaid worden.")
      else:
        if omdraaien == "ja":
          print(f"Juist: kaarten met kleur {kleur} moeten gedraaid worden.")
        else:
          print(f"Fout: kaarten met kleur {kleur} moeten gedraaid worden.")
  else:
      if int(kleur) %2:
        if omdraaien == "ja":
          print(f"Fout: kaarten met waarde {kleur} moeten niet gedraaid worden.")
        else:
          print(f"Juist: kaarten met waarde {kleur} moeten niet gedraaid worden.")
      else:
        if omdraaien == "ja":
          print(f"Juist: kaarten met waarde {kleur} moeten gedraaid worden.")
        else:
          print(f"Fout: kaarten met waarde {kleur} moeten gedraaid worden.")

Wason(waarde,kleur,omdraaien)
