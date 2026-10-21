Clear[q,z];
w=(-3+4 I)/5;
r=(1-(q^7+q^-7)/2)(1+(q+q^-1)/2);
a=Expand[(q^7+q^-7)/2+r/10+r(q-q^-1)/(200 I)+r(Conjugate[w] z+w/z)/200-1/10];
b=Expand[a/.{q->q^3 z^4,z->q^2 z^3}];
c=Coefficient[Coefficient[Expand[a b q^50 z^50],q,50],z,50];
q0=Coefficient[Coefficient[Expand[a^2 q^18 z^2],q,18],z,2];
{q0,c,2(q0-c)}

