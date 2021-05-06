#include<GL/glut.h>
#include<math.h>
void display() {
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(0.8, 0.6, 0.4);
	//car boundary
	glBegin(GL_POLYGON);
	glVertex2f(100, 100);
	glVertex2f(450, 100);
	glVertex2f(450, 160);
	glVertex2f(400, 200);
	glVertex2f(200, 200);
	glVertex2f(150, 160);
	glVertex2f(100, 150);
	glEnd();
	//wheel 1
	glBegin(GL_POLYGON);
	glColor3f(0.0, 0.0, 0.0);
	int x1 = 200, y = 100, r = 25;
	for (int i = 0; i < 360; i++) {
		float th = i * 3.142 / 180;
		glVertex2f(x1 + r * cos(th), y + r * sin(th));
	}
	glEnd();
	//wheel 2
	glBegin(GL_POLYGON);
	glColor3f(0.0, 0.0, 0.0);
	int x2 = 380;
	for (int i = 0; i < 360; i++) {
		float th = i * 3.142 / 180;
		glVertex2f(x2 + r * cos(th), y + r * sin(th));
	}
	glEnd();
	glFlush();
}
void myinit() {
	glClearColor(1.0, 1.0, 1.0, 1.0);
	//glColor3f(1.0, 0.0, 0.0);
	glPointSize(5.0);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0.0, 499.0, 0.0, 499.0);
}
int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(0, 0);
	glutCreateWindow("Points");
	glutDisplayFunc(display);
	myinit();
	glutMainLoop();
}



