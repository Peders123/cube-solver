#pragma once

#include "Engine.hpp"
#include "Matrix.hpp"
#include "PolygonFill.hpp"

#include "Eigen/Dense"
#include "SDL2/SDL.h"

#include <vector>

#define ROTATION_MATRICES(angle) \
    Eigen::Matrix3d rotation_matrix_x; \
    rotation_matrix_x << 1, 0, 0, \
                         0, cos(angle), -sin(angle), \
                         0, sin(angle), cos(angle);  \
                         \
    Eigen::Matrix3d rotation_matrix_y; \
    rotation_matrix_y << cos(angle), 0, -sin(angle), \
                         0, 1, 0,  \
                         sin(angle), 0, cos(angle);

class Face {

    private:

        Eigen::Vector3d a;
        Eigen::Vector3d b;
        Eigen::Vector3d c;
        Eigen::Vector3d d;

        Eigen::Vector3d *corners[4];

    public:
        Face(int, int);
        ~Face();

        void update();
        void draw();
        Eigen::Vector2i getDrawingCoords(Eigen::Vector3d);

};