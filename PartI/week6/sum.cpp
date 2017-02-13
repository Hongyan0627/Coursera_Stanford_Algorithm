#include <fstream>
#include <iostream>
#include <unordered_map>

#define N 200
using namespace std;
unordered_map<long long int,int> umap;

int main(){
	long long int n;
	freopen("./2sum.txt","r",stdin);
	while(cin>>n){
		umap.insert(make_pair(n,1));
	}
	long int count = 0;
	for(long int i = -10000;i <= 10000; i++){
		unordered_map<long long int, int>::iterator p;
		for(p = umap.begin(); p != umap.end(); p++){
			if((umap.find(i - p->first) != umap.end()) && ((i - p->first) != p->first)){
				count++;
				break;
			}
		}
	}
	cout<<count<<endl;
	return 0;
}