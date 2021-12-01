from base_regles import Base_Regles
class Base_Faits:
    def __init__(self):
        self.faits = [] #liste contenant les faits 

    def Construct_LF (self,file_name): # Construire la liste des faits
        br1= open(file_name,'r')
        text=br1.read()
        self.faits=text.split("\n")
        log = open("log.txt", "a")
        log.write("liste des faits \n" +str(self.faits) +"\n")
        log.write("**************************************** \n")

        return self.faits

    def check_P_BF(self,premisse):# checker si une prémisse (meme complexe) est dans BF 
        if(" et " in premisse):
            while (" et " in premisse):
                premisse = premisse.split(" et ") # liste des prémisses sans et 
                splited_premisse=premisse
        else:
            if premisse in self.faits: # i mean simple premisse
                return True
            else: 
                return False
        

        for element in splited_premisse:
    
            if element not in self.faits:
                return False
        return True


    def regleDeclenchable(self, premisse):
        if(" et " in premisse):
            while (" et " in premisse):
                a = premisse.split(" et ",1)[0]
                premisse = premisse.split(" et ")
                if (a not in self.faits):
                    return False         
        if(premisse in self.faits):
            return True
        else :
            return False

    def Add_Fait(self , fait):
        self.faits.append(fait)


"""def main():
    #file_name=input("Entrer la base de regles")
    b=Base_Faits()
    b.Construct_LF("base_faits_1.txt")
    x=(b.check_P_BF("noir_et_blanc"))
    print(x)
    #b.regleDeclenchable("plumes et non_vole et nage ")

if __name__ == "__main__":
    main()"""