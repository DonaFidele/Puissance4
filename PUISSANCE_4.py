#coding:utf-8
import os,sys,time
from random import *
from re import *
from copy import *
class Puissance_4:

    def __init__(self):

        self.grille="""
        ___________a_______________b_________________c_______________d________________e________________f________________g_____________



          |                }                }                }                }                }                }                }
          |                }                }                }                }                }                }                }
          |        01      }      02        }       03       }        04      }        05      }       06       }       07       }
          |                }                }                }                }                }                }                }
          *****************}****************}****************}****************}****************}****************}****************}
          |                }                }                }                }                }                }                } 
          |                }                }                }                }                }                }                }
          |        08      }        09      }       10       }        11      }        12      }        13      }      14        }
          |                }                }                }                }                }                }                }
          |                }                }                }                }                }                }                }
          *****************}****************}****************}****************}****************}****************}****************}                                                                                                               
          |                }                }                }                }                }                }                }
          |                }                }                }                }                }                }                }
          |        15      }         16     }        17      }        18      }       19       }       20       }      21        }
          |                }                }                }                }                }                }                }
          |                }                }                }                }                }                }                }
          *****************}****************}****************}****************}****************}****************}****************}                                                                                                               
          |                }                }                }                }                }                }                }
          |                }                }                }                }                }                }                }
          |        22      }       23       }        24      }       25       }       26       }      27        }      28        }
          |                }                }                }                }                }                }                }
          |                }                }                }                }                }                }                }
          *****************}****************}****************}****************}****************}****************}*****************                                                                                                              
          |                }                }                }                }                }                }                }
          |                }                }                }                }                }                }                }
          |       29       }       30       }       31       }        32      }       33       }      34        }      35        }
          |                }                }                }                }                }                }                }
          |                }                }                }                }                }                }                }
          *****************}****************}****************}****************}****************}****************}****************}                                                                                                            
          |                }                }                }                }                }                }                }
          |                }                }                }                }                }                }                }
          |      36        }       37       }        38      }         39     }        40      }        41      }       42       }
          |                }                }                }                }                }                }                }
          {                }                }                }                }                }                }                }
          {~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}

          """
        self.liste=['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
        self.boule="" ;self.pseudo="";self.ma_boule="";self.grille_1=""
        couleur_boule=compile("(^jaune$)|(^blanc$)") ; 
        self.afficher_plateau()
        self.jouer=True
        while self.pseudo=="":
            self.pseudo=input("Pseudo: ")

        while couleur_boule.search(self.boule) is None:
            self.boule=input("Choisissez votre boule ( blanc🏐️ ou jaune😁️) : ")

        if self.boule=='blanc':
            self.boule='🏐️'
            self.ma_boule='😁️'
        elif self.boule=='jaune':
            self.boule='😁️'
            self.ma_boule='🏐️'
        print(f"Ma boule: {self.ma_boule}")

    def afficher_plateau(self):
        afficher_plateau="""                                                                                     
                             |     |     |     |  🤗️ |     |     |      P             I          S              N               E
                             |_____|_🏐__|_____|_____|_____|_____|              U           S            A              C
                        """                                                   
        print(f"{afficher_plateau * 5}\n\n\n~~~~~~~~~~ ~~~~ ~~~~ 4 ~~~~~~~ ~~~~~~ 4 ~~~~~~~ ~~~~~~~~~   4  ~~~~~ ~~~~~~~~~~~ ~~~~~~~~~~ 4  ~~~~~~~~ ~~~~~~~  4 ~~~~~~~" )

        self.clean(2)
        print("""\n\n                                                (Case: Tapez ici la lettre correspondant à la case de votre choix )
                                                                           
        """)
        self.cases_numbers=compile(r"[0-9][^.]") 
        self.grille_1=self.cases_numbers.sub("  ",self.grille)
        print(self.grille_1)

    def verifier_case(self,case):
        if case not in self.grille:
            return True

    def playeur_game(self):
        ligne_6=compile("3[6-9]|4[0-2]");ligne_6=ligne_6.findall(self.grille)
        case_regex=""
        self.cases_numbers=compile(r"[0-9][^.]")  ;self.cases_numbers_1=compile(r"^[a-g]$")      
        case=""
        if self.cases_numbers_1.search(self.grille) is not None:#vérifier s'il y a toujours des cases vides
            if self.fin()!=1:
                self.jouer=False
                sys.exit()
        
        while self.cases_numbers_1.search(case) is None:#choisir une des 42 cases vides
            case=input("Votre case : ")
        cases_vides=self.cases_numbers.findall(self.grille)

        if case=='a':
            case="36"
            while self.verifier_case(case)==True:
                case=str(int(case)-7)
                if case=='1':
                    case='01'
                elif case=='8':
                    case='08'
                self.verifier_case(case)
        elif case=='b':
            case='37'
            while self.verifier_case(case)==True:
                case=str(int(case)-7)
                if case=='2':
                    case='02'
                elif case=='9':
                    case='09'
                self.verifier_case(case)
        elif case=='c':
            case='38'
            while self.verifier_case(case)==True:
                case=str(int(case)-7)
                if case=='3':
                    case='03'
                self.verifier_case(case)
        elif case=='d':
            case='39'
            while self.verifier_case(case)==True:
                case=str(int(case)-7)
                if case=='4':
                    case='04'
                self.verifier_case(case)
        elif case=='e':
            case='40'
            
            while self.verifier_case(case)==True:
                case=str(int(case)-7)
                if case=='5':
                    case='05'
                self.verifier_case(case)
        elif case=='f':
            case='41'

            while self.verifier_case(case)==True:
                case=str(int(case)-7)
                if case=='6':
                    case='06'
                self.verifier_case(case)
        elif case=='g':
            case='42'
            
            while self.verifier_case(case)==True:
                case=str(int(case)-7)
                if case=='7':
                    case='07'
                self.verifier_case(case)

        self.grille=self.grille.replace(case,self.boule)
        self.grille_1=self.cases_numbers.sub("  ",self.grille)
        self.liste[int(case)-1]=self.boule
        print(self.grille_1)
        if self.end_game()==True:
            print(f" ........🎉️...🎊️.....🎉️..........🎊️.....🎉️.....🎉️........💫️..👑️..🍾️...FELICITATION   ✨️!✨️!✨️!✨️ M\Mme🎊️ {self.pseudo} \n\n🎇️Vous🎊️ avez🎉️ gagné🎉️")
            if self.fin()!=1:
                self.jouer=False
                sys.exit()      

    def ordi_game(self):
        ligne_6=compile("3[6-9]|4[0-2]");ligne_5=compile("29|3[0-5]");ligne_4=compile("2[2-8]");ligne_3=compile("1[5-9]|2[0-1]");ligne_2=compile("08|09|1[0-4]");ligne_1=compile("0[1-7]")
        ligne_6=ligne_6.findall(self.grille);ligne_5=ligne_5.findall(self.grille);ligne_4=ligne_4.findall(self.grille);ligne_3=ligne_3.findall(self.grille);ligne_2=ligne_2.findall(self.grille);ligne_1=ligne_1.findall(self.grille)

        indixe=0;ma_case=""
        liste_copy=deepcopy(self.liste)
        while indixe<42:#verifier les possibilites de gagner
            self.liste=deepcopy(liste_copy)
            if self.liste[indixe]!=self.boule and self.liste[indixe]!=self.ma_boule:
                self.liste[indixe]=self.ma_boule
                if self.end_game()==True and self.verifier_case_en_dessous(str(indixe+1))!= True:
                    self.grille=self.grille.replace(str(indixe+1),self.ma_boule)
                    self.grille_1=self.cases_numbers.sub("  ",self.grille)
                    print(f"{self.grille_1}\n\n\nEt j'ai gagné😏️😎️...........🤣️😂️")
                    if self.fin()!=1:
                        self.jouer=False
                        sys.exit()
                              
            indixe+=1
        self.liste=liste_copy   
        if indixe==42:#vérifier les possibilités de bloquer
            indixe=0
            while indixe<42:
                self.liste=deepcopy(liste_copy)
                if self.liste[indixe]!=self.boule and self.liste[indixe]!=self.ma_boule:
                    self.liste[indixe]=self.boule
                    if self.end_game()==True and self.verifier_case_en_dessous(str(indixe+1))!= True:
                        ma_case=indixe+1
                        self.liste[indixe]=self.ma_boule
                        if indixe<=8:                            
                            self.grille=self.grille.replace(f"{indixe+1:02}",self.ma_boule)
                            self.grille_1=self.cases_numbers.sub("  ",self.grille)
                        else:
                            self.grille=self.grille.replace(f"{indixe+1:01}",self.ma_boule)
                            self.grille_1=self.cases_numbers.sub("  ",self.grille)
                        print(f"{self.grille_1}\n\nA vous de jouer 😏️😎️")
                        
                        indixe=43                   
                indixe+=1

        if indixe==42:
            self.liste=liste_copy
            self.liste=deepcopy(liste_copy)
            if len(ligne_6)!=0:
                ma_case=choice(ligne_6)#choisir parmis les cases vides de la ligne 6
                self.change_grille(ma_case)                #break
            elif len(ligne_5)!=0:
                ma_case=choice(ligne_5)#choisir parmis les cases vides de la ligne 5
                self.change_grille(ma_case)               #break
            elif len(ligne_4)!=0:
                ma_case=choice(ligne_4)#choisir parmis les cases vides de la ligne 4
                self.change_grille(ma_case)                #break
            elif len(ligne_3)!=0:
                ma_case=choice(ligne_3)#choisir parmis les cases vides de la ligne 3
                self.change_grille(ma_case)
            elif len(ligne_2)!=0:
                ma_case=choice(ligne_2)#choisir parmis les cases vides de la ligne 2
                self.change_grille(ma_case)                #break
            elif len(ligne_1)!=0:
                ma_case=choice(ligne_1)#choisir parmis les cases vides de la ligne 1
                self.change_grille(ma_case)      
        
    def change_grille(self,ma_case):
        self.grille=self.grille.replace(ma_case,self.ma_boule)
        self.grille_1=self.cases_numbers.sub("  ",self.grille)
        self.liste[int(ma_case)-1]=self.ma_boule
        print(f"{self.grille_1}")
        if self.end_game()==True:
            print("Et j'ai gagné!!!😏️😎️...........🤣️😂️")
            #self.fin()
            if self.fin()!=1:
                self.jouer=False
                sys.exit()

    def verifier_case_en_dessous(self,case):#si la case en dessous est vide :true
        ligne_6=compile("3[6-9]|4[0-2]");ligne_6=ligne_6.findall(self.grille)
        if int(case)>35:
            return True   
        elif self.liste[int(case)+6]!=self.boule and self.liste[int(case)+6]!=self.ma_boule :
            return True        

    def end_game(self):
       
        ligne_1=[];ligne_2=[];ligne_3=[];ligne_4=[];ligne_5=[];ligne_6=[]
        stickers_winner=compile(r"(😁️\s*\}\s*😁️\s*\}\s*😁️\s*\}\s*😁️)|(🏐️\s*\}\s*🏐️\s*\}\s*🏐️\s*\}\s*🏐️)")
        #cassons self.listes en six lignes manipulables
        for indixe in range(0,7):
            ligne_1+= [self.liste[indixe]]
        for indixe in range(7,14):
            ligne_2+= [self.liste[indixe]]
        for indixe in range(14,21):
            ligne_3+= [self.liste[indixe]]
        for indixe in range(21,28):
            ligne_4+= [self.liste[indixe]]
        for indixe in range(28,35):
            ligne_5+= [self.liste[indixe]]
        for indixe in range(35,42):
            ligne_6+= [self.liste[indixe]]

        for indixe in range(7):#gagner en colonne
            if ligne_6[indixe] == ligne_5[indixe] == ligne_4[indixe] == ligne_3[indixe]==self.boule or ligne_6[indixe] == ligne_5[indixe] == ligne_4[indixe] == ligne_3[indixe]==self.ma_boule:
                return True
            elif ligne_5[indixe] == ligne_4[indixe] == ligne_3[indixe] == ligne_2[indixe]==self.boule or ligne_5[indixe] == ligne_4[indixe] == ligne_3[indixe] == ligne_2[indixe]==self.ma_boule:
                return True
            elif ligne_4[indixe] == ligne_3[indixe] == ligne_2[indixe] == ligne_1[indixe]==self.boule or ligne_4[indixe] == ligne_3[indixe] == ligne_2[indixe] == ligne_1[indixe]==self.ma_boule:
                return True

        for indixe in range(4):#gagner en diagonale montante
            if ligne_6[indixe] == ligne_5[indixe+1] == ligne_4[indixe+2] == ligne_3[indixe+3]==self.boule or ligne_6[indixe] == ligne_5[indixe+1] == ligne_4[indixe+2] == ligne_3[indixe+3]==self.ma_boule:
                return True
            elif ligne_5[indixe] == ligne_4[indixe+1] == ligne_3[indixe+2] == ligne_2[indixe+3]==self.boule or ligne_5[indixe] == ligne_4[indixe+1] == ligne_3[indixe+2] == ligne_2[indixe+3]==self.ma_boule:
                return True
            elif ligne_4[indixe] == ligne_3[indixe+1] == ligne_2[indixe+2] == ligne_1[indixe+3]==self.boule or ligne_4[indixe] == ligne_3[indixe+1] == ligne_2[indixe+2] == ligne_1[indixe+3]==self.ma_boule :
                return True   
        
        for indixe in range(3,7):#gagner en diagonale descendante
            if ligne_6[indixe] == ligne_5[indixe-1] == ligne_4[indixe-2] == ligne_3[indixe-3]==self.boule or ligne_6[indixe] == ligne_5[indixe-1] == ligne_4[indixe-2] == ligne_3[indixe-3]==self.ma_boule:
                return True
            elif ligne_5[indixe] == ligne_4[indixe-1] == ligne_3[indixe-2] == ligne_2[indixe-3]==self.boule or ligne_5[indixe] == ligne_4[indixe-1] == ligne_3[indixe-2] == ligne_2[indixe-3]==self.ma_boule:
                return True
            elif ligne_4[indixe] == ligne_3[indixe-1] == ligne_2[indixe-2] == ligne_1[indixe-3]==self.boule or ligne_4[indixe] == ligne_3[indixe-1] == ligne_2[indixe-2] == ligne_1[indixe-3]==self.ma_boule:
                return True   

        for indixe in range(4):#gagner en horizontale
            if ligne_6[indixe] == ligne_6[indixe+1] == ligne_6[indixe+2] == ligne_6[indixe+3]==self.boule or ligne_6[indixe] == ligne_6[indixe+1] == ligne_6[indixe+2] == ligne_6[indixe+3]==self.ma_boule:
                return True
            elif ligne_5[indixe] == ligne_5[indixe+1] == ligne_5[indixe+2] == ligne_5[indixe+3]==self.boule or ligne_5[indixe] == ligne_5[indixe+1] == ligne_5[indixe+2] == ligne_5[indixe+3]==self.ma_boule:
                return True
            elif ligne_3[indixe] == ligne_3[indixe+1] == ligne_3[indixe+2] == ligne_3[indixe+3]==self.boule or ligne_3[indixe] == ligne_3[indixe+1] == ligne_3[indixe+2] == ligne_3[indixe+3]==self.ma_boule :
                return True   
            elif ligne_2[indixe] == ligne_2[indixe+1] == ligne_2[indixe+2] == ligne_2[indixe+3]==self.boule or ligne_2[indixe] == ligne_2[indixe+1] == ligne_2[indixe+2] == ligne_2[indixe+3]==self.ma_boule:
                return True
            elif ligne_1[indixe] == ligne_1[indixe+1] == ligne_1[indixe+2] == ligne_1[indixe+3]==self.boule or ligne_1[indixe] == ligne_1[indixe+1] == ligne_1[indixe+2] == ligne_1[indixe+3]==self.ma_boule :
                return True           
            elif ligne_4[indixe] == ligne_4[indixe+1] == ligne_4[indixe+2] == ligne_4[indixe+3]==self.boule or ligne_4[indixe] == ligne_4[indixe+1] == ligne_4[indixe+2] == ligne_4[indixe+3]==self.ma_boule :
                return True               

        if stickers_winner.search(self.grille):#gagner en horizontale
                return True
    
    def help(self):
        print("""                        Le jeu <<Puissance 4>> est un jeu de stratégie et plein d'astuce.
                                         Facile à apprendre et amusant à jouer 😏️.Ses règles sont simples.
                                         Chacun essaie d'aligner quatre pions horizontalement,verticalemet
                                         ou diagonalement.Vous aurez à choisir un numero de case et votre 
                                         pion tombera dans la case.Mais attention,le pion tombe dans la g
                                         rille ,il faut d'abord vous assurez que la case sous la case que
                                         vous choisissez n'est pas vide.😎️
                                                    AMUSEZ VOUS BIEN!!!✨️🤣️😂️

            """)

    def fin(self):
        q=int(input("FIN............................................\n\nAPPUYEZ 1 si vous voulez continuer SINON une touche pour quitter.\n"))
        return q
        
            
    def clean(self,temps):
        time.sleep(temps)
        os.system("clear")    


if __name__ == "__main__":
    jeu=Puissance_4() 

    while True:
        #jeu.clean(1)            
        jeu.playeur_game()
        jeu.clean(0)    
        jeu.ordi_game()
        
        
