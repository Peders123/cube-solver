#include "Face.hpp"


Face::Face(int axis, int magnitude) {

    this->a(axis, 0) = magnitude;
    this->b(axis, 0) = magnitude;
    this->c(axis, 0) = magnitude;
    this->d(axis, 0) = magnitude;

    this->corners[0] = &this->a;
    this->corners[1] = &this->b;
    this->corners[2] = &this->d;
    this->corners[3] = &this->c;

    std::vector<int> rows;

    switch (axis) {
        case 0:
            rows.push_back(1);
            rows.push_back(2);
            break;
        case 1:
            rows.push_back(0);
            rows.push_back(2);
            break;
        case 2:
            rows.push_back(0);
            rows.push_back(1);
            break;
        default:
            break;
    }

    this->a(rows[0], 0) = -1;
    this->a(rows[1], 0) = 1;

    this->b(rows[0], 0) = 1;
    this->b(rows[1], 0) = 1;

    this->c(rows[0], 0) = -1;
    this->c(rows[1], 0) = -1;

    this->d(rows[0], 0) = 1;
    this->d(rows[1], 0) = -1;

    std::cout << this->a << "\n" << std::endl;
    std::cout << this->b << "\n" << std::endl;
    std::cout << this->c << "\n" << std::endl;
    std::cout << this->d << "\n" << std::endl;

}

Face::~Face() {}

void Face::update() {

    double angle = 0.05;

    ROTATION_MATRICES(angle)

    this->a = rotation_matrix_x * this->a;
    this->a = rotation_matrix_y * this->a;

    this->b = rotation_matrix_x * this->b;
    this->b = rotation_matrix_y * this->b;

    this->c = rotation_matrix_x * this->c;
    this->c = rotation_matrix_y * this->c;

    this->d = rotation_matrix_x * this->d;
    this->d = rotation_matrix_y * this->d;

}

void Face::draw() {

    std::vector<Eigen::Vector2i> vertices;

    vertices.push_back(Face::getDrawingCoords(this->a));
    vertices.push_back(Face::getDrawingCoords(this->b));
    vertices.push_back(Face::getDrawingCoords(this->d));
    vertices.push_back(Face::getDrawingCoords(this->c));

    fillPolygon(vertices);

    SDL_SetRenderDrawColor(Engine::renderer, 0, 0, 0, 255);

    SDL_RenderDrawLine(Engine::renderer, vertices[0](0, 0), vertices[0](1, 0), vertices[1](0, 0), vertices[1](1, 0));
    SDL_RenderDrawLine(Engine::renderer, vertices[1](0, 0), vertices[1](1, 0), vertices[2](0, 0), vertices[2](1, 0));
    SDL_RenderDrawLine(Engine::renderer, vertices[0](0, 0), vertices[0](1, 0), vertices[3](0, 0), vertices[3](1, 0));
    SDL_RenderDrawLine(Engine::renderer, vertices[3](0, 0), vertices[3](1, 0), vertices[2](0, 0), vertices[2](1, 0));

    SDL_SetRenderDrawColor(Engine::renderer, 255, 255, 255, 255);

}

Eigen::Vector2i Face::getDrawingCoords(Eigen::Vector3d v) {

    Eigen::Matrix<double, 2, 3> projection_matrix {
        {1, 0, 0},
        {0, 1, 0},
    };

    Eigen::Vector2d projected_coords = projection_matrix * v;
    Eigen::Vector2i coords;

    coords(0, 0) = (int)((projected_coords(0, 0) * SCALE) + WIDTH / 2);
    coords(1, 0) = (int)((projected_coords(1, 0) * SCALE) + HEIGHT / 2);

    return coords;

}