
#include<iostream>
using namespace std;

void midPointCircleDraw(int x_centre, int y_centre, int r)
{
	int x = r, y = 0;

	cout << "(" << x + x_centre << ", " << y + y_centre << ") ";

	if (r > 0)
	{
		cout << "(" << x + x_centre << ", " << -y + y_centre << ") ";
		cout << "(" << y + x_centre << ", " << x + y_centre << ") ";
		cout << "(" << -y + x_centre << ", " << x + y_centre << ")\n";
	}

	int P = 1 - r;
	while (x > y)
	{
		y++;

	
		if (P <= 0)
			P = P + 2 * y + 1;

		else
		{
			x--;
			P = P + 2 * y - 2 * x + 1;
		}

		
		if (x < y)
			break;


		cout << "(" << x + x_centre << ", " << y + y_centre << ") ";
		cout << "(" << -x + x_centre << ", " << y + y_centre << ") ";
		cout << "(" << x + x_centre << ", " << -y + y_centre << ") ";
		cout << "(" << -x + x_centre << ", " << -y + y_centre << ")\n";

		if (x != y)
		{
			cout << "(" << y + x_centre << ", " << x + y_centre << ") ";
			cout << "(" << -y + x_centre << ", " << x + y_centre << ") ";
			cout << "(" << y + x_centre << ", " << -x + y_centre << ") ";
			cout << "(" << -y + x_centre << ", " << -x + y_centre << ")\n";
		}
	}
}

int main()
{
	midPointCircleDraw(0, 0, 3);
	return 0;
}
