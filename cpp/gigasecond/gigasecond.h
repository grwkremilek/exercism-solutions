#ifndef _gigasecond_h
#define _gigasecond_h

#include <boost/date_time/gregorian/gregorian.hpp>

namespace gigasecond {
  boost::gregorian::date advance(boost::gregorian::date d);
} /* gigasecond */

#endif