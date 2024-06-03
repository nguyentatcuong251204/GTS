#include<iostream>
#include<cmath>
#include<iomanip>
using namespace std;

double f_x(double a,int n,double arr[10000]){
    double result=0;
    for(int i=0;i<=n;i++){
        result+=arr[i]*pow(a,n-i);
    }
    return result;
}
double f_derivative1(double a,int n,double arr[10000]){
    double result=0;
    for(int i=0;i<=n;i++){
        result+=(n-i)*arr[i]*pow(a,n-i-1);
    }
    return result;
}
double f_derivative2(double a,int n,double arr[10000]){
    double result=0;
    for(int i=0;i<=n;i++){
        result+=(n-i)*(n-i-1)*arr[i]*pow(a,n-i-2);
    }
    return result;
}
double dx(double a,int n,double arr[10000],double d){
        return -(f_x(a,n,arr)*(a-d))/(f_x(a,n,arr)-f_x(d,n,arr));
    }
void pp_day_cung(double can_trai,double can_phai,double ep,int n,double arr[10000]){
    double x;
    double d;
    if(f_derivative2((can_trai+can_phai)/2,n,arr)*f_x(can_trai,n,arr)>0){
        int cnt=1;
        d=can_trai;
        x=can_phai;
        cout<<"x"<<"                                          "<<"dx"<<endl;
        while(abs(dx(x,n,arr,d))>ep){
            x=x+dx(x,n,arr,d);
            cout<<setprecision(15)<<x<<"                         "<<dx(x,n,arr,d)<<endl;
            cnt+=1;
        }
    }
    else{
        d=can_phai;
        x=can_trai;
        int cnt=1;
        cout<<"x"<<"                    "<<"dx"<<endl;
        while(abs(dx(x,n,arr,d))>ep){
            x=x+dx(x,n,arr,d);
            cout<<setprecision(15)<<x<<cnt<<"                         "<<dx(x,n,arr,d)<<endl;
            cnt+=1;
        }
    }
    
}
int main(){
    int n;cout<<"NHAP VAO BAC CUA DA THUC : ";cin>>n;
    double a[10000];
    for(int i=0;i<=n;i++){
        cout<<"NHAP VAO HE SO X^"<<n-i<<" ";
        cin>>a[i];
    }
    double can_trai,can_phai,ep;
    cout<<"NHAP VAO CAN TRAI ";cin>>can_trai;
    cout<<"NHAP VAO CAN PHAI ";cin>>can_phai;
    cout<<"NHAP VAO EPXILON ";cin>>ep;
    pp_day_cung(can_trai,can_phai,ep,n,a);
}