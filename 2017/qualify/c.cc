#include<iostream>
#include<queue>
#include<string>

using namespace std;

void solve( int N, int K, int & r_max, int & r_min)
{
    priority_queue<int> queue;
    queue.push( N );

    while( !queue.empty() && K > 0 )
    {
        int space = queue.top();
        space --;
        int a = space /2;
        int b = space -a;

        queue.pop();
        queue.push(a);
        queue.push(b);
        K--;

        if( K==0)
        {
            r_max = a>b? a: b; 
            r_min = a>b? b: a; 
        }

    }
}

int main()
{ 
    
    int n(0), N(0), K(0);
    cin>> n;
    for( int i=0; i!= n ; i++)
    {
        cin >> N >> K;
        int r_max(0), r_min(0);
        solve( N, K, r_max, r_min);
        cout << "Case #" << i+1 << ": " 
            << r_max << " " << r_min << endl;
    }

    return 0;
}
