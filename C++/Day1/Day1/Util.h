#pragma once
#include <iostream>
#include <fstream>
#include <vector>

namespace utility
{
	bool readFileToBuffer(std::string filePath, std::vector<unsigned char>& buffer);
}
