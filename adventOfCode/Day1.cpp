#include "Util.h"

using namespace std;

int main()
{
	//DAY 1: 
	std::vector<unsigned char> buffer;
	if (utility::readFileToBuffer("Day1.txt", buffer)) {
		int total = 0;
		int size = buffer.size();
		int shift = size / 2; // shift = 1 for the first assignment


		for (int i = 0; i<size; i++)
		{
			if ((int)buffer[i] == (int)buffer[(i + shift) % size]) {
				total = total + (buffer[i] - '0');
			}
		}

		cout << total << endl;
		return 0;
	}
	else {
		return 1;
	}

}

