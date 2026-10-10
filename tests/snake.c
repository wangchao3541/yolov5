#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<windows.h>
#include<conio.h>
#include"snake.h"

SNAKE snake;
FOOD food;
COORD coord;
int kx = 1;
int ky = 0;
int length;

int main()
{
	srand(time(NULL));
	init_snake();
	init_food();
	DrawSnake();	//画
	putchar_food();		//画食物
	PlayGame();			//开始游戏
	
	final_concul();
	int score = 0;

	return 0;
}
void init_snake()
{
	snake.size = 2;

	snake.body[0].x = WIDTH /2;
	snake.body[0].y = HIGH /2;

	snake.body[1].x = WIDTH /2 - 1;
	snake.body[1].y = HIGH /2;
}

void init_food()
{
	food.x = rand() % WIDTH;
	food.y = rand() % HIGH;
}

void DrawSnake()
{
	for (int i = 0; i < snake.size; i++)
	{
		coord.X = snake.body[i].x;
		coord.Y = snake.body[i].y;
		SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
		if (i == 0)
		{
			printf("@"); //蛇头
		}
		else
		{
			printf("#"); //身体
		}
	}
}
void putchar_food()
{
	coord.X = food.x;
	coord.Y = food.y;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
	printf("$");

}

void final_concul()
{
	coord.X = 0;
	coord.Y = HIGH + 2;
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
	printf(" ");
}

//碰撞    1，失败         1，头和墙碰撞  2，头和身体盆装
//        2，长度加1      1，头和食物碰撞
void PlayGame()
{
	
	char key = 'd';
	while (snake.body[0].x >= 0 && snake.body[0].x < WIDTH
		&& snake.body[0].y >= 0 && snake.body[0].y < HIGH)
		   
	{
		for (int j = 1;j < snake.size;j++) {
			if (snake.body[0].x == snake.body[j].x
				&&
				snake.body[0].y == snake.body[j].y)
				return 0;
		}

		if (_kbhit()) {
			key = _getch();

			switch (key) {
			case 'w': kx = 0;  ky = -1; break;  // 上：Y-1
			case 's': kx = 0;  ky = 1;  break;  // 下：Y+1
			case 'a': kx = -1; ky = 0;  break;  // 左：X-1
			case 'd': kx = 1;  ky = 0;  break;  // 右：X+1
			}
		}
		if (snake.body[0].x == food.x && snake.body[0].y == food.y)
		{
			init_food();
			putchar_food();
			snake.size++;
			coord.X = snake.body[snake.size - 1].x;
			coord.Y = snake.body[snake.size - 1].y;
			SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
			printf("#");
		}
		
	    for (int i = snake.size - 1;i > 0;i--)
		{
			snake.body[i].x = snake.body[i - 1].x;
			snake.body[i].y = snake.body[i - 1].y;
		}
		
		snake.body[0].x += kx;
		snake.body[0].y += ky;

		system("cls");
		DrawSnake();
		putchar_food();

		Sleep(80);
	}
	
	return 0;
}