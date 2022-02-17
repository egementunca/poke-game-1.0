#first, creates user's first pokemon randomly.
#then menu->> 'My Pokemons Menu','Upgrades','Feed','Go Arena','Search for New Pokemon',S
#on the top (SELECT CURRENT POKEMON ,which between user's all pokemons, OPTION)

from poke import Pokemon
import time
import random


earnedMoney = 0 #this is the total money that user earned while playing so cannot be used for in-game.


ALLNUMBERS= list(range(2,802)) 
USEDNUMBERS = list() #after earning a pokemon,it will not be recreated as a opponent
list_difference = [number for number in ALLNUMBERS if number not in USEDNUMBERS]

winTexts=["WOW! That was tough...","YESS !","Good Job.","Easy One!","Jeezzz! Your poke almost died.",
            "YEAPPPP!","Easy Peasy Lemon Squezzy","Ya! Keep goin","That's it","Thats what im talkin aboutt.!!!"]
loseTexts=["Good Try...","Oh! Sorry..","Damn It!","What a dickens...","Unlucky...","Don't forget upgradesss!!",
            "lame -_-","Go train more you fool!","OMG! That was close!!"]


def createPokemon():
    number = random.choice(list_difference)
    USEDNUMBERS.append(number)
    poke = Pokemon(number)
    return poke


def upgrademenu():  
    pass

    

def main():


    ownedPokes = [] #this list contains all the pokes we got
    CurrentPokemon = createPokemon()
    ownedPokes.append(CurrentPokemon)

    money = 0 
    beatedCount = 0 #amount of pokemons that beated in arena -> these two will display on end screen.


    print("""
    --------------------------------
    WELCOME TO THE POKEMON COLLECTOR
    -------------------------------- 
    """)
 

    Run = True
    while Run:
        print("""
            ---------------------------
            Owned Pokemons:%d    Money:%d
            ---------------------------
                
        1) GO TO ARENA
        2) MY BACKPACK
        3) UPGRADE
        4) SELECT POKEMON
            
        """%(len(ownedPokes),money))
        request = input("Request: ")

        # ARENA
        if request == "1":
            Rival = createPokemon()
            winChance = int((CurrentPokemon.total)/(CurrentPokemon.total + Rival.total)*100)
            print("""
                ---------------------------
                Rival: {} | Win Chance: %{}
                ---------------------------
            1) FIGHT!
            2) GO BACK
                """.format(Rival.name,winChance))
            print(winChance)
            request = input("Request: ")
            if int(request) == 1:
                print("BATTLE BEGIN!!!!")
                time.sleep(1)
                #choosing the winner
                if random.randint(1,101)<=winChance:
                    beatedCount+=1
                    ownedPokes.append(Rival)
                    print(random.choice(winTexts))
                    print("You Won!")
                    time.sleep(1)
                    print("%s is added to your collection!"%(Rival.name))
                    print("You earned %s coin!"%(100-winChance))
                    money+=(100-winChance)
                else:
                    print(random.choice(loseTexts))
                    print("You Lost!")
                    time.sleep(1)
                    print("%s is died..."%(CurrentPokemon.name))
                    ownedPokes.remove(CurrentPokemon)

                    if len(ownedPokes) == 0: # Ending situation
                        print("You lost all your poke's...")
                        time.sleep(3/2)
                        print("""
                                Good Game!
                        ---------------------------
                        ↓↓ Here is your records ↓↓
                        ---------------------------
                        Beated %d pokemon,
                        Earned %d coin in total.
                        ---------------------------
                        """%(beatedCount,earnedMoney))
                        Run = False
            elif int(request) == 2:
                main()


        # BACKPACK 
        elif request == "2":
            print("Type 'q' to go back.\n")

            d = dict()
            display_d = dict()

            for index,pokemon in enumerate(ownedPokes):
                d[str(index)] = pokemon
                display_d[str(index)] = pokemon.name
            print(display_d)
            time.sleep(1/2)   


            request = input("Pokemon: ")
            if request in d:
                print("----------------")
                print(d[request])
                print("----------------")
                print("To select as Main Pokemon, type 'main'")
                request2 = input()
                if request2 == 'main':
                    CurrentPokemon=d[request]
                    time.sleep(1/2)
                    print("OK!")
                time.sleep(3)
            else:
                continue


        # UPGRADE
        elif request == "3":
            upgrademenu()

        elif request == "4":
            pass
            



main()

