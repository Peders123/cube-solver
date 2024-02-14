#pragma once

#include "Cubie.hpp"
#include "Engine.hpp"
#include "Face.hpp"

#include "Eigen/Dense"
#include "SDL2/SDL.h"

#include <cmath>
#include <iostream>

class Face;

class Cube {

    private:

        std::vector<Face> faces;
        Cubie cubies[0];

    public:

        Cube();
        void update();
        void draw();

        static double calculateDistance(Eigen::Vector3d, Eigen::Vector3d);
        static bool compareFaces(Face, Face);

};