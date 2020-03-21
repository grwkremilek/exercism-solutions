#include "bob.h"
#include <regex>

std::string bob::hey(const std::string &input)
{    
    std::regex question("\\?\\W*$");
    std::regex shouting("^[^a-z]+[A-Z][^a-z]+$");
    std::regex blabol("^\\W*$");

    if ( regex_search(input, question) )
    {
        return "Sure.";
    }
    
    else if (regex_search(input, shouting))
    {
        return "Whoa, chill out!";
    }
    
    else if (regex_search(input, blabol))
    {
        return "Fine. Be that way!";
    }    

    return "Whatever.";
}
