#include <iostream>
#include <sstream>
#include <numeric>

using namespace std;

int main(int argc, char** argv) {
    int n = 3;
    if (argc != 1) {
        stringstream input(argv[1]);
        input >> n;
    }

    int s = 0;
    for (int x = 1; x <= n; x++) {
        for (int y = x + 1; y <= n; y++) {
            s += gcd(x, y);
        }
    }

    cout << s << endl;
}