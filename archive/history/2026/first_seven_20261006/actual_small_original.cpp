#define main polynomial_certificate_main
#include "review.cpp"
#undef main
int inverse_mod(int a,int n){for(int k=1;k<n;k++)if(a*k%n==1)return k;throw runtime_error("inverse_mod");}
int rankm(Mat a){int r=0;for(int k=0;k<(int)a[0].size()&&r<(int)a.size();k++){int j=r;while(j<(int)a.size()&&!a[j][k])j++;if(j==(int)a.size())continue;swap(a[j],a[r]);int v=inv(a[r][k]);for(int i=r+1;i<(int)a.size();i++)if(a[i][k]){int c=mul(a[i][k],v);for(int h=k+1;h<(int)a[0].size();h++)a[i][h]=sub(a[i][h],mul(c,a[r][h]));a[i][k]=0;}r++;}return r;}
int main(){field();for(int N: {7,21,63}){int L=N/7,h=inverse_mod(2,N),a=(1-h+N)%N,ih=inverse_mod(8,N),q=pw(5,63/N);P d(N,1);for(int t=1;t<L;t++)for(int j=0;j<7;j++){int z=pw(q,t+j*L),s=sub(pw(z,7),1),u=add(z,1);int b=ng[mul(mul(s,s),mul(mul(u,u),inv(pw(z,8))))];req(b!=0,"internal zero");d[t*7+j]=mul(d[(t-1)*7+j],inv(b));}Mat G(N,P(N));for(int t=0;t<L;t++)for(int j=0;j<7;j++)for(int s=0;s<L;s++)for(int k=0;k<7;k++){int x=(a+t+j*L)%N,y=(a+s+k*L)%N;int e=(-ih*(3*x*x-2*x*y+3*y*y))%N;if(e<0)e+=N;G[t*7+j][s*7+k]=mul(mul(inv(d[t*7+j]),pw(q,e)),d[s*7+k]);}
Mat equations(N*N,P(L*49-1));for(int t=0;t<L;t++)for(int i=0;i<7;i++)for(int s=0;s<L;s++)for(int k=0;k<7;k++){int row=(t*7+i)*N+s*7+k;for(int dd=0;dd<L;dd++)for(int u=0;u<7;u++)for(int v=0;v<7;v++){int col=dd*49+7*u+v-1;if(col<0)continue;int left=(i==u&&t+dd<L)?G[(t+dd)*7+v][s*7+k]:0;int right=(v==k&&s>=dd)?G[t*7+i][(s-dd)*7+u]:0;equations[row][col]=sub(left,right);}}
int rank=rankm(equations),nul=L*49-rank;req(N==7?rank<48:rank==L*49-1,"actual nullity");cout<<"ACTUAL characteristic5 N="<<N<<" chain depth="<<L<<" restricted equations="<<N*N<<" by "<<L*49-1<<" rank="<<rank<<" full common commutant dimension="<<nul<<endl;
}return 0;}
