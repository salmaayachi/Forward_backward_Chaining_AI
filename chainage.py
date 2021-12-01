from base_faits import Base_Faits
from base_regles import Base_Regles

def Forward_Chaining(goal,BF,BR):
    i=0
    log = open("log.txt", "a")
    log.write("Deroulement du Chainage Avant : \n")
    log.write("But a inferer: "+str(goal)+"\n")
    log.write('\n')
    while (goal not in BF.faits) and (len(BR.regles)!=0):
        #print("still in while")
        none_declenchable=False
        for premisse in BR.premisses:
            i=i+1
            cpremisse=premisse
            if BF.check_P_BF(cpremisse):
                log.write("La regle declanchee est : \n"+ str(BR.regles[(BR.premisses).index(premisse)])+"\n")
                BF.Add_Fait(BR.conclusions[(BR.premisses).index(premisse)])
                log.write("conclusion ajoutee a la liste des faits  :\n "+ str(BR.conclusions[(BR.premisses).index(premisse)])+"\n")
                #print("conclusion ajouté à la liste des faits  : ", BR.conclusions[(BR.premisses).index(premisse)]," index: ", i)
                log.write("Nouvelle Base des faits \n" +str(BF.faits)+"\n")
                #print(BF.faits)
                log.write("regle supprimee \n")
                log.write("********** \n")
                BR.Remove_regle((BR.premisses).index(premisse))
                
                none_declenchable=True
        if none_declenchable == False:
            log.write("Aucune Regle Declenchable \n")
            print("Aucune Regle Declenchable")
            break
    if goal in BF.faits:
        log.write(goal + " est etabli")
        print(goal + " est établi")
    else:
        log.write(goal + " est non etabli")
        print(goal+ " non établi")

def Backward_Chaining(goal,BF,BR):
    goals=[goal]
    succeed=True
    log = open("log.txt", "a")
    log.write("Deroulement du Chainage Ariere : \n")
    log.write("But a inferer: "+str(goal)+"\n")
    log.write('\n')
    while True:
        
        if goals[-1] in BF.faits:
            goals.pop()

        if len(goals)==0:
            break

        # si aucune regle declenchable
        if goals[-1] not in BR.conclusions:
            succeed=False
            break

        # Tableau fih les regles declenchables
        regles_declenchables=[]
        i=0
        for conclusion in BR.conclusions:
            if goals[-1] == conclusion:
                premisse= BR.premisses[i]
                premisse_table=premisse.split(" et ")
                regles_declenchables.append((premisse_table,conclusion))
            i+=1
        log.write("Toutes les regles declecnhables : \n"+ str(regles_declenchables)+"\n")
        log.write('\n')

        if len(regles_declenchables)==0:   
            succeed=False
            break
        else:
            regle_declenchable=regles_declenchables[0]
            for tr in regles_declenchables:
                 if len(tr[0])>len(regle_declenchable[0]):
                    regle_declenchable=tr
            log.write("Regle declenchable selon notre critere : \n"+ str(regle_declenchable)+"\n")
            log.write("****************************\n")


            valid=True
            for premisse in regle_declenchable[0]:
                if premisse not in BF.faits:
                    goals.append(premisse)
                    valid=False
            if valid:
                BF.Add_Fait(goals[-1])
                log.write('nouvelle Base des faits \n'+str(BF.faits)+'\n')
    if succeed:
        log.write(str(goal)+" est atteint \n")
        print(goal+" est atteint")
    else:
        log.write(str(goal)+" est non atteint \n")
        print(goal+" non atteint")





def main(): 
    BF=Base_Faits()
    BR=Base_Regles()
    BR.Construct_LP_LC("BR1.txt")
    BF.Construct_LF("BF1.txt")
    goal=input("Donner le but à inférer: ")
    type_chainage=""
    while type_chainage not in ["AR","AV"]:
        type_chainage=input("Taper AV pour chainage avant et AR pour chainage arriere:")
    if (type_chainage =='AV'):
        Forward_Chaining(goal,BF,BR)
    else:
        Backward_Chaining(goal,BF,BR)

if __name__ == "__main__":
    main()