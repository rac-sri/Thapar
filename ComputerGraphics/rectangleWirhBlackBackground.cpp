
#include<GL/glut.h>

//Program to create an empty Widdow
void init() {
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);	//Line C
	glutInitWindowSize(640, 480);
	glutInitWindowPosition(1000, 200);
	glutCreateWindow("Simple Window");
}

void display()
{
	glClearColor(0.0, 0.0, 0.0, 0.0);
	glClear(GL_COLOR_BUFFER_BIT);

	glColor3f(1.0, 0.0, 0.0);
	glRectf(0.0, 0.0, -0.6, -0.45);
	glFlush();
}

int main(int argc, char** argv)
{
	glutInit(&argc, argv);			//Line A
	init();					//Line B
	glutDisplayFunc(display);
	glutMainLoop();

	return 0;
}

