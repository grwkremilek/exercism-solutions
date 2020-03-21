#include "sieve.h"
#include <vector>
#include <math.h>

std::vector<int> sieve::primes(int max_num)
{    
    if (max_num == 0 or max_num == 1) 
    {
        return {};
    }
    std::vector<bool> candidates(max_num + 1, true);
    
    for(int i = 2; i < sqrt(max_num)+1; i++) 
    {
        if (candidates[i] == true)
        {
            for(int j = i * i; j < max_num + 1; j+= i)
            {
                candidates[j] = false;
            }
        }
    }
    std::vector<int> primes;
    for (int i = 2; i <= max_num; i++)
    {
        if (candidates[i]) 
        {
            primes.push_back(i);
        }
    }
    return primes;
}
