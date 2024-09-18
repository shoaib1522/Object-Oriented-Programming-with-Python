#include <iostream>
#include <fstream>
#include <string>

using namespace std;

struct city
{
	char name[21];
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
	
	
	return -999999;
}

int main()
{
	city pakcities[100];
	int CITY_COUNT = 0;
	
	ifstream db;
	db.open("pakcities.bin", ios::binary);
	
	if(db.is_open())
	{
		db.read((char *)(&CITY_COUNT), sizeof(CITY_COUNT));
		int j=0;
		while(db.good())
		{
			db.read((char *)(&pakcities[j]), sizeof(city));
			j = j+1;
		}
		db.close();
	}

	// just to test, what was read
	for(int j=0;j<CITY_COUNT;j++)
	{
		cout << pakcities[j].name << " " << pakcities[j].lat << " " << pakcities[j].lon << endl;
	}
	
	// just to test, call empty function
	cout << "Distance b/w 5 and 10 is "<< distance(pakcities, 5, 10);

	cout << endl;
	return 0;
}
