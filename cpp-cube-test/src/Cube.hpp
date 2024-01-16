#pragma once

#include "Cubie.hpp"
#include "Engine.hpp"
#include "Face.hpp"
#include "Matrix.hpp"

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
        // static Matrix<float> getDrawingCoords(Matrix<float>);

};