%---------------Dipole antenna simulation----------------------------------
clear all
close all
clc
NX=100;               % whole space x dimension
NY=100;               % whole space y dimension
NZ=100;               % whole space z dimension
dipole_length=0.5;    % dipole length (wavelength)
radi=0.01;            % dipole radius (wavelength)
cell_x=0.5/34;        % cell dimension 
Nd=floor(dipole_length/cell_x)+1;

xc=ceil(NX/2);
yc=ceil(NY/2);
zc=ceil(NZ/2);

c0=3e8;
dt=cell_x/(2*c0);     %Time step
Z0=377;

px=7;                 %PML length in x diection
py=7;                 %PML length in y diection
pz=7;                 %PML length in z diection

pml_length=px;
p0=0.33;

pxb=NX-px-1;
pyb=NY-py-1;
pzb=NZ-pz-1;

ex=zeros(NX,NY,NZ);  % Initializing the E-field vector
ey=zeros(NX,NY,NZ);
ez=zeros(NX,NY,NZ);

dx=zeros(NX,NY,NZ);  % Initializing the D vector
dy=zeros(NX,NY,NZ);
dz=zeros(NX,NY,NZ);

hx=zeros(NX,NY,NZ);  % Initializing the H-field vector
hy=zeros(NX,NY,NZ);
hz=zeros(NX,NY,NZ);

cx=ones(NX,NY,NZ);
cy=ones(NX,NY,NZ);
cz=ones(NX,NY,NZ);

curr_dxl=zeros(px,NY,NZ);
curr_dxh=zeros(px,NY,NZ);
curr_dyl=zeros(NX,py,NZ);
curr_dyh=zeros(NX,py,NZ);
curr_dzl=zeros(NX,NY,pz);
curr_dzh=zeros(NX,NY,pz);

curr_hxl=zeros(px,NY,NZ);
curr_hxh=zeros(px,NY,NZ);
curr_hyl=zeros(NX,py,NZ);
curr_hyh=zeros(NX,py,NZ);
curr_hzl=zeros(NX,NY,pz);
curr_hzh=zeros(NX,NY,pz);

curr_dipole=zeros(35,2048); % Initializing the dipole current

%---------------Specify Dipole----------------------------%

for k=zc-floor(Nd/2):zc+floor(Nd/2)
    cz(xc,yc,k)=0.0;
end

cz(xc,yc,zc)=1.0;
%--------------PML boundary condition---------------------%
mx1=zeros(1,NX);
nx1=zeros(1,NX);
mx2=ones(1,NX);
nx2=ones(1,NX);
mx3=ones(1,NX);
nx3=ones(1,NX);

my1=zeros(1,NY);
ny1=zeros(1,NY);
my2=ones(1,NY);
ny2=ones(1,NY);
my3=ones(1,NY);
ny3=ones(1,NY);

mz1=zeros(1,NZ);
nz1=zeros(1,NZ);
mz2=ones(1,NZ);
nz2=ones(1,NZ);
mz3=ones(1,NZ);
nz3=ones(1,NZ);

pml_length=7;
for i=1:pml_length
    ax=(pml_length-i+1)/pml_length;
    ax1=p0*ax^3;
    nx1(i)=ax1;
    nx1(NX-i+1)=ax1;
    mx2(i)=1/(1+ax1);
    mx2(NX-i+1)=1/(1+ax1);
    mx3(i)=(1-ax1)/(1+ax1);
    mx3(NX-i+1)=(1-ax1)/(1+ax1);
    ax=(pml_length-i+0.5)/pml_length;
    ax1=p0*ax^3;
    mx1(i)=ax1;
    mx1(NX-i)=ax1;
    nx2(i)=1/(1+ax1);
    nx2(NX-i)=1/(1+ax1);
    nx3(i)=(1-ax1)/(1+ax1);
    nx3(NX-i)=(1-ax1)/(1+ax1);
end

for j=1:pml_length
    ax=(pml_length-j+1)/pml_length;
    ax1=p0*ax^3;
    ny1(j)=ax1;
    ny1(NX-j+1)=ax1;
    my2(j)=1/(1+ax1);
    my2(NX-j+1)=1/(1+ax1);
    my3(j)=(1-ax1)/(1+ax1);
    my3(NX-j+1)=(1-ax1)/(1+ax1);
    ax=(pml_length-j+0.5)/pml_length;
    ax1=p0*ax^3;
    my1(j)=ax1;
    my1(NX-j)=ax1;
    ny2(j)=1/(1+ax1);
    ny2(NX-j)=1/(1+ax1);
    ny3(j)=(1-ax1)/(1+ax1);
    ny3(NX-j)=(1-ax1)/(1+ax1);
