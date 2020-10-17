// Author: Alex Witt <awitt2399@utexas.edu>
//

#include <iostream>
#include <string>

#include "absl/strings/str_split.h"
#include "Eigen/Dense"
#include "glog/logging.h"

DEFINE_string(spring_constants, "1,1,1,1", "The spring constants.");
DEFINE_string(masses, "1,1,1,1", "The masses of the weights.");


Eigen::MatrixXd GetDifferenceMatrix(
    const int rows, const int cols, const bool diagonal)
{
    auto A = Eigen::MatrixXd(rows, cols);
    A.setZero();
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (i == j)
            {
                A(j , i) = -1.0;
            }
            else if (i - j == diagonal + 1)
            {
               A(j , i) = 1.0; 
            }
        }
    }
    return A;
}


int main(int argc, char** argv)
{
    google::InitGoogleLogging(argv[0]);


    std::vector<float> spring_constants;
    for (const auto& s : absl::StrSplit(FLAGS_spring_constants, ","))
    {
        spring_constants.push_back(std::stof(std::string(s), nullptr));
    }

    std::vector<float> masses;
    for (const auto& s : absl::StrSplit(FLAGS_masses, ","))
    {
        masses.push_back(std::stof(std::string(s), nullptr));
    }  

    auto A = GetDifferenceMatrix(
        spring_constants.size(), masses.size(), !(spring_constants.size() >= masses.size()));

    return 0;
}