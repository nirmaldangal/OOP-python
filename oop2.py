class City():
    def __init__(self, Hospital, Population, House, School, Openarea):
        self.Hospital= Hospital
        self.Population= Population
        self.House= House
        self.School= School
        self.Openarea= Openarea
        self.completecitydetails= 'This is the name of the hospital'+' '+Hospital+' '+ 'and population is' +' '+ str(Population)


Watercity= City('Koshi hospital',1000, 400, 'Sukuna School',4000)
Skycity= City('Mechi hospital', 5000, 500,'Janata School', 5000)
Landcity= City('Jhapa hospital', 4300, 600, 'rangeli school', 3000)

print(Watercity.Population)
print(Landcity.School)
#Watercity.completecitydetails()
print(Watercity.completecitydetails)

