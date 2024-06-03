#include<iostream>
#include<iomanip>
#include<cmath>
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
double dx(double x){
    return -f_x(x)/f_derivative1(x);
}

void pp_tiep_tuyen(double a,double b,double ep){
    cout<<"x                                           dx"<<endl;
    if(f_derivative2((a+b)/2)*f_x(a)>0){
        double x=a;
        while(abs(dx(x))>ep){
            cout<<setprecision(15)<<x;
            cout<<"                                            ";
            cout<<dx(x);
            cout<<endl;
            x=x+dx(x);
        }
    }
    else{
        double x=b;
        while(abs(dx(x))>ep){
            cout<<setprecision(15)<<x;
            cout<<"                                            ";
            cout<<dx(x);
            cout<<endl;
            x=x+dx(x);
        }
    }
}

int main(){
    pp_tiep_tuyen(1,3,0.00000000001);
}