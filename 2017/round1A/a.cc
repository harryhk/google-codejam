#include<iostream>
#include<queue>
#include<string>

using namespace std;


int main()
{ 
    
    int n(0), R(0), C(0);
    cin>> n;
    for( int i=0; i!= n ; i++)
    {
        cin >> R >> C ;
        
        solve( N, K, r_max, r_min);
        cout << "Case #" << i+1 << ": " 
            << r_max << " " << r_min << endl;
    }

    return 0;
}