end

for k=1:pml_length
    ax=(pml_length-k+1)/pml_length;
    ax1=p0*ax^3;
    nz1(k)=ax1;
    nz1(NX-k+1)=ax1;
    mz2(k)=1/(1+ax1);
    mz2(NX-k+1)=1/(1+ax1);
    mz3(k)=(1-ax1)/(1+ax1);
    mz3(NX-k+1)=(1-ax1)/(1+ax1);
    ax=(pml_length-k+0.5)/pml_length;
    ax1=p0*ax^3;
    mz1(k)=ax1;
    mz1(NX-k)=ax1;
    nz2(k)=1/(1+ax1);
    nz2(NX-k)=1/(1+ax1);
    nz3(k)=(1-ax1)/(1+ax1);
    nz3(NX-k)=(1-ax1)/(1+ax1);
end



Ts=0.0;         %time sample
Tsmax=2048;     %maximum number of time samples
Is=0;
%***************************start of FDTD loop******************
for n=1:Tsmax
    Ts=Ts+dt;
%***************************Dx field****************************
    for i=2:px
        for j=2:NY
            for k=2:NZ
                curl_h=(hz(i,j,k)-hz(i,j-1,k)-hy(i,j,k)+hy(i,j,k-1));
                curr_dxl(i,j,k)=curr_dxl(i,j,k)+curl_h;
                dx(i,j,k)=(my3(j)*mz3(k)*dx(i,j,k))+(my2(j)*mz2(k)*0.5*(curl_h+mx1(i)*curr_dxl(i,j,k)));
            end
        end
    end
 %***************************************************************
 
    for i=px+1:pxb+1
        for j=2:NY
            for k=2:NZ
                curl_h=(hz(i,j,k)-hz(i,j-1,k)-hy(i,j,k)+hy(i,j,k-1));
                dx(i,j,k)=(my3(j)*mz3(k)*dx(i,j,k))+(my2(j)*mz2(k)*0.5*curl_h);
            end
        end
    end
 %***************************************************************
 for i=pxb+2:NX
     for j=2:NY
         for k=2:NZ
             x_up=i-pxb-1;
             curl_h=(hz(i,j,k)-hz(i,j-1,k)-hy(i,j,k)+hy(i,j,k-1));
             curr_dxh(x_up,j,k)=curr_dxh(x_up,j,k)+curl_h;
             dx(i,j,k)=(my3(j)*mz3(k)*dx(i,j,k))+(my2(j)*mz2(k)*0.5*(curl_h+mx1(i)*curr_dxh(x_up,j,k)));
         end
     end
 end
 
 %************************Dy field*******************************
 for i=2:NX
        for j=2:py
            for k=2:NZ
                curl_h=(hx(i,j,k)-hx(i,j,k-1)-hz(i,j,k)+hz(i-1,j,k));
                curr_dyl(i,j,k)=curr_dyl(i,j,k)+curl_h;
                dy(i,j,k)=(mx3(i)*mz3(k)*dy(i,j,k))+(mx2(i)*mz2(k)*0.5*(curl_h+my1(j)*curr_dyl(i,j,k)));
            end
        end
 end
 %***************************************************************
 for i=2:NX
        for j=py+1:pyb+1
            for k=2:NZ
                curl_h=(hx(i,j,k)-hx(i,j,k-1)-hz(i,j,k)+hz(i-1,j,k));
                dy(i,j,k)=(mx3(i)*mz3(k)*dy(i,j,k))+(mx2(i)*mz2(k)*0.5*curl_h);
            end
        end
 end
 %***************************************************************
 for i=2:NX
        for j=pyb+2:NY
            for k=2:NZ
                y_up=j-pyb-1;
                curl_h=(hx(i,j,k)-hx(i,j,k-1)-hz(i,j,k)+hz(i-1,j,k));
                curr_dyh(i,y_up,k)=curr_dyh(i,y_up,k)+curl_h;
                dy(i,j,k)=(mx3(i)*mz3(k)*dy(i,j,k))+(mx2(i)*mz2(k)*0.5*(curl_h+my1(j)*curr_dyh(i,y_up,k)));
            end
        end
 end
 %***************************Dz field****************************
  for i=2:NX
        for j=2:NY
            for k=2:pz
                curl_h=(hy(i,j,k)-hy(i-1,j,k)-hx(i,j,k)+hx(i,j-1,k));
                curr_dzl(i,j,k)=curr_dzl(i,j,k)+curl_h;
                dz(i,j,k)=(mx3(i)*my3(j)*dz(i,j,k))+(mx2(i)*my2(j)*0.5*(curl_h+mz1(k)*curr_dzl(i,j,k)));
            end
        end
 end
 %***************************************************************
 for i=2:NX
        for j=2:NY
            for k=pz+1:pzb+1
                curl_h=(hy(i,j,k)-hy(i-1,j,k)-hx(i,j,k)+hx(i,j-1,k));
                dz(i,j,k)=(mx3(i)*my3(j)*dz(i,j,k))+(mx2(i)*my2(j)*0.5*curl_h);
            end
        end
 end
 %***************************************************************
 for i=2:NX
        for j=2:NY
            for k=pzb+2:NZ
                z_up=k-pzb-1;
                curl_h=(hy(i,j,k)-hy(i-1,j,k)-hx(i,j,k)+hx(i,j-1,k));
                curr_dzh(i,j,z_up)=curr_dzh(i,j,z_up)+curl_h;
                dz(i,j,k)=(mx3(i)*my3(j)*dz(i,j,k))+(mx2(i)*my2(j)*0.5*(curl_h+mz1(k)*curr_dzh(i,j,z_up)));
            end
        end
 end
 %***********************Source**********************************
 f=300e6;
 source(n)=sin(2 * pi * f * Ts);   
 dz(xc,yc,zc)=source(n);
 %************************Calculating E from D*******************
  
 for k=2:NZ-1
     for j=2:NY-1
         for i=2:NX-1
             ex(i,j,k)=cx(i,j,k)*dx(i,j,k);
             ey(i,j,k)=cy(i,j,k)*dy(i,j,k);
             ez(i,j,k)=cz(i,j,k)*dz(i,j,k);
         end
     end
 end
 %***************************************************************
 for j=1:NY
     for k=1:NZ
         ex(1,j,k)=0;
         ey(1,j,k)=0;
         ez(1,j,k)=0;
     end
 end
 for j=1:NY
     for k=1:NZ
         ex(NX,j,k)=0;
         ey(NX,j,k)=0;
         ez(NX,j,k)=0;
     end
 end
 for i=1:NX
     for k=1:NZ
         ex(i,1,k)=0;
         ey(i,1,k)=0;
         ez(i,1,k)=0;
     end
 end
 for i=1:NX
     for k=1:NZ
         ex(i,NY,k)=0;
         ey(i,NY,k)=0;
         ez(i,NY,k)=0;
     end
 end
 for i=1:NX
     for j=1:NY
         ex(i,j,1)=0;
         ey(i,j,1)=0;
         ez(i,j,1)=0;
     end
 end
 for i=1:NX
     for j=1:NY
         ex(i,j,NZ)=0;
         ey(i,j,NZ)=0;
         ez(i,j,NZ)=0;
     end
 end
 %***************************Hx field****************************
    for i=1:px
        for j=1:NY-1
            for k=1:NZ-1
                curl_e=(ey(i,j,k+1)-ey(i,j,k)-ez(i,j+1,k)+ez(i,j,k));
                curr_hxl(i,j,k)=curr_hxl(i,j,k)+curl_e;
                hx(i,j,k)=(ny3(j)*nz3(k)*hx(i,j,k))+ny2(j)*nz2(k)*0.5*(curl_e+nx1(i)*curr_hxl(i,j,k));
            end
        end
    end
 %***************************************************************
 for i=px+1:pxb+1
        for j=1:NY-1
            for k=1:NZ-1
                curl_e=(ey(i,j,k+1)-ey(i,j,k)-ez(i,j+1,k)+ez(i,j,k));
                hx(i,j,k)=(ny3(j)*nz3(k)*hx(i,j,k))+ny2(j)*nz2(k)*0.5*curl_e;
            end
        end
 end
 %***************************************************************
 for i=pxb+2:NX
        for j=1:NY-1
            for k=1:NZ-1
                x_up=i-pxb-1;
                curl_e=(ey(i,j,k+1)-ey(i,j,k)-ez(i,j+1,k)+ez(i,j,k));
                curr_hxh(x_up,j,k)=curr_hxh(x_up,j,k)+curl_e;
                hx(i,j,k)=(ny3(j)*nz3(k)*hx(i,j,k))+ny2(j)*nz2(k)*0.5*(curl_e+nx1(i)*curr_hxh(x_up,j,k));
            end
        end
 end
 
 %***************************Hy field****************************
    for i=1:NX-1
        for j=1:py
            for k=1:NZ-1
                curl_e=(ez(i+1,j,k)-ez(i,j,k)-ex(i,j,k+1)+ex(i,j,k));
                curr_hyl(i,j,k)=curr_hyl(i,j,k)+curl_e;
                hy(i,j,k)=(nx3(i)*nz3(k)*hy(i,j,k))+nx2(i)*nz2(k)*0.5*(curl_e+ny1(j)*curr_hyl(i,j,k));
            end
        end
    end
 %***************************************************************
 for i=1:NX-1
        for j=py+1:pyb+1
            for k=1:NZ-1
                curl_e=(ez(i+1,j,k)-ez(i,j,k)-ex(i,j,k+1)+ex(i,j,k));
                hy(i,j,k)=(nx3(i)*nz3(k)*hy(i,j,k))+nx2(i)*nz2(k)*0.5*curl_e;
            end
        end
 end
 %***************************************************************
 for i=1:NX-1
        for j=pyb+2:NY
            for k=1:NZ-1
                y_up=j-pyb-1;
                curl_e=(ez(i+1,j,k)-ez(i,j,k)-ex(i,j,k+1)+ex(i,j,k));
                curr_hyh(i,y_up,k)=curr_hyh(i,y_up,k)+curl_e;
                hy(i,j,k)=(nx3(i)*nz3(k)*hy(i,j,k))+nx2(i)*nz2(k)*0.5*(curl_e+ny1(j)*curr_hyh(i,y_up,k));
            end
        end
 end
 %***************************Hz field****************************
    for i=1:NX-1
        for j=1:NY-1
            for k=1:pz
                curl_e=(ex(i,j+1,k)-ex(i,j,k)-ey(i+1,j,k)+ey(i,j,k));
                curr_hzl(i,j,k)=curr_hzl(i,j,k)+curl_e;
                hz(i,j,k)=(nx3(i)*ny3(j)*hz(i,j,k))+nx2(i)*ny2(j)*0.5*(curl_e+nz1(k)*curr_hzl(i,j,k));
            end
        end
    end
 %****************************************************************
 for i=1:NX-1
        for j=1:NY-1
            for k=pz+1:pzb+1
                curl_e=(ex(i,j+1,k)-ex(i,j,k)-ey(i+1,j,k)+ey(i,j,k));
                hz(i,j,k)=(nx3(i)*ny3(j)*hz(i,j,k))+nx2(i)*ny2(j)*0.5*curl_e;
            end
        end
 end
 %****************************************************************
 for i=1:NX-1
        for j=1:NY-1
            for k=pzb+2:NZ
                z_up=k-pzb-1;
                curl_e=(ex(i,j+1,k)-ex(i,j,k)-ey(i+1,j,k)+ey(i,j,k));
                curr_hzh(i,j,z_up)=curr_hzh(i,j,z_up)+curl_e;
                hz(i,j,k)=(nx3(i)*ny3(j)*hz(i,j,k))+nx2(i)*ny2(j)*0.5*(curl_e+nz1(k)*curr_hzh(i,j,z_up));
            end
        end
 end
