#include<bits/stdc++.h>
using namespace std ;
int main(){

int t;
cin>>t;
while(t--){
    int n,m,k;
    cin>>n>>m>>k;
    if(m==k){
        cout<<"1111"<<endl;
        continue;
    }
    vector<int>v(m);
    for(int i=0;i<m;i++){
        cin>>v[i];
    }
    set<int>st;
    for(int i=0;i<k;i++){
        int x;
        cin>>x;
        st.insert(x);
    }
    string res="";
    for(int i=0;i<n;i++){
        if(st.find(v[i])!=st.end()){
            res+="0";
        }
        else{
            res+="1";
        }
    }
    cout<<res<<endl;

}
return 0 ;
}