#include "Cube.hpp"

Cube::Cube() {

    this->faces.push_back(Face(1, -1));
    //this->faces.push_back(Face(1, 1));
    this->faces.push_back(Face(2, -1));
    //this->faces.push_back(Face(2, 1));
    this->faces.push_back(Face(3, -1));
    //this->faces.push_back(Face(3, 1));

}

void Cube::update() {

    for (int i = 0; i < this->faces.size(); i++) {
        this->faces[i].update();
    }

}

void Cube::draw() {

    for (int i = 0; i < this->faces.size(); i++) {
        this->faces[i].draw();
    }

}