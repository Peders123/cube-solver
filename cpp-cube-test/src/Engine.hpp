#pragma once

#include "Cube.hpp"

#include "Eigen/Dense"
#include "SDL2/SDL.h"

#define WIDTH 640
#define HEIGHT 480
#define SCALE 100

class Cube;

class Engine {

    private:

        bool running;
        SDL_Window *window;
        Cube *cube;
        
    public:

        static SDL_Renderer *renderer;
        static SDL_Event event;
        static Eigen::Vector3d *camera;

        Engine();
        ~Engine();

        void init(const char *title, int width, int height, bool fullscreen);
        void handleEvents();
        void update();
        void render();
        void clean();

        bool isRunning() { return this->running; }
        Cube *getCube() { return this->cube; }

};