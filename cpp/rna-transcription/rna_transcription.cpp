#include "rna_transcription.h"
#include <map>


namespace transcription
{
    std::map<char,char> dictionary =
        {
            {'G', 'C'}, {'C', 'G'}, {'T', 'A'}, {'A', 'U'}
        };

    char to_rna(char c)
        {
            return dictionary[c];
        }

    std::string to_rna(std::string s)
        {
            for (char &c : s) c = dictionary[c];
            return s;
        }
}
