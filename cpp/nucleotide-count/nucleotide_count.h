#if !defined(NUCLEOTIDE_COUNT_H)
#define NUCLEOTIDE_COUNT_H

#include <string>
#include <map>

namespace dna
{
    class counter
    {
    public:
        std::string strand;
        counter(std::string);
        int count(char) const;
        std::map<char, int> nucleotide_counts() const;
    };
}
#endif
