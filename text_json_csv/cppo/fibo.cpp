#include<iostream>
using namespace std;
int main(){
    int num1,num2=0,non=1,i;
    cout<<"enter the num";
    cin>>num1;
    for(i=0;i<num1;i++)
    {   
        for(int j=0;j<i;j++)
        {
            non=non+num2;
            cout<<non<<endl;
        }
        num2=non;
        
    }
}