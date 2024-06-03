#include<iostream>
#include<math.h>
#include<iomanip>
using namespace std;
double ham_lap(double x){
    return (-pow(x,5)+17)/25;
}
void pp_lap(double x,double q,double ep){
    int cnt=1;
    while(abs(ham_lap(x)-x)>(ep*(1-q)/q)){
        cout<<"x"<<cnt<<"              ";
        cout<<setprecision(9)<<x;
        cout<<endl;
        x=ham_lap(x);
        cnt++;
    }
}
int main(){
    double x,q,ep;
    cout<<"NHAP GIA TRI X BAT KI TRONG KHOANG CACH LY : ";cin>>x;
    cout<<"\nNHAP GIA TRI Q-MAX(ABS(F_DERIVATIVE1)) TREN KHOANG CACH LY : ";cin>>q;
    cout<<"\nNHAP GIA TRI EPXILON : ";cin>>ep;
    pp_lap(x,q,ep);
    return 0;
}