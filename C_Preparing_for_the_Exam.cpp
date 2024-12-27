#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

void solve() {
    int t; // Number of test cases
    cin >> t;
    while (t--) {
        int n, m, k;
        cin >> n >> m >> k;

        // Input `a` (the excluded questions for each list)
        vector<int> a(m);
        for (int i = 0; i < m; ++i) {
            cin >> a[i];
        }

        // Input `q` (questions Monocarp knows)
        unordered_set<int> known_set;
        for (int i = 0; i < k; ++i) {
            int q;
            cin >> q;
            known_set.insert(q);
        }

        // Result string for this test case
        string result = "";

        // Check each list
        for (int i = 0; i < m; ++i) {
            int excluded = a[i];
            
            // Case 1: Monocarp knows all `n` questions
            if (known_set.size() == n) {
                result += '1';
            }
            // Case 2: Monocarp knows `n - 1` questions, but the excluded question `a[i]` is NOT in the known set
            else if (known_set.size() == n - 1 && !known_set.count(excluded)) {
                result += '1';
            }
            // Otherwise, Monocarp fails for this list
            else {
                result += '0';
            }
        }

        // Output the result for this test case
        cout << result << endl;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}
