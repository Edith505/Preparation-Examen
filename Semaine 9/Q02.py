class Server:
    def __init__(self, address_ip, nom, statut):
        if(statut in ["démarré","arrêté"]):
            raise Exception ("statut invalides")
        self.address_ip = address_ip
        self.nom = nom
        self.statut = statut

    def __init__(self):
        pass
    
    def demarrer(self):
        self.statut = "démarré"
    
    def arreter(self):
        self.statut = "arrêté"
    
    def afficher_etat(self):
        print(f"Serveur : {self.nom} - IP: {self.address_ip} - Statut: {self.statut}.")
    
s = Server("1", "Serveur1", "arrêté")
s.afficher_etat()
s.demarrer()
s.afficher_etat()  