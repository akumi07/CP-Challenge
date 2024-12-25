#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        long long n, a, b, c;
        cin >> n >> a >> b >> c;

        long long sum_of_cycle = a + b + c;
        long long full_cycles = n / sum_of_cycle;
        long long distance_covered = full_cycles * sum_of_cycle;
        long long remaining_distance = n - distance_covered;

        int day = 1;

        // Simulate the remaining days in the current cycle
        if (remaining_distance > 0) {
            remaining_distance -= a;
            if (remaining_distance > 0) {
                day++;
                remaining_distance -= b;
            }
            if (remaining_distance > 0) {
                day++;
                remaining_distance -= c;
            }
        }

        // Total days = (full cycles * 3) + remaining days
        cout << (full_cycles * 3 + day) << endl;
    }

    return 0;
}
