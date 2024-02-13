#pragma once

#include "Engine.hpp"

#include "Eigen/Dense"
#include "SDL2/SDL.h"

#include <iostream>

#define POLY_CORNERS 4

void fillPolygon(const std::vector<Eigen::Vector2i>& vertices);
void fillPixel(int, int);

