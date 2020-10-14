// Author: Alex Witt <awitt2399@utexas.edu>
//

#include <Egien
#include "glog/logging.h"

DEFINE_int32(num_masses, 3, "Number of masses in the system.");
DEFINE_int32(num_springs, 4, "Number of springs in the system.");
DEFINE_string(spring_constants, "1,1,1,1", "The spring constants.");
DEFINE_string(masses, "1,1,1,1", "The masses of the weights.");


std::vector<std::vector<float>> 


int main(int argc, char** argv)
{

    google::InitGoogleLogging(argv[0]);
    return 0;
}