# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur apiet fungerar
# vi använder oss enbart av /nobelPrizes
# Dokumentation, hjälp samt verktyg för att testa apiet fins här:
# https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1
import pprint
# from prettyprint import prettyprint

from tentamen_2021.nobel_prize_api import get_nobel_prize_data


HELP_STRING = """
Ange ett år och fält
Exempelvis 1965 fysik
Fält: fysik, kemi, litteratur, ekonomi, fred, medicin
Ange Q för att avsluta programmet
"""

fields = {"fysik": "phy",
           "kemi": "che",
           "litteratur": "lit",
           "ekonomi": "eco",
           "fred": "pea",
           "medicin": "med"}


# TODO 10p programmet skall ge en hjälpsam utskrift istället för en krasch om användaren skriver in fel input
# TODO 15p om användaren inte anger ett område som exempelvis fysik eller kemi så skall den parametern
#  inte skickas med till apiet och vi får då alla priser det året


def main():
    print(HELP_STRING)
    while True:
        # TODO 5p Skriv bara ut hjälptexten en gång när programmet startar
        #  inte efter varje gång användaren matat in en fråga
        #  Förbättra hjälputskriften så att användaren vet vilka fält, exempelvis kemi som finns att välja på DONE

        # TODO 5p Gör så att det finns ett sätt att avsluta programmet,
        #  om användaren skriver Q så skall programmet stängas av
        #      Beskriv i hjälptexten hur man avslutar programmet DONE

        user_input = input(">")
        if user_input.upper() == 'Q':
            break
        year, field = user_input.split()
        prize_category = fields[field]

        nobel_prize_data = get_nobel_prize_data(prize_category, year)

        # TODO 5p Förbättra programmet så att vi får tydligare output.
        #  Nu är det svårt att läsa om det är flera mottagare av ett pris
        for nobel_prize in nobel_prize_data["nobelPrizes"]:
            prize_amount = nobel_prize["prizeAmount"]
            # prize_amount_adjusted = nobel_prize["prizeAmountAdjusted"]
            print(f"{nobel_prize['categoryFullName']['se']} prissumma {prize_amount} SEK")

            print(pprint.pformat(nobel_prize))

            print()
            for recipient in nobel_prize["laureates"]:
                print(recipient['knownName']['en'])
                print(recipient['motivation']['en'])
                # andel = recipient['portion']
        # TODO 10p Skriv ut hur mycket pengar varje pristagare fick,
        #  tänk på att en del priser delas mellan flera mottagare, skriv ut både i dåtidens pengar och dagens värde
        #  Feynman fick exempelvis 1/3 av priset i fysik 1965, vilket borde gett ungefär 282000/3 kronor i
        #  dåtidens penningvärde


if __name__ == '__main__':
    main()
