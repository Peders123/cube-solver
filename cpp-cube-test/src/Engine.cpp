#include "Engine.hpp"

SDL_Renderer *Engine::renderer = nullptr;
SDL_Event Engine::event;
Eigen::Vector3d *Engine::camera = nullptr;

Engine::Engine() {

    this->cube = new Cube();

}

void Engine::init(const char *title, int width, int height, bool fullscreen) {

    int flags = 0;

    if (fullscreen) {

        flags = SDL_WINDOW_FULLSCREEN;

    }

    if (SDL_Init(SDL_INIT_EVERYTHING) == 0) {
        std::cout << "Subsystems Initialised!..." << std::endl;

        window = SDL_CreateWindow(title, SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, width, height, flags);
        if (window) {
            std::cout << "Window created!" << std::endl;
        }

        renderer = SDL_CreateRenderer(window, -1, 0);
        if (renderer) {
            SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
            std::cout << "Renderer created!" << std::endl;
        }

        camera = new Eigen::Vector3d;
        if (camera) {
            *camera << 0, 0, -10;
            std::cout << "Camera initialised!" << std::endl;
        }

        this->running = true;

    }

}

void Engine::handleEvents() {

    SDL_PollEvent(&event);

    switch (event.type) {
        case SDL_QUIT:
            this->running = false;
            break;
        default:
            break;
    }

}

void Engine::update() {

    this->cube->update();

}

void Engine::render() {

    SDL_RenderClear(renderer);
    this->cube->draw();
    SDL_RenderPresent(renderer);

}

void Engine::clean() {

    SDL_DestroyWindow(window);
    SDL_DestroyRenderer(renderer);
    SDL_Quit();

}