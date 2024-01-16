#include "PolygonFill.hpp"

void fillPolygon(Matrix<float> *poly) {

    int nodes, nodeX[4], pixelX, pixelY, i, j, swap;

    for (pixelY = 0; pixelY < HEIGHT; pixelY++) {

        nodes = 0; j = POLY_CORNERS - 1;
        for (i = 0; i < POLY_CORNERS; i++) {
            if (poly[i](1, 2)<(double) pixelY && poly[j](1, 2)>=(double) pixelY
            ||  poly[j](1, 2)<(double) pixelY && poly[i](1, 2)>=(double) pixelY) {
            nodeX[nodes++]=(int) (poly[i](1, 1)+(pixelY-poly[i](1, 2))/(poly[j](1, 2)-poly[i](1, 2))
            *(poly[j](1, 1)-poly[i](1, 1))); }
            j=i; }

        i=0;
        while (i<nodes-1) {
            if (nodeX[i]>nodeX[i+1]) {
            swap=nodeX[i]; nodeX[i]=nodeX[i+1]; nodeX[i+1]=swap; if (i) i--; }
            else {
            i++; }}

        for (i = 0; i < nodes; i++) {

            if (nodeX[i] >= WIDTH) break;
            if (nodeX[i+1] > 0) {
                if (nodeX[i] < 0) nodeX[i] = 0;
                if (nodeX[i+1] > WIDTH) nodeX[i+1] = WIDTH;
                for (pixelX = nodeX[i]; pixelX < nodeX[i+1]; pixelX++) fillPixel(pixelX, pixelY);
            }

        }
    
    }

}

void fillPixel(int pixelX, int pixelY) {

    SDL_SetRenderDrawColor(Engine::renderer, 255, 0, 0, 255);
    SDL_RenderDrawPoint(Engine::renderer, pixelX, pixelY);

}