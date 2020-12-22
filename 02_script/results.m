%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                   Reaction times of PVT task
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Very brief first analysis of all recorded .xdf files
% Data: Covidom (Walter Maetzler, University of Kiel)
% Author: Julius Welzel (j.welzel@neurologie.uni-kiel.de)

clc; clear all; close all;

MAIN = [fileparts(pwd) '\'];
addpath(genpath(MAIN));

%Change MatLab defaults
set(0,'defaultfigurecolor',[1 1 1]);

%% Set envir

PATHIN      = [MAIN '03_data\00_raw\'];
PATHOUT     = [MAIN '03_data\01_prep_ss\'];

if ~isdir(PATHOUT);mkdir(PATHOUT);end

%% Get subjs

list = dir(fullfile([PATHIN '*.xdf']));
nms_SUBJ = extractBetween({list.name},'pvt_','.xdf');

for s = 1:numel(nms_SUBJ)

    % load data
    tmp = load_xdf([PATHIN 'pvt_' nms_SUBJ{s} '.xdf']);
    pvt = findLslStream(tmp,'PsychoPyTrigger');

    % find all trial starts and button presses
    idx_ts = find(strcmp(pvt.time_series,'Trial start'));
    idx_bps = find(strcmp(pvt.time_series,'BP'));

   %prelocate
   RT = [];
   c = 1;

   for i = 9:numel(idx_bps)

       if idx_bps(i)-idx_ts(i) ~= 1; continue;end

       RT(c)    = pvt.time_stamps(idx_bps(i))-pvt.time_stamps(idx_ts(i));
       c        = c+1;

   end

   figure
   subplot(1,2,1)
   singleBoxplot({RT})
   tune_BP([87, 95, 207]/255)
        ylabel 'RT [s]'
        xticklabels 'PVT'
        
    subplot(1,2,2)
    plot(RT,'.','Color',[.8 .8 .8],'MarkerSize',15)
    hline(mean(RT),'k--')
        ylabel 'RT [s]'
        xlabel 'Trial number'
        box off

    save_fig(gcf,PATHOUT,[nms_SUBJ{s} '_pvt'])

end
