#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;
double abs(double x,double y){
    return x>y ? x-y:y-x;
}
double f_x(double x){
    return log(x)-1;
}
char sign(double a){
    if(a>0) return '+';
    else{
        return '-';
    }
    
}
void pp_chia_doi(double a,double b,double epxilon){
    double m;
    cout<<"STT        an        bn        xn        sign        denta_xn"<<endl;
    int cnt=1;
    while(abs(a,b)>epxilon){
        cout<<cnt<<"          "<<a<<"          "<<b<<"         "<<setprecision(15)<<((a+b)/2)<<"          "<<sign(f_x((a+b)/2))<<"          "<<(abs(a,b)/2)<<endl;
        m=(a+b)/2;
        if(f_x(m)*f_x(a)>0){
            a=m;
        }
        else{
            b=m;
        }
        cnt++;
    }
}

int main(){
    double a,b,epx;
    cout<<"NHAP VAO GIA TRI CUA a : ";cin>>a;
    cout<<"NHAP VAO GIA TRI CUA b : ";cin>>b;
    cout<<"NHAP VAO GIA TRI CUA epxilon : ";cin>>epx;
    pp_chia_doi(a,b,epx);
}