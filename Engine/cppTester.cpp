// C++ remake of python test script
#include  "sdlWrapper.cpp"

//SDL required for special pointer types
#if _WIN32 || _WIN64
    #include "SDL2\SDL.h"
    #include "SDL2\SDL_image.h"
    #include "SDL2\SDL_ttf.h"
#else
    #include <SDL2/SDL.h>
    #include <SDL2/SDL_timer.h>
    #include <SDL2/SDL_image.h>
    #include <SDL2/SDL_ttf.h>
#endif

int main(int argv,char **argc){
    int loaded = start_engine("Crumbl Engine test program",1366,768);

    int r = 0;
    int g = 0;
    int b = 0;
    int colorchange = 0;

    bool running = true;

    while(running){
        if(r != 255 && colorchange == 0){
            b -= 1;
            r += 1;
        }
        if(r == 255){
            colorchange += 1;
        }
        if(g != 255 && colorchange == 1){
            r -= 1;
            g += 1;
        }
        if(g == 255){
            colorchange += 1;
        }
        if(b != 255 && colorchange == 2){
            g -= 1;
            b += 1;
        }
        if(b == 255){
            colorchange = 0;
        }
        changeBGColor(r,g,b,255);
        updateCrumblTasks(window,winSurface,true,true,60);
    }
}