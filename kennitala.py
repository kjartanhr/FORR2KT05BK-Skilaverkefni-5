from datetime import datetime
from dateutil.relativedelta import relativedelta

class Kennitala:
    def __init__(self, kennitala=None):
        self.kennitala = kennitala

    def __convert_kt_string(self):
        if isinstance(self.kennitala, str):
            return self.kennitala.replace('-', '')
        else:
            return str(self.kennitala)

    def er_logleg(self):
        kt = self.__convert_kt_string()
        sm = int(kt[0:1]) * 3
        sm = sm + int(kt[1:2]) * 2
        sm = sm + int(kt[2:3]) * 7
        sm = sm + int(kt[3:4]) * 6
        sm = sm + int(kt[4:5]) * 5
        sm = sm + int(kt[5:6]) * 4
        sm = sm + int(kt[6:7]) * 3
        sm = sm + int(kt[7:8]) * 2
        sm = 11 - (sm % 11)
        if sm == 11: sm = 0
        return int(kt[8:9]) == sm

    def dagur(self):
        kt = self.__convert_kt_string()
        return kt[0:2]

    def manudur(self):
        kt = self.__convert_kt_string()
        return kt[2:4]

    def ar(self):
        kt = self.__convert_kt_string()
        yy = kt[4:6]
        ce = int(kt[9:10])
        return f"{'20' if ce == 0 else f'1{ce}'}{yy}"

    def vartala(self):
        kt = self.__convert_kt_string()
        return kt[8:9]

    def aldur(self):
        dd = self.dagur()
        mm = self.manudur()
        yyyy = self.ar()
        date = datetime(int(yyyy), int(mm), int(dd))
        curr = datetime.now()
        diff = relativedelta(curr, date)
        return diff.years

def main():
    try:
        kv = input("Sláðu inn kennitölu (t.d. 461202-3490) ~ ")
        kt = Kennitala(kv)
        while True:
            menu = ["Prófa vartölu",
                    "Fá fæðingardag",
                    "Fá fæðingarmánuð",
                    "Fá fæðingarár",
                    "Fá vartölu",
                    "Fá aldur",
                    "Hætta"]
            for i, x in enumerate(menu):
                print(f"{i + 1}. {x}")
            ch = int(input("Sláðu inn val ~ "))
            if ch == 1:
                print(f"Kennitalan er {'lögleg' if kt.er_logleg() == True else 'ólögleg'}.\n")
            elif ch == 2:
                print(f"Fæðingardagur: {kt.dagur()}\n")
            elif ch == 3:
                print(f"Fæðingarmánuður: {kt.manudur()}\n")
            elif ch == 4:
                print(f"Fæðingarár: {kt.ar()}\n")
            elif ch == 5:
                print(f"Vartala: {kt.vartala()}\n")
            elif ch == 6:
                print(f"Aldur: {kt.aldur()}\n")
            elif ch == 7:
                exit(0)
            else:
                print("Ógildur innsláttur.\n")
    except KeyboardInterrupt:
        exit(0)

if __name__ == '__main__':
    main()