%*****************************************************************
k1=zc-floor(Nd/2);
k2=zc+floor(Nd/2);
for k=k1:k2
    curr_dipole(k-k1+1,n)=(hx(xc,yc,k)-hx(xc,yc-1,k)-hy(xc,yc,k)+hy(xc-1,yc,k))/Z0;
end
timestep=int2str(n);
% ex_time(:,:,:,n)=ex;
% ey_time(:,:,:,n)=ey;
% ez_time(:,:,:,n)=ez;
% hx_time(:,:,:,n)=hx;
% hy_time(:,:,:,n)=hy;
% hz_time(:,:,:,n)=hz;
for ii=2:NX
    for kk=2:NZ
        ez1(kk-1,ii-1)=ez(ii,yc,kk);
    end 
end
surf(2:NZ,2:NX,20*log10(abs(ez1))); view (0, 90); shading interp

 title(['Ez in the XZ plane at time step = ',timestep]);
set(gca,'Clim',[-80,0]);
colorbar
 pause(0.001);
end    
%-------------------end of FDTD loop---------------------------------------
%-------------------calculating the input impedance------------------------
I_input=curr_dipole(ceil(Nd/2),:);
Vfreq=source;
Ifreq=I_input;
df=1/(dt*Tsmax);    % frequency step
Zin=Vfreq./Ifreq;
Rin=real(Zin);
Xin=imag(Zin);
Yin=Ifreq./Vfreq;
Gin=real(Yin);
Bin=imag(Yin);
