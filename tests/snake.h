#ifndef SNAKE_H
#define SNAKE_H

#define WIDTH 60
#define HIGH 20

typedef struct BODY
{
	int x;
	int y;
}BODY;

typedef struct SNAKE
{
	BODY body[100];
	int size;
}SNAKE;

typedef struct FOOD
{
	int x;
	int y;
}FOOD;

extern SNAKE snake;
extern FOOD food;
extern x;
extern y;
extern kx;
extern ky;

void init_snake();
void init_food();
void DrawSnake();
void putchar_food();
void final_concul();
void PlayGame();
#endif















