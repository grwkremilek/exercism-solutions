#include "nucleotide_count.h"

namespace dna
{
    counter::counter(std::string s) : strand(s)
    {
        for (auto c : strand) 
        {
            if (c != 'A' && c != 'T' && c != 'C' && c != 'G') 
            {
                throw std::invalid_argument("invalid input");
            }
        }
    }
    
    std::map<char, int> counter::nucleotide_counts() const
    {
        std::map<char, int> results = { {'G', 0}, {'C', 0}, {'T', 0}, {'A', 0} };
        for (const char &n : strand) results[n]++;
        return results;
    }
    
    int counter::count(char base) const
    {
        int sum = 0;
        for (const char &n : strand) if (n==base) sum++;
        return sum;
    }
}

