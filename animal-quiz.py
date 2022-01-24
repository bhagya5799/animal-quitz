

def chek_guess(guess,answer):
    global score
    still_guessing=True
    attempt=0
    while still_guessing and attempt<3:
        if guess.lower()==answer.lower():
            print("correct answer")
            score=score+1
            still_guessing=False
        else:
            if attempt<2:
                guess=input("sorry wrong answer,try again")
            attempt=attempt+1
    if attempt==3:
        print("currect answer is",answer)

score=0
print("guess the animal")
guess1=input("which bear lives  at the north pole?")
chek_guess(guess1,"polar bear")
guess2=input("which is fatest lan animal? ")
chek_guess(guess2,"cheetah")
guess3=input("which is largest animal?")
chek_guess(guess3,"blue whale")
print("your score is "+str(score))
