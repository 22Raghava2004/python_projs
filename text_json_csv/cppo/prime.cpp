#include<iostream>
using namespace std;
int main()
{
    int num;
    cout<<"enter the num";
    cin>>num;
    if (num<2)
    {
        cout<<"not prime:";

    }
    else{
        for (int i=2;i<num;i++)
        { 
            if(num%i==0)
            {
                cout<<"not primt";
                    return 0;}
            
            
        }
    cout<<"prime";
    return 0;
    }
}
