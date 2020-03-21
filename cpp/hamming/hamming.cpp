#include "hamming.h"
#include <string>
#include <stdexcept>

int hamming::compute( const std::string& strand1, const std::string& strand2 )
{
    if (strand1.length() != strand2.length())
    {
        throw std::domain_error("The input strings are of different lengths");
    };
    int total=0;
    for (int i=0; i<strand1.length(); i++)
    {
        if(strand1[i]!=strand2[i]){total++;}
    }
    return total;
}


