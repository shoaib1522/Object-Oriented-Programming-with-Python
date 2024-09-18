#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

struct BMP{
       char header[54];
       char *data;
};

BMP* fileRead(char *fileName)
{
     BMP *img = new BMP;

     ifstream b(fileName, ios::binary);
     if (!b.is_open()){
        printf("Error reading file");
        exit(EXIT_FAILURE);
     }

     b.read(img->header,54);

     int *size=reinterpret_cast<int *>(&img->header[2]);
     img->data=new char[*size];

     b.read(img->data, *size);

     b.close();

     return img;
}

void fileWrite(char *fileName, BMP *img)
{
     ofstream b(fileName, ios::binary);
     if (!b.is_open()){
        printf("Error writing file");
        exit(EXIT_FAILURE);
     }

     b.write(img->header,54);

     int *size=reinterpret_cast<int *>(&img->header[2]);

     b.write(img->data, *size);

     b.close();
}

int main(int argc, char *argv[])
{
    BMP *bmp1, *bmp2;
    bmp1 = fileRead("data.bmp");
    bmp2 = fileRead("back.bmp");

    BMP newBmp=*bmp1;
    int *size=(int *)(&bmp1->header[2]);

    newBmp.data = new char[*size];

    double w1 = 0.85;
    double w2 = 0.15;

    for (long i=0;i<*size;i++)
    {
        newBmp.data[i]=static_cast<int>((((double)bmp1->data[i]*w1)+(((double)bmp2->data[i]*w2))));
        // newBmp.data[i] = 
		//    bmp1.data[i]*w1 + bmp2.data[i]*w2
	}

    fileWrite("mixed.bmp",&newBmp);

    return EXIT_SUCCESS;
}
