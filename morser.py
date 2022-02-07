from morse_codes import morse_stafrof, stafrof_morse

def translate_sentence(sentence):
    r = []
    for char in sentence:
        if char != " ": r.append(stafrof_morse[char.upper()])
        else: r.append(" ")
    return " ".join(r)

def translate_morse(morse):
    r = []
    for char in morse.split(' '):
        print("\"" + char + "\"")
        if char != " " and char != "": r.append(morse_stafrof[char.upper()])
        else: r.append(" ")
    return "".join(r).replace("  ", " ")

def main():
    try:
        while True:
            menu = ["Þýða staf yfir á mors",
                    "Þýða mors yfir í staf",
                    "Þýða setningu yfir á morse",
                    "Þýða setningu aftur frá morse",
                    "Þýða setningu á morse og vista",
                    "Hætta"]
            for i, x in enumerate(menu):
                print(f"{i + 1}. {x}")
            ch = int(input("Sláðu inn val ~ "))
            if ch == 1:
                letter = input("Sláðu inn staf ~ ")
                try:
                    print(f"Stafurinn {letter} á morse er: {stafrof_morse[letter.upper()]}\n")
                except KeyError:
                    print("Þessi stafur finnst ekki í töflunni.\n")
            elif ch == 2:
                morse = input("Sláðu inn morse ~ ")
                try:
                    print(f"\"{morse}\" þýtt er: {morse_stafrof[morse]}\n")
                except KeyError:
                    print("Þetta morse finnst ekki í töflunni.\n")
            elif ch == 3:
                sentence = input("Sláðu inn setningu ~ ")
                try:
                    print(f"Þýdd setning: \"{translate_sentence(sentence)}\"\n")
                except KeyError:
                    print("Það eru ógildir stafir í setningunni! Notaðu enska stafi.\n")
            elif ch == 4:
                morse = input("Sláðu inn morse ~ ")
                try:
                    print(f"Þýdd setning: \"{translate_morse(morse)}\"\n")
                except KeyError:
                    print("Það eru ógildir stafir í setningunni! Ertu viss um að þetta sé gilt morse?\n")
            elif ch == 5:
                sentence = input("Sláðu inn setningu til að vista sem morse ~ ")
                try:
                    translated = translate_sentence(sentence)
                    filename = input("Sláðu inn nafn til að vista morse-ið þitt í (morse.txt) ~ ")
                    with open(f"save/{filename if filename != '' else 'morse.txt'}", 'w+') as file:
                        file.write(translated)
                    print("Vistun tókst!\n")
                except KeyError:
                    print("Það eru ógildir stafir í setningunni! Notaðu enska stafi.\n")
            elif ch == 6:
                exit(0)
            else:
                print("Ógildur innsláttur.\n")
    except KeyboardInterrupt:
        exit(0)

if __name__ == '__main__':
    main()