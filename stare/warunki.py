print("ćwiczymy warunki")

temperatura = 16

if temperatura >= 25:
    print("gorąco")
else:
    print("może być")

if temperatura >= 25:
    print("gorąco")
elif temperatura >= 20:
    print("Super")
elif temperatura >=15:
    print("w miarę")
else:
    print("może być")



if temperatura >=25:
    if piwo == "zimne":
        print("ekstra")
    else:
        print ("ciepłe piwo???")
else:
    print("za zimno... :(")

piwo = "zimne"
if temperatura >=25 and piwo == "zimne":
    print("doskonale")
else:
    print("nie pasuje mi...")

piwo = "zimne"

recznik = "jest"

if temperatura >=25 and (piwo == "zimne" or recznik == "jest"):
    print("doskonale")
else:
    print("nie pasuje mi...")


#if (kolor == "biały" or kolor=="czerwony") and lokalizacja == "mazowieckie":
#    print("super")


if temperatura >= 25 and piwo == "zimne":
    print("doskonale")
else:
    print("słabo")
