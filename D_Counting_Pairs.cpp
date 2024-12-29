#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long countInterestingPairs(vector<int>& a, long long x, long long y) {
    long long totalSum = 0;
    for (int num : a) totalSum += num;

    sort(a.begin(), a.end());
    int n = a.size();
    long long count = 0;

    for (int i = 0; i < n - 1; ++i) {
        long long lowerBound = totalSum - a[i] - y;
        long long upperBound = totalSum - a[i] - x;

        // Use binary search to find the range of valid a[j] values.
        int left = upper_bound(a.begin() + i + 1, a.end(), lowerBound - 1) - a.begin();
        int right = lower_bound(a.begin() + i + 1, a.end(), upperBound + 1) - a.begin();

        count += (right - left);
    }

    return count;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        long long x, y;
        cin >> n >> x >> y;

        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }

        cout << countInterestingPairs(a, x, y) << endl;
    }

    return 0;
}
