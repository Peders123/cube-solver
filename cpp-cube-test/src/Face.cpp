#include "Face.hpp"


Face::Face(int axis, int magnitude) {

    this->a.setElem(axis, 1, magnitude);
    this->b.setElem(axis, 1, magnitude);
    this->c.setElem(axis, 1, magnitude);
    this->d.setElem(axis, 1, magnitude);

    this->corners[0] = &this->a;
    this->corners[1] = &this->b;
    this->corners[2] = &this->d;
    this->corners[3] = &this->c;

    std::vector<int> rows;

    switch (axis) {
        case 1:
            rows.push_back(2);
            rows.push_back(3);
            break;
        case 2:
            rows.push_back(1);
            rows.push_back(3);
            break;
        case 3:
            rows.push_back(1);
            rows.push_back(2);
            break;
        default:
            break;
    }

    this->a.setElem(rows[0], 1, -1);
    this->a.setElem(rows[1], 1, 1);

    this->b.setElem(rows[0], 1, 1);
    this->b.setElem(rows[1], 1, 1);

    this->c.setElem(rows[0], 1, -1);
    this->c.setElem(rows[1], 1, -1);

    this->d.setElem(rows[0], 1, 1);
    this->d.setElem(rows[1], 1, -1);
}

Face::~Face() {}

void Face::update() {

    float angle = 0.05;

    Matrix<float> rotation_x(3, 3);
    Matrix<float> rotation_y(3, 3);

    rotation_x.setElem(1, 1, 1);
    rotation_x.setElem(1, 2, 0);
    rotation_x.setElem(1, 3, 0);
    rotation_x.setElem(2, 1, 0);
    rotation_x.setElem(2, 2, cos(angle));
    rotation_x.setElem(2, 3, -sin(angle));
    rotation_x.setElem(3, 1, 0);
    rotation_x.setElem(3, 2, sin(angle));
    rotation_x.setElem(3, 3, cos(angle));

    rotation_y.setElem(1, 1, cos(-angle));
    rotation_y.setElem(1, 2, 0);
    rotation_y.setElem(1, 3, sin(-angle));
    rotation_y.setElem(2, 1, 0);
    rotation_y.setElem(2, 2, 1);
    rotation_y.setElem(2, 3, 0);
    rotation_y.setElem(3, 1, -sin(-angle));
    rotation_y.setElem(3, 2, 0);
    rotation_y.setElem(3, 3, cos(-angle));

    this->a = rotation_x * this->a;
    this->a = rotation_y * this->a;
    this->b = rotation_x * this->b;
    this->b = rotation_y * this->b;
    this->c = rotation_x * this->c;
    this->c = rotation_y * this->c;
    this->d = rotation_x * this->d;
    this->d = rotation_y * this->d;

}

void Face::draw() {

    std::vector<Matrix<float>> drawing_coordinates;

    drawing_coordinates.push_back(Face::getDrawingCoords(this->a));
    drawing_coordinates.push_back(Face::getDrawingCoords(this->b));
    drawing_coordinates.push_back(Face::getDrawingCoords(this->c));
    drawing_coordinates.push_back(Face::getDrawingCoords(this->d));

    Matrix<float> poly[4];

    poly[0] = drawing_coordinates[0];
    poly[1] = drawing_coordinates[1];
    poly[2] = drawing_coordinates[3];
    poly[3] = drawing_coordinates[2];

    fillPolygon(poly);

    SDL_SetRenderDrawColor(Engine::renderer, 0, 0, 0, 255);
    SDL_RenderDrawLine(Engine::renderer, drawing_coordinates[0](1, 1), drawing_coordinates[0](1, 2), drawing_coordinates[1](1, 1), drawing_coordinates[1](1, 2));
    SDL_RenderDrawLine(Engine::renderer, drawing_coordinates[1](1, 1), drawing_coordinates[1](1, 2), drawing_coordinates[3](1, 1), drawing_coordinates[3](1, 2));
    SDL_RenderDrawLine(Engine::renderer, drawing_coordinates[0](1, 1), drawing_coordinates[0](1, 2), drawing_coordinates[2](1, 1), drawing_coordinates[2](1, 2));
    SDL_RenderDrawLine(Engine::renderer, drawing_coordinates[2](1, 1), drawing_coordinates[2](1, 2), drawing_coordinates[3](1, 1), drawing_coordinates[3](1, 2));
    SDL_SetRenderDrawColor(Engine::renderer, 255, 255, 255, 255);

}

Matrix<float> Face::getDrawingCoords(Matrix<float> m) {

    Matrix<float> projection_matrix(2, 3);

    projection_matrix.setElem(1, 1, 1);
    projection_matrix.setElem(2, 2, 1);

    Matrix<float> projected_coords = projection_matrix * m;

    Matrix<float> coords(1, 2);

    coords.setElem(1, 1, (int)((projected_coords(1, 1) * SCALE) + WIDTH / 2));
    coords.setElem(1, 2, (int)((projected_coords(2, 1) * SCALE) + HEIGHT / 2));

    return coords;

}