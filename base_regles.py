
class Base_Regles:
    def __init__(self):

        self.premisses=[]
        self.conclusions=[]
        self.regles=[]

    def Construct_LP_LC(self,file_name): # Construire les listes de prémisses et de conclusions
        br1= open(file_name,'r')
        text=br1.read()
        self.regles=text.split("\n")
        #print("liste des regles \n" ,self.regles)
        #print(len(self.regles))
        for line in self.regles:
            premisse=self.Extract_Premisse(line)
            self.premisses.append(premisse)
            conclusion=self.Extract_Conclusion(line)
            self.conclusions.append(conclusion)
        print("liste des prémisses \n" ,self.premisses)
        print("****************************************")
        print("liste des conclusions \n" ,self.conclusions)
        print("****************************************")
        #print(len(self.premisses))
        #print(len(self.conclusions))
        #print("liste des regles \n" ,self.regles)

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

    def remove2(self,conclusion,premisse,regle):
        self.conclusions.remove(conclusion)
        self.premisses.remove(premisse)
        self.regles.remove(conclusion)

"""def main():
    #file_name=input("Entrer la base de regles")
    b=Base_Regles()
    b.Construct_LP_LC("base_regles_BC1.txt")

if __name__ == "__main__":
    main()"""
    

