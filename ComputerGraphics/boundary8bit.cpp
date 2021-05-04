#include <iostream>
#include <math.h>
#include <GL/glut.h>
using namespace std;
float boundaryColor[] = { 1,0,0 };
float fillColor[] = { 0,0,1 };		
void draw_poly() {
	glLineWidth(2);
	glPointSize(1);
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3fv(boundaryColor);	
	glBegin(GL_LINE_LOOP);
	glVertex2i(30, 30);
	glVertex2i(90, 30);
	glVertex2i(90, 45);
	glVertex2i(30, 45);
	glEnd();
	glFlush();
}

void boundary_fill8(int x, int y, float* fillColor, float* boundaryColor) {
	float color[3];
	glReadPixels(x, y, 1.0, 1.0, GL_RGB, GL_FLOAT, color);

	if ((color[0] != boundaryColor[0] || color[1] != boundaryColor[1] || color[2] != boundaryColor[2]) && (
		color[0] != fillColor[0] || color[1] != fillColor[1] || color[2] != fillColor[2])) {
		glColor3f(fillColor[0], fillColor[1], fillColor[2]);
		glBegin(GL_POINTS);
		glVertex2i(x, y);
		glEnd();
		glFlush();
		
		boundary_fill8(x + 1, y, fillColor, boundaryColor);
		boundary_fill8(x - 1, y, fillColor, boundaryColor);
		boundary_fill8(x, y + 1, fillColor, boundaryColor);
		boundary_fill8(x, y - 1, fillColor, boundaryColor);
		
		boundary_fill8(x - 1, y + 1, fillColor, boundaryColor);
		boundary_fill8(x + 1, y + 1, fillColor, boundaryColor);
		boundary_fill8(x - 1, y - 1, fillColor, boundaryColor);
		boundary_fill8(x + 1, y - 1, fillColor, boundaryColor);
	}
}
void init() {

	glClearColor(1.0, 1.0, 1.0, 0.0);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0, 600, 0, 500);
}
void mouse(int btn, int state, int x, int y) {
	y = 500 - y;
	if (btn == GLUT_LEFT_BUTTON)
	{
		if (state == GLUT_DOWN)
		{
			
			boundary_fill8(x, y, fillColor, boundaryColor);
		}
	}
}
int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(600, 500);
	glutInitWindowPosition(200, 200);
	glutCreateWindow("Boundary Fill 8 connected");
	glutDisplayFunc(draw_poly);
	glutMouseFunc(mouse);
	init();
	glutMainLoop();
	return 0;
}

