#include <iostream>
using namespace std;

int main() {

	int input, rest, am, x, y;
	int vals[] = {1000, 500, 100, 50, 10, 5, 1};
	char lastChar, chars[] = {'M', 'D', 'C', 'L', 'X', 'V', 'I'};
	string str;
		
	cout << "Enter a number between 1 and 3999. Enter 0 to stop.\n";

	do {
		
		cin >> input;		
		
		if (input > 0 && input < 4000 && !cin.fail()) {
			rest = input; // create duplicate so while can keep on using input
			str  = "";
			lastChar = 0;
			
			for (x = 0; x < 7; x++) {
				
				am    = rest / vals[x];
				rest %= vals[x];
				
				if (am == 4) { // maximum is 3 of same character
					if (lastChar != '\0' && ((lastChar == 'V' && x == 6) || (lastChar == 'L' && x == 4) || (lastChar == 'D' && x == 2))) { // trying to make 9__
						str = str.substr(0, (str.length() - 1)); // remove last
						str += chars[x];
						str += chars[(x-2)];
					} else { // 4__
						str += chars[x];
						str += chars[(x-1)];
					}
					lastChar = chars[x];
				} else if (am > 0) {
					for (y = 0; y < am; y++) { // add the chars
						str += chars[x];
					}
					lastChar = chars[x]; // save last char added for next loop
				}
				
			}
			
			cout << str << "\n";
		} else if (input != 0 || cin.fail()) {
			cout << "Not a valid number.\n";
			cin.clear();
			input = 1; // prevent while from stopping
		}
		
	} while (input != 0);
	
	cout << "End of program. Press Enter to close.\n";
	cin.get();
	return 0;
}
