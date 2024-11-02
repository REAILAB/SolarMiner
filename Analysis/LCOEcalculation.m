%% Step1: Aera calculation from the segmentation results
% % For Zibo24 dataset
% clc;
% clear all;
% A_RA = [1,1,1,1,1,1
%       5.5,1.4,1.8,1.3,12.1,1.1
%       0.18,0.12,0.25,0.08,0.35,0.20];
% K  = [0.6,0.7,0.65,0.8,0.5,0.4
%       0.7,0.6,0.7,0.8,0.6,0.3
%       0.5,0.6,0.4,0.2,0.6,0.1];
% % RAA rooftop area is from the segmentation results fom Segment Anything
% % Model in Pytorch and Python, so the matrix is only as input here.
% RAA = [56194238,32877425,44583152,82321505,9843321,86554648
%     56194238,32877425,44583152,82321505,9843321,86554648
%     56194238,32877425,44583152,82321505,9843321,86554648];
% APV= RAA.* A_RA.* K;
% APV = APV/2.094/1.038;
% format bank; 
% % disp(APV')
%% Step2: PV power generation from PV model
% PVlib in this paper is developed in Python, so here are the calculation
% results only.
PVG = [946.23
257.75
500.48];
% PV panel number
num_P = [2323165217
452306087
565382609];
%% Step3: LCOE calculation
% the relative cost are changing in the below 2 matrics.
Com_r=[0.14
0.21
0.49];
Cequ=[22.41
25.15
26.75];

LC = (Com_r+Cequ)./1.05;
E = PVG./1.05;
for i = 2:1:25
    LC = LC+Com_r./(1.05^i);
    E = E + PVG./(1.05^i);
end
EE = E.*1000; % kWh to TWh
%disp(LC)
 
capa = num_P.*450;
LCOE = (capa.*LC)./EE;
disp(LCOE);

%% Step4: Carbon calculation
% Please calculate with the Emission Factor (EF)


