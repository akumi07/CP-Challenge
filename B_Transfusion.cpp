#include <bits/stdc++.h>
using namespace std;

int main() {
    int t; // Number of test cases
    cin >> t;
    while (t--) {
        int n; 
        cin >> n; // Size of the array
        vector<int> a(n);
        for (int &x : a) cin >> x;

        long long ods = 0, evs = 0;
        for (int i = 0; i < n; i++) {
            if (i & 1) // Odd index
                ods += a[i];
            else       // Even index
                evs += a[i];
        }

        int odc = n / 2;     // Odd index count
        int evc = n / 2;     // Even index count
        if (n & 1) evc++;    // If `n` is odd, one more element in even indices

        // Checking conditions
        if (ods % odc != 0 || evs % evc != 0 || ods / odc != evs / evc) {
            cout << "NO" << endl;
        } else {
            cout << "YES" << endl;
        }
    }
    return 0;
}
