#include "gigasecond.h"

namespace gigasecond {
  boost::gregorian::date advance(boost::gregorian::date d)
  {
    boost::gregorian::date_duration days((1000000000 / (60 * 60 * 24)));
    return d + days;
  }
} /* gigasecond */
