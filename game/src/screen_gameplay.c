/**********************************************************************************************
*
*   raylib - Advance Game template
*
*   Gameplay Screen Functions Definitions (Init, Update, Draw, Unload)
*
*   Copyright (c) 2014-2022 Ramon Santamaria (@raysan5)
*
*   This software is provided "as-is", without any express or implied warranty. In no event
*   will the authors be held liable for any damages arising from the use of this software.
*
*   Permission is granted to anyone to use this software for any purpose, including commercial
*   applications, and to alter it and redistribute it freely, subject to the following restrictions:
*
*     1. The origin of this software must not be misrepresented; you must not claim that you
*     wrote the original software. If you use this software in a product, an acknowledgment
*     in the product documentation would be appreciated but is not required.
*
*     2. Altered source versions must be plainly marked as such, and must not be misrepresented
*     as being the original software.
*
*     3. This notice may not be removed or altered from any source distribution.
*
**********************************************************************************************/
#define _USE_MATH_DEFINES
#define INDIGO CLITERAL(Color){ 75, 0, 130, 255 }
#include "raylib.h"
#include "screens.h"
#include "stdlib.h"
#include "math.h"
//----------------------------------------------------------------------------------
// Module Variables Definition (local)
//----------------------------------------------------------------------------------
#define num_samples 44000;
const float Tau = 2 * M_PI;
static int framesCounter = 0;
static int finishScreen = 0;
float sample_rate = 44000.0;
float amplitude = 100.0;
float frequency = 0.0;
int current_channel = 0;
int AmpArray[] = { 0 };
int main_x_offset = 90;
float main_y_offset = 230;

typedef struct {
    int osc_number;
    int xoffset; 
    int yoffset;
    int width; 
    int height;
    Color color;
} window ;

window windows[9] = { 
    { 0,  90,  40, 870, 380, 1 }, //Big Display
    { 1,  90, 600, 100,  56, 2 }, // Display 1 ..
    { 2, 200, 600, 100,  56, 3 },
    { 3, 310, 600, 100,  56, 4 },
    { 4, 420, 600, 100,  56, 5 },
    { 5, 530, 600, 100,  56, 6 },
    { 6, 640, 600, 100,  56, 7 },
    { 7, 750, 600, 100,  56, 8 },
    { 8, 860, 600, 100,  56, 0 }, // Display 8;
};
//-------------------------------
typedef struct {
    float frequency;
    float amplitude;
} wave;

wave waves[9] = {
    {0,100},
    {1,22},
    {2,22},
    {3,22},
    {4,22},
    {5,22},
    {6,22},
    {7,22},
    {8,22},
};


// Gameplay Screen Initialization logic
void InitGameplayScreen(void) {
    //Color color_array[] = { GRAY, RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET, PINK };
    // TODO: Initialize GAMEPLAY screen variables here!
    framesCounter = 0;
    finishScreen = 0;    
}

// Gameplay Screen Update logic
void UpdateGameplayScreen(void) {
    framesCounter++;
    // TODO: Update GAMEPLAY screen variables here!
    // Press ENTER or TAP to load ENDING screen
    if (IsKeyPressed(KEY_ENTER) || IsGestureDetected(GESTURE_TAP)) {
        finishScreen = 1;
        PlaySound(fxCoin);
    }
}
//working good do not touch 3-13-2024
void draw_windows(Color color_array[9]) {
    for (int i = 0; i < 9; i++) {        
        // Draw Borders
        DrawRectangleLines (
            windows[i].xoffset, 
            windows[i].yoffset, 
            windows[i].width, 
            windows[i].height, 
            color_array[i]
        );
        // Draw 0 Center Line
        DrawLine (
            windows[i].xoffset, 
            windows[i].yoffset + windows[i].height / 2, 
            windows[i].xoffset + windows[i].width,
            windows[i].yoffset + windows[i].height / 2, 
            RAYWHITE
        ); 
    }
}

// Gameplay Screen Draw logic
void DrawGameplayScreen(void) {
    Color color_array[] = { GRAY, RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET, PINK };    
    render_title(windows[0].xoffset, windows[0].yoffset);
    draw_windows(color_array);
    update_wave_mouse();
    render_wave((int)windows[1].yoffset, color_array);
    // render_main_wave((int)windows[0].yoffset, color_array); <- CRASHING HERE
}

void render_title() {
    Vector2 titleoffset = { 100, 40 };
    const char* title = "Sin(q)uencer";
    DrawTextEx(font, title, titleoffset, font.baseSize * 3.0f, 4, BLUE);
    DrawText(TextFormat("%.2lf hz, %i samplerate, %i amplitude", frequency, (int)sample_rate, (int)amplitude), 100, 90, 20, GREEN);
}

void render_main_wave(int yoffset, Color color_array[9]) {
    for (int x = 0; x < windows[0].width; x++) {
        float time_scale = sample_rate / windows[0].width;
        float current_y = sin(Tau * frequency * x / sample_rate * time_scale) * waves[0].amplitude;
        AmpArray[x] = current_y;
        DrawLine(
            windows[0].xoffset,
            windows[0].yoffset + windows[0].height / 2,
            windows[0].xoffset + windows[0].width,
            windows[0].yoffset + windows[0].height / 2,
            windows[1].color
        );
    }
}

void render_wave(int yoffset, Color color_array[9]) {    
    for (int i = 1; i < 9; i++) {
        for (int x = 1; x < windows[i].width; x++) {
            float time_scale = sample_rate / windows[i].width;
            float current_y = sin(Tau * waves[i].frequency * x / sample_rate * time_scale) * waves[i].amplitude;
            AmpArray[x] = current_y;
            DrawLine(
                windows[i].xoffset + x - 1,
                windows[i].yoffset - AmpArray[abs((int)x - 1)] + windows[i].height / 2,
                windows[i].xoffset + x,
                windows[i].yoffset - AmpArray[abs((int)x)] + windows[i].height / 2,
                color_array[i]);
        }
    }
}

void update_wave_mouse() {
    // PRESS KEY TO INCREASE OR DECRESS (mousewheel up or down)    
    float gmw = GetMouseWheelMove();
    if (gmw == 1) {
        //if (IsKeyDown(KEY_KP_ADD)){ 
        frequency = rint((frequency + 1.0) * 1000.0) / 1000.0;
    }
    if (gmw == -1) {
        //if (IsKeyDown(KEY_KP_SUBTRACT)) {
        frequency = rint((frequency - 1.0) * 1000.0) / 1000.0;
    }
}
// Gameplay Screen Unload logic
void UnloadGameplayScreen(void)
{
    // TODO: Unload GAMEPLAY screen variables here!
}

// Gameplay Screen should finish?
int FinishGameplayScreen(void)
{
    return finishScreen;
}