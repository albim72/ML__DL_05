def konkurs(imie,punkty,miejsce):
    return f"uczestnik konkursu -> {imie},liczba punktów: {punkty}, zajęte miejsce: {miejsce}"

def bonus(punkty,bonus):
    if punkty > 50:
        return punkty + bonus
    else:
        return punkty
