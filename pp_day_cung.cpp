#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;

double f_x(double a){
    return log(a)-1;
}
double f_derivative1(double a){
    return 1/a;
}
double f_derivative2(double a){
    return -1/pow(a,2);
}
double dx(double x,double d){
        return -(f_x(x)*(x-d))/(f_x(x)-f_x(d));
    }
void pp_day_cung(double a,double b,double ep){
    double x;
    double d;
    if(f_derivative2((a+b)/2)*f_x(a)>0){
        int cnt=1;
        d=a;
        x=b;
        cout<<"x"<<"                                          "<<"dx"<<endl;
        while(abs(dx(x,d))>ep){
            x=x+dx(x,d);
            cout<<setprecision(15)<<x<<"                         "<<dx(x,d)<<endl;
            cnt+=1;
        }
    }
    else{
        d=b;
        x=a;
        int cnt=1;
        cout<<"x"<<"                    "<<"dx"<<endl;
        while(abs(dx(x,d))>ep){
            x=x+dx(x,d);
            cout<<setprecision(15)<<x<<cnt<<"                         "<<dx(x,d)<<endl;
            cnt+=1;
        }
    }
    
}
int main(){
    pp_day_cung(1,3,0.000000001);
}