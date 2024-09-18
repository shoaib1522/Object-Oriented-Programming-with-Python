#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

using namespace std;

void ignoreComment(ifstream &file)
{
	char c;
	while(true)
	{
		file >> ws;
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
			file.ignore(1);
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
     ignoreComment(img);

	  //loop and read data
	  int pval;
     for(int i=0; i<pic.datasize; i++)
	  {
		  img >> pval;
		  pic.data[i] = pval;
	  }
	  
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

	  //loop and write data
     for(int i=0; i<pic.datasize; i++)
	  {
		  if (i > 0 && i%15 == 0)
		  {
			  imag << endl;
		  }
		  imag << int(pic.data[i]) << " ";
	  }

     imag.close();
}

int main()
{
	cout << "Program converting an image to its negative" << endl;
	cout << "This may take some time, please wait . . ." << endl;

    AsciiPPM BKA;
	 fileRead("brian_kernighan_ascii.ppm", BKA);
    //fileWrite("brian_kernighan_new.ppm", BKA);

    AsciiPPM newBKA = BKA;
	 for (long i=0;i<BKA.datasize;i++)
    {
        newBKA.data[i] = BKA.shades - BKA.data[i];

        //newBKA.data[BKA.datasize-i-1] = BKA.data[i];
        //newBKA.data[i] = i%3 == 0 ? (BKA.data[i]+BKA.data[i+1]+BKA.data[i+2])/3 : 0;
        //newBKA.data[i] = i%3 == 1 ? (BKA.data[i-1]+BKA.data[i]+BKA.data[i+1])/3 : 0;
        //newBKA.data[i] = i%3 == 2 ? (BKA.data[i-2]+BKA.data[i-1]+BKA.data[i])/3 : 0;
        //newBKA.data[i] = i % newBKA.width;
	 }

    //fileWrite("brian_kernighan_new.ppm", BKA);
    fileWrite("brian_kernighan_new.ppm", newBKA);

	cout << "Conversion completed, thanks" << endl;

	return EXIT_SUCCESS;
}
