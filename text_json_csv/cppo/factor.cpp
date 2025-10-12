#include<iostream>
using namespace std;

int main()
{   int num;
    int fact;
    cout<<"enter fact";
    cin>>fact;
    int fact1=1;
    
    for (int i=1;i<fact+1;i+=1)
    {
         fact1=fact1*i;
        
    }
    cout<<fact1;
    return 0;
}