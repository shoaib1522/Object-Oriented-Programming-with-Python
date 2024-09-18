#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

void ignoreComment(ifstream &file)
{
	char c;
	while(true)
	{
		c = file.peek();
		if (c >= '0' && c <= '9')
		{
			return;
		}
		else if (c == '#')
		{
			file.ignore(4096, '\n');
		}
		else
		{
			file.ignore(1); // fishy
		}
	}
}

struct AsciiPPM{
       char header[2];
       int width;
       int height;
       int shades;
		 int datasize; // width*height*3
       unsigned char data[270000]; // max image size is 270000
};

void fileRead(string fileName, AsciiPPM &pic)
{
     ifstream img(fileName.c_str());
     if (!img.is_open()){
        cout << "Error reading file: " << fileName << endl;
        throw 1;
     }

     //read header
	  img >> pic.header[0] ;
     img >> pic.header[1] ;
     ignoreComment(img);
	  img >> pic.width ;
     ignoreComment(img);
     img >> pic.height ;
     ignoreComment(img);
	  pic.datasize = pic.height * pic.width * 3;
     img >> pic.shades ;
     img.ignore(1);
	  //ignoreComment(img);

	  //read binary data
	  img.read((char *)pic.data, pic.datasize);

     img.close();
}

void fileWrite(string fileName, const AsciiPPM &pic)
{
     ofstream imag(fileName.c_str());
     if (!imag.is_open()){
        cout << "Error writing file: " << fileName << endl;
        throw 2;
     }

     // minimum header, comment may be included if required
	  imag << pic.header[0] ;
     imag << pic.header[1] << endl;
     imag << pic.width << endl ;
     imag << pic.height << endl ;
     imag << pic.shades << endl ;

	  //write binary data
	  imag.write((char *)pic.data, pic.datasize);

     imag.close();
}

int main()
{
	cout << "Program converting an image to its negative" << endl;
	cout << "This may take some time, please wait . . ." << endl;

    AsciiPPM BKA;
	 try
	 {
		fileRead("brian_kernighan_binary.ppm", BKA);
	 }
	 catch(int ex_no)
	 {
		 if(ex_no == 1)
		 {
			 cout << "Error reading file: brian_kernighan_binary.ppm" << endl;
		 }
		 else
		 {
			 cout << "An unknown error occurs" << endl;
		 }
		 return 1;
	 }
    //fileWrite("brian_kernighan_new.ppm", BKA);

	 int r,c,t;
    AsciiPPM newBKA = BKA;
	 newBKA.width = BKA.height;
	 newBKA.height = BKA.width;
	 
	 for (long i=0;i<BKA.datasize;i+=3)
    {
		 r = i / 3 / BKA.width;
		 c = i / 3 % BKA.width;
		 t = 3 * (c*newBKA.width+r);
       newBKA.data[t] = BKA.data[i];
       newBKA.data[t+1] = BKA.data[i+1];
       newBKA.data[t+2] = BKA.data[i+2];
	 }

    //fileWrite("brian_kernighan_new.ppm", BKA);
	 try
	 {
		fileWrite("brian_kernighan_new.ppm", newBKA);
	 }
	 catch(int ex_no)
	 {
		 if(ex_no == 2)
		 {
			 cout << "Error writing file: brian_kernighan_new.ppm" << endl;
		 }
		 else
		 {
			 cout << "An unknown error occurs" << endl;
		 }
		 return 1;
	 }

	cout << "Conversion completed, thanks" << endl;

	return EXIT_SUCCESS;
}
