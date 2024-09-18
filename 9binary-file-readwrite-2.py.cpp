#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main() 
{
	double a[4] = {2.5, 6.4, 0.9, 1.2};

	ofstream oof("bin2.txt");
	oof.write((char *)a, sizeof(double)*4);
	oof.close();
	
	a[0]=a[1]=a[2]=a[3]=-1.0;
	cout << a[0] << ' ' << a[1] << ' ' << a[2] << ' ' << a[3] << ' ' << endl;
	
	ifstream iif("bin2.txt");
	iif.read((char *)a, sizeof(a));
	iif.close();
	
	cout << a[0] << ' ' << a[1] << ' ' << a[2] << ' ' << a[3] << ' ' << endl;
	
   return 0;
}