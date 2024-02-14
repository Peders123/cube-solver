#pragma once

#include "Engine.hpp"
#include "PolygonFill.hpp"

#include "Eigen/Dense"
#include "SDL2/SDL.h"

#include <cmath>
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

typedef struct Colour{
    uint8_t red = 0;
    uint8_t green = 0;
    uint8_t blue = 0;
} COLOUR;

#define RED COLOUR{255, 0, 0}
#define GREEN COLOUR{0, 255, 0}
#define BLUE COLOUR{0, 0, 255}
#define WHITE COLOUR{255, 255, 255}
#define YELLOW COLOUR{255, 255, 0}
#define ORANGE COLOUR{255, 165, 0}

class Face {

    private:

        Eigen::Vector3d a;
        Eigen::Vector3d b;
        Eigen::Vector3d c;
        Eigen::Vector3d d;

        Eigen::Vector3d *corners[4];

        COLOUR colour;

    public:
        Face(int, int);
        Face(int, int, COLOUR);
        ~Face();

        void update();
        void draw();
        Eigen::Vector2i getDrawingCoords(Eigen::Vector3d);
        Eigen::Vector3d getCentre();

};