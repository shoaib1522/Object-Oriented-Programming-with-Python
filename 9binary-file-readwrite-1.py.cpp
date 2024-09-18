#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main() 
{
	char a[21] = "Pakistan";
	a[20] = '\0';

	ofstream oof("bin1.txt");
	oof.write(a,21);
	oof.close();
	
	strcpy(a,"a quick brown fox");
	cout << a << endl;
	
	ifstream iif("bin1.txt");
	iif.read(a,4);
	iif.close();
	
	cout << a << endl;
	
   return 0;
}