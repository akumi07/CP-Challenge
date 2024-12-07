#include<bits/stdc++.h>
using namespace std ;
int main(){

int t;
cin>>t;
while(t--){
    int n,m;

    cin>>n>>m;

    vector<string>v(n);
    for(int i=0;i<n;i++){
        cin>>v[i];
        // cout<<v[i]<<endl;
    }
    int ans=0;
    // cout<<"value of m :"<<m<<endl;
    for(int i=0;i<n;i++){
        if(m>=v[i].size()){
            ans++;
            m-=v[i].size();
            // cout<<"Updated value of m at "<<i<<" "<<m;
        }
        else{
            break;
        }
    }
    cout<<ans<<endl;;


}
return 0 ;
}