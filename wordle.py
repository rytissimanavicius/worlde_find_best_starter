# Issiaiskinti kuris angliskas 5 raidziu zodis yra geriausias starteris Wordle zaidime.
#
# 1. Visos zodzio raides turi buti skirtingos.
# 2. Visos to zodzio raides turi sutapti daugiausiai kartu su kitais zodziais.

import os

def main():
    if os.path.exists("output.txt"):
        os.remove("output.txt")
    f = open("words.txt", "r")
    o = open("output.txt", "x")
    score = 0
    top_score = 0
    top_word = ""
    for x in f:
        if len(set(x)) == len(x): # Tik zodziai kurie neturi sutampanciu raidziu.
            f2 = open("words - Copy.txt", "r") # Jeigu lyginami zodziai vienodi gaus +5 score, bet nieko nepakeis.
            for x2 in f2:
                for l in range(5):
                    if x[l] == x2[l]:
                        score += 1
            o.write(f"{score} {x}")    
            if score > top_score:
                top_score = score
                top_word = x
            score = 0
    print(top_score)
    print(top_word)
    
# Visi zodziai prasidedantys su 's' raide turi 
# auksciausia score... Kazkas negerai.
# Galbut tikrina tik pirma raide? Todel tiek vienodai.
        
if __name__ == "__main__":
    main()