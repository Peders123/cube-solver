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

    /* game = new Game();
    game->init("Rubik's Cube", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 1024, 704, false);

    while (game->running()) {

        frameStart = SDL_GetTicks();

        game->handleEvents();
        game->update();
        game->render();

        frameTime = SDL_GetTicks() - frameStart;

        if (frameDelay > frameTime) {
            SDL_Delay(frameDelay - frameTime);
        }

    }

    game->clean(); */

    return 0;

}