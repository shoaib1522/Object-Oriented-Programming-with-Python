#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>

using namespace std;

struct city
{
	string name;
	double lat;
	double lon;
};


int distance(city c1[], int s, int t)
{
	// following links can be used to get formula of 
	// computing distance between cities from its
	// spherical coordinates lat, lon
	
	//http://www.satsig.net/maps/lat-long-finder.htm
	//http://universimmedia.pagesperso-orange.fr/geo/loc.htm

	//http://www.movable-type.co.uk/scripts/latlong.html
	
	
	return -999999;// update expression later
}

int main()
{
	const int CITY_COUNT = 74;
	
	city pakcities[CITY_COUNT];

	char cityname[21];

	ifstream db;
	db.open("pakcities.txt");
	
	if(db.is_open())
	{
		int j=0;
		while(db.good())
		{
			db.get(cityname, 21);
			//db.clear();
			pakcities[j].name = string(cityname);
			db >> pakcities[j].lat;
			db >> pakcities[j].lon;
			//db.ignore(); // eating \r to make the next getline safe
			db.ignore(); // eating \n to make the next getline safe
			
			j = j+1;

		}
		db.close();
	}

	// just to test, what was read
	for(int j=0;j<CITY_COUNT;j++)
	{
		cout << setw(20) << pakcities[j].name;
		cout << " ";
		cout << fixed << setprecision(6) << pakcities[j].lat;
		cout << " ";
		cout << fixed << setprecision(6) << pakcities[j].lon;
		cout << endl;
	}
	
	// just to test, call empty function
	cout << endl << endl;
	cout << "Distance between city no. 5 and city no. 10 is "<< distance(pakcities, 5, 10);

	cout << endl;
	return 0;
}
