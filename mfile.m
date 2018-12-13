%J=[0 0;0 0];
%J=[0 1; 0 0];
%J=[-1 0;0 0];
%J=[-2 0;0 -1];
%J=[-1 0;0 -1];
%J=[-1 1;0 -1];
%J=[-1 0;0 1];
%J=[0 -1;1 0];
%J=[-1 -1;1 -1];

P=eye(2);       
A=P*J*P^(-1);
hold on;
for j=-5:5
    WPC=[sin(j);cos(j)]; %wartoœæ pocz¹tkowa na kole jednostkowym
    open ('model2');
    sim ('model2');
    x1=x(:,1);
    x2=x(:,2);
    plot(x1,x2);
end;
title('Portret fazowy');
xlabel('x1');
ylabel('x2');
hold off;