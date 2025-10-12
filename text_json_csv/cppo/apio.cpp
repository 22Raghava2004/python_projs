#include<iostream>
using namespace std;
int main()
{
    int num;
    cout<<"Enter a number from print"<<endl;
    cin>>num;
    int sum;
    cout<<"Enter the number  to print"<<endl;
    cin>>sum;
    int i;
    int total=0;

    for(i=0;i<sum;i=i+1)
    {
     int result=(num+i)*(num+i);
        cout<<result<<endl;
        total=total+result;
    }
    cout<<"The total is "<<total<<endl; 


    return 0;
}