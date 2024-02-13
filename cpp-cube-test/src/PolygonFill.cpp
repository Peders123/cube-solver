#include "PolygonFill.hpp"

// Edge struct to represent an edge of the polygon
struct Edge {
    int startY; // Starting y-coordinate of the edge
    int endY;   // Ending y-coordinate of the edge
    float startX; // Starting x-coordinate of the edge
    float slopeInverse; // Inverse slope of the edge

    Edge(int startY, int endY, float startX, float slopeInverse)
        : startY(startY), endY(endY), startX(startX), slopeInverse(slopeInverse) {}
};

// Function to fill the pixels inside the polygon
void fillPolygon(const std::vector<Eigen::Vector2i>& vertices) {
    int minY = INT_MAX;
    int maxY = INT_MIN;

    // Find the minimum and maximum y-coordinates
    for (const auto& vertex : vertices) {
        minY = std::min(minY, vertex.y());
        maxY = std::max(maxY, vertex.y());
    }

    // Initialize a vector to store edges
    std::vector<Edge> edges;

    // Create edges from the vertices
    for (size_t i = 0; i < vertices.size(); ++i) {
        // Get the current and next vertex
        Eigen::Vector2i current = vertices[i];
        Eigen::Vector2i next = vertices[(i + 1) % vertices.size()];

        // If the edge is not horizontal
        if (current.y() != next.y()) {
            // Ensure current.y() < next.y()
            if (current.y() > next.y())
                std::swap(current, next);

            // Calculate inverse slope of the edge
            float slopeInverse = static_cast<float>(next.x() - current.x()) / (next.y() - current.y());

            // Add the edge to the edges vector
            edges.emplace_back(current.y(), next.y(), current.x(), slopeInverse);
        }
    }

    // Scanline algorithm to fill the polygon
    for (int y = minY; y < maxY; ++y) {
        std::vector<float> intersections;

        // Find intersections of scanline with edges
        for (const auto& edge : edges) {
            if (y >= edge.startY && y < edge.endY) {
                float xIntersect = edge.startX + edge.slopeInverse * (y - edge.startY);
                intersections.push_back(xIntersect);
            }
        }

        // Sort intersections from left to right
        std::sort(intersections.begin(), intersections.end());

        // Fill pixels between intersections
        for (size_t i = 0; i < intersections.size(); i += 2) {
            int startX = static_cast<int>(intersections[i]);
            int endX = static_cast<int>(intersections[i + 1]);

            for (int x = startX; x < endX; ++x) {
                fillPixel(x, y);
            }
        }
    }
}

void fillPixel(int pixelX, int pixelY) {

    SDL_SetRenderDrawColor(Engine::renderer, 255, 0, 0, 255);
    SDL_RenderDrawPoint(Engine::renderer, pixelX, pixelY);

}