#include<bits/stdc++.h>
using namespace std ;
int main(){

int t;
cin>>t;
while(t--){
    int n,k;
    cin>>n>>k;
    vector<int>a(n);
    vector<int>b(n);
    int minb=INT_MAX;
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    for(int i=0;i<n;i++){
        cin>>b[i];
        
    }
    sort(a.begin(),a.end());
    sort(b.begin(),b.end());
    for(int i=0;i<n;i++){
        int ub=upper_bound(b.begin(),b.end(),b[i])-b.begin();
        cout<<"upper_bound: "<<b[i]<<" :- "<<ub<<endl;
        int lb=lower_bound(a.begin(),a.end(),b[i])-a.begin();
        cout<<"lower_bound: "<<lb<<endl;
    }
}
return 0 ;
}