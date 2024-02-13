#include "Eigen/Dense"
#include "SDL2/SDL.h"
#include "Engine.hpp"
#include "Cube.hpp"
#include <iostream>

Engine *engine = nullptr;

int main(int argc, char *argv[]) {

    const int FPS = 30;
    const int frameDelay = 1000 / FPS;

    Uint32 frameStart;
    int frameTime;

    engine = new Engine();
    engine->init("Rubik's Cube", WIDTH, HEIGHT, false);

    while (engine->isRunning()) {

        frameStart = SDL_GetTicks();

        engine->handleEvents();
        engine->update();
        engine->render();

        frameTime = SDL_GetTicks() - frameStart;

        if (frameDelay > frameTime) {
            SDL_Delay(frameDelay - frameTime);
        }

    }

    return 0;

}