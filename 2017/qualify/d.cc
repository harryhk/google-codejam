#include<iostream>
#include<vector>
#include<string>
#include<set>
#include<iterator>
#include<algorithm>

using namespace std;

typedef vector< vector<char > >  ARR;

int get_points(const  ARR & arr)
{
    int point = 0;
    int N = arr.size();
    for( int i=0; i!= N ; i++ )
    {
        for( int j=0; j!= N ; j++ )
        {
            if( arr[i][j] == '+' || arr[i][j] == 'x' )
            {
                point ++;
            }
            else if( arr[i][j] == 'o' )
            {
                point +=2;
            }
        }
    }

    return point;
}

int get_changes( const ARR & arr, const ARR & arr_m)
{
    int changes= 0;
    int N = arr.size();
    for( int i=0; i!= N ; i++ )
    {
        for( int j=0; j!= N ; j++ )
        {
            if( arr[i][j] != arr_m[i][j] )
            {
                changes ++;
            }
        }
    }

    return changes;
}
    

struct Solution
{
    Solution( ARR & arr): arr_m( arr ) {
    
        points_m = get_points( arr_m );
        N = arr.size();
    }

    set<char> get_row_cand( int r, int c)
    {
        char pos = arr_m[r][c];
        set<char> rlt;
        rlt.insert( pos );

        if( pos == 'x' )
        {
            rlt.insert('o');
        }
        
        int c1(0), c2(0);
        for( int i=0; i!= N ; i++ ) 
        {
            if ( arr_m[r][i] =='o' || arr_m[r][i] == 'x' ) c1++;
        }

        for( int i=0; i!= N ; i++ ) 
        {
            if ( arr_m[i][c] =='o' || arr_m[i][c] == 'x' ) c2++;
        }

        if( pos == '+' )
        {
            if( c1 == 0 && c2 == 0 ) rlt.insert('o');
        }

        if( pos == '.' )
        {
            if( c1 == 0 && c2 == 0 ) 
            {
                rlt.insert('o');
                rlt.insert('x');
            }
            rlt.insert('+');
        }

        return rlt;
    }

    set<char> get_col_cand( int r, int c)
    {
        char pos = arr_m[r][c];
        set<char> rlt;
        rlt.insert( pos );

        if( pos == '+' )
        {
            rlt.insert('o');
        }
        
        int c1(0), c2(0);
        
        int i  = r - min(r,c);
        int j  = c - min(r,c);
        for( ; i!= N && j!=N ; i++, j++ ) 
        {
            if ( arr_m[i][j] =='o' || arr_m[i][j] == '+' ) c1++;
        }

        for( int i=0; i <= r+c ; i++ ) 
        {
            j = r+c -i;
            if( i < N &&  j < N )
            {
                if ( arr_m[i][j] =='o' || arr_m[i][j] == '+' ) c2++;
            }
        }

        if( pos == 'x' )
        {
            if( c1 == 0 && c2 == 0 ) rlt.insert('o');
        }

        if( pos == '.' )
        {
            if( c1 == 0 && c2 == 0 ) 
            {
                rlt.insert('o');
                rlt.insert('+');
            }
            rlt.insert('x');
        }

        return rlt;
    }
        
    set<char> get_cand( int pos )
    {
        set<char > rlt;
        if( pos < N * N ) 
        {
            int r = pos/ N;
            int c = pos % N;
            
            set<char> row_cand = get_row_cand( r, c );
            set<char> col_cand = get_col_cand( r, c );
            set_intersection( row_cand.begin(), row_cand.end(), col_cand.begin(), col_cand.end(), inserter(rlt, rlt.begin() ) );

        }

        if( rlt.count('o') > 0 )
        {
            set<char> tmp;
            tmp.insert('o');
            return tmp;
        }

        else if( rlt.count('x') > 0 )
        {
            set<char> tmp;
            tmp.insert('x');
            return tmp;
        }
        else if( rlt.count('+') > 0 )
        {
            set<char> tmp;
            tmp.insert('+');
            return tmp;
        }
        else if ( rlt.count('.') > 0 )
        {
            set<char> tmp;
            tmp.insert('.');
            return tmp;
        }
        return rlt;
        
    }
    
    void print()
    {
        for( int i=0; i!= N ; i++)
        {
            for( int j=0; j!=N; j++) cout << arr_m[i][j] << " ";
            cout << endl;
        }
    }

    void solve(  int pos, ARR &  arr_rlt )
    {
        int r = pos/ N;
        int c = pos % N;
        //cout << pos << endl;
        //print();
         
        set<char> cands = get_cand( pos);
        if( cands.empty() ) 
        {
            int curr_point = get_points( arr_m );
            if ( curr_point > points_m )
            {
                //cout << "max point " << curr_point << endl; 
                points_m = curr_point;
                arr_rlt = arr_m;
            }
            
        }
        else
        {
            char old = arr_m[r][c];
            for( auto m : cands )
            {
                arr_m[r][c] = m;
                solve( pos+1, arr_rlt );

            }
            arr_m[r][c] = old;
        }
    }

    ARR  arr_m;
    int points_m;
    int N;

};

int main()
{ 
    
    int n(0), N(0), M(0);
    cin>> n;
    for( int i=0; i!= n ; i++)
    {
        cin >> N >> M;
        ARR  arr(N, vector<char>(N, '.' ) );
        char c;
        int R(0), C(0);
        for( int j=0; j!= M ; j++ )
        {
            cin >> c >> R >> C;
            arr[R-1][C-1] =  c;
            
        }
        Solution solv( arr );
        
        ARR arr_rlt( arr );
        solv.solve( 0 , arr_rlt);

        cout << "Case #" << i+1 << ": " 
            << get_points( arr_rlt)  << " " << get_changes( arr_rlt, arr )<< endl;
        for( int r= 0; r != N ; r++ )
        {
            for( int c = 0; c!= N ; c++ )
            {
                if( arr_rlt[r][c] != arr[r][c] )
                {
                    cout << arr_rlt[r][c] << " " << r+1 << " " << c+1 << endl;
                }

            }
        }
    }

    return 0;
}
