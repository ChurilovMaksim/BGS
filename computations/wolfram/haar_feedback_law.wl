(* Exact finite polynomial controls, not an analytic Haar or BGS proof. *)
Clear[a, xr, xi, y];
vars = {a, xr, xi, y};
image = {a, a xr-xi, xr+a xi,
         a (xr^2+xi^2)+(1+xr^2+xi^2) y};
jac = Det[Outer[D,image,vars]];
h = {{a, (xr-I xi)(a-I)},
     {(xr+I xi)(a+I), Last[image]}};
{Simplify[jac == (1+a^2)(1+xr^2+xi^2)],
 Simplify[Det[IdentityMatrix[2]+h.h] ==
          (1+a^2)(1+xr^2+xi^2)^2(1+y^2)]}
