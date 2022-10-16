# The 5 Love Languages

def love_language(partner, weeks):
    for i in LOVE_LANGUAGES:
        positive = 0
        neutral = 0
        for j in range(weeks):
            if partner.response(i)=="positive":
                positive += 1
            else:
                neutral += 1       
        if positive > neutral:
            return i
