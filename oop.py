#OOP python 
# There are three city which name is Watercity, Skycity, and Landcity in the City district
# In the city, there is different attributes ( for example; Population, Open Area, House, School, Hospital etc )
# In the time being, the size of the all attributes is increased
#In this practice OOP, we plan to set the past and present situation of the city under the Class 'City': District.
#Class of the Project is City
class City():
  
  pass
#Name of the city which is inside the City district
Watercity= City()
Skycity= City()
Landcity= City()
#Watercity details

Watercity.Hospital= 'Koshi hospital';
Watercity.Population= 1000;
Watercity.house= 400;
Watercity.school='Sukuna School';
Watercity.openarea= 6000;

#Skycity details

Skycity.Hospital= 'Mechi hospital';
Skycity.Population= 2000;
Skycity.house= 500;
Skycity.school='Janata School';
Skycity.openarea= 7000;
# Landcity details

Landcity.Hospital= 'Jhapa hospital';
Landcity.Population= 3000;
Landcity.house= 600;
Landcity.school='Rangeli School';
Landcity.openarea= 8000;

print(Watercity.Hospital)
print(Landcity.Population)
print(Landcity.school)
