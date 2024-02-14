#include "Cube.hpp"

Cube::Cube() {

    this->faces.push_back(Face(0, 1, YELLOW));
    this->faces.push_back(Face(0, -1, WHITE));
    this->faces.push_back(Face(1, 1, RED));
    this->faces.push_back(Face(1, -1, ORANGE));
    this->faces.push_back(Face(2, 1, GREEN));
    this->faces.push_back(Face(2, -1, BLUE));

}

void Cube::update() {

    for (int i = 0; i < this->faces.size(); i++) {
        this->faces[i].update();
    }

}

void Cube::draw() {

    std::sort(this->faces.begin(), this->faces.end(), compareFaces);

    for (int i = 0; i < this->faces.size() / 2; i++) {

        this->faces[i].draw();

    }

}

double Cube::calculateDistance(Eigen::Vector3d v, Eigen::Vector3d w) {

    double total;

    double x = v(0, 0) - w(0, 0);
    double y = v(1, 0) - w(1, 0);
    double z = v(2, 0) - w(2, 0);

    total = (x * x) + (y * y) + (z * z);

    return sqrt(total);

}

bool Cube::compareFaces(Face face1, Face face2) {

    return Cube::calculateDistance(*Engine::camera, face1.getCentre()) >
           Cube::calculateDistance(*Engine::camera, face2.getCentre());

}