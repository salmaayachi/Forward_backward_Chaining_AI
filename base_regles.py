
class Base_Regles:
    def __init__(self):

        self.premisses=[]
        self.conclusions=[]
        self.regles=[]

    def Construct_LP_LC(self,file_name): # Construire les listes de prémisses et de conclusions
        br1= open(file_name,'r')
        text=br1.read()
        self.regles=text.split("\n")
        for line in self.regles:
            premisse=self.Extract_Premisse(line)
            self.premisses.append(premisse)
            conclusion=self.Extract_Conclusion(line)
            self.conclusions.append(conclusion)
        #Afficher ces listes dans le fichier log
        log = open("log.txt", "a")
        log.write("liste des premisses \n" +str(self.premisses)+"\n")
        log.write("**************************************** \n")
        log.write("liste des conclusions \n" +str(self.conclusions)+"\n")
        log.write("****************************************\n")


        return self.premisses,self.conclusions,self.regles

    def Extract_Premisse(self,regle):
        a=  (regle.split("si"))
        b = a[1].split("alors")[0]
        return b.strip()

    def Extract_Conclusion(self,regle):
        a=  (regle.split("si"))
        b = a[1].split("alors")[1]
        return b.strip()
    
    def Remove_regle(self, index):
        self.regles.pop(index)
        self.premisses.pop(index)
        self.conclusions.pop(index)

"""def main():
    #file_name=input("Entrer la base de regles")
    b=Base_Regles()
    b.Construct_LP_LC("base_regles_BC1.txt")

if __name__ == "__main__":
    main()"""
    

