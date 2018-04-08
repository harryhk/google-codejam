#include<iostream>
#include<queue>
#include<string>
#include<cmath>
#include<tuple>
#include<algorithm>
#include<set>

using namespace std;

class Data
{

public:
    Data( double  n, double p )
    {
        min_ = ceil( p / n / 1.1 );
        max_ = floor( p / n / 0.9 );
        if ( min_ > max_ )
        {
            min_ = -1;
            max_ = -1;
        }
    }


    friend bool operator<( const Data & lhs, const  Data &  rhs )
    {
        return tie(lhs.min_, lhs.max_) < tie(rhs.min_, rhs.max_ );
    }

    friend ostream & operator<< ( ostream & os, const Data & d )
    {
        os << "(" << d.min_ << "," << d.max_ << ")";
        return os;
    }

    int min_;
    int max_;
    
};

int n(0), N(0), P(0);


bool check( vector<int> & idx, vector< vector<Data> > & d )
{
    for( int  jj = 0; jj < N ; jj ++ )
    {
        if( idx[jj] == d[jj].size() ) return false; 
    }
    return true;
}

int solve( vector< vector<Data> > & data )
{
    set< int > pos_num;  

    for( int i = 0; i < N ; i++ )
    {
        sort( data[i].begin(), data[i].end() );
        for( auto & d : data[i] ) pos_num.insert( d.min_ ) ;
    }

    vector< int > idx(N );  // index for P 
    int count =0;
    
    if( pos_num.size() == 0 ) return 0;

    auto it_num =  pos_num.begin();

    while( check( idx, data ) && it_num != pos_num.end() )
    {
        bool found = true;

        for(int i=0; i < N ; i++ )
        {
            //cout << *it_num << "," << data[i][idx[i] ] << endl;
            if( * it_num > data[i][ idx[i] ].max_ )
            {
                idx[i] ++ ; 
                found = false;
                break;
            }
            if( *it_num < data[i][ idx[i] ].min_ )
            {
                found = false;
                it_num ++;
                break;
            }
        }
        
        if( found  ) 
        {
            count ++;
            for( int jj = 0; jj < N ; jj++ ) idx[jj] ++;
        }


    }

    return count ;
}

int main()
{ 
    
    cin>> n;
    for( int i=0; i!= n ; i++)
    {
        cin >> N >> P ;
        vector< vector< Data > > data(N, vector< Data >() );

        vector<int> NI(N);
        for( int ii = 0; ii < N ; ii++)
        {
            int t(0);
            cin >> t ;
            NI[ii] = t;
        }
        vector< vector<int> > PI(N, vector<int>(P) );
        for( int ii = 0; ii < N ; ii++)
        {
            for( int jj =0; jj < P ; jj ++ )
            {
                int t(0);
                cin >> t ;
                Data tmp( NI[ii], t );
                if( tmp.min_ != -1 ) data[ii].push_back( tmp ); 
            }
        }

        cout << "Case #" << i+1 << ": " 
            << solve( data ) << endl; 
    }

    return 0;
}
