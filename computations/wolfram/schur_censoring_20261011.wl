ClearAll["Global`*"];
p = {{1/2, 1/4, 1/4}, {1/8, 1/2, 3/8}, {3/8, 1/4, 3/8}};
pc = p[[1;;2, 1;;2]] + Outer[Times, p[[1;;2, 3]], p[[3, 1;;2]]]/(1-p[[3,3]]);
x = {z,-z}; t = {p[[3, 1;;2]].x/(1-p[[3,3]])};
lift = Join[x,t]; lift0 = lift-Total[lift]/3;
left = (p.lift0).(p.lift0)-s2 lift0.lift0;
extra = t.t-Total[t]^2/3;
right = (pc.x).(pc.x)-s2 x.x+(1-s2) extra;
h = {{1,1,1,1},{1,-1,1,-1},{1,1,-1,-1},{1,-1,-1,1}}/2;
feedback = h[[2;;4,2;;4]]+2 Outer[Times,h[[2;;4,1]],h[[1,2;;4]]];
mean = Abs[h[[2;;4,2;;4]]]^2+Outer[Times,Abs[h[[2;;4,1]]]^2,Abs[h[[1,2;;4]]]^2]/(1-h[[1,1]]^2);
<|"version"->$Version, "energyIdentity"->(Together[left-right]===0),
"nonnegativeLiftCorrection"->(Together[extra-2 z^2/75]===0),
"exactMeanFlat"->(mean===ConstantArray[1/3,{3,3}]),
"exactPermutationFeedback"->(feedback==={{0,1,0},{1,0,0},{0,0,1}}),
"nonClaims"->{"Asymptotic theorem","All-time flatness probability","BGS proof"}|>
