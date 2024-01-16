#pragma once

#include "Engine.hpp"
#include "Matrix.hpp"
#include "PolygonFill.hpp"

#include "SDL2/SDL.h"

#include <vector>


class Face {

    private:
        Matrix<float> a = Matrix<float>(3, 1);
        Matrix<float> b = Matrix<float>(3, 1);
        Matrix<float> c = Matrix<float>(3, 1);
        Matrix<float> d = Matrix<float>(3, 1);

        Matrix<float> *corners[4];

    public:
        Face(int, int);
        ~Face();

        void update();
        void draw();
        Matrix<float> getDrawingCoords(Matrix<float>);

};