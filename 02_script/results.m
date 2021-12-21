%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                   Reaction times of PVT task
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Very brief first analysis of all recorded .xdf files
% Data: Covidom (Walter Maetzler, University of Kiel)
% Author: Julius Welzel (j.welzel@neurologie.uni-kiel.de)

clc; clear all; close all;

filepath = fileparts(mfilename('fullpath'))
cd (filepath)

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

all     = table;
c       = 1; % counter for long table

for s = 1:numel(nms_SUBJ)
    
    % check id
    if contains(nms_SUBJ{s},'old')
        continue;
    end
    
        

    % load data
    try
        tmp = load_xdf([PATHIN 'pvt_' nms_SUBJ{s} '.xdf']);
    catch ME
        continue
    end
    
    pvt = findLslStream(tmp,'PsychoPyTrigger');

    % find all trial starts and button presses
    idx_ts = find(strcmp(pvt.time_series,'Trial start'));
    idx_bps = find(strcmp(pvt.time_series,'BP'));

    %prelocate

    for i = 9:numel(idx_bps)

        if idx_bps(i)-idx_ts(i) ~= 1; continue;end

        all.rt(c)   = pvt.time_stamps(idx_bps(i))-pvt.time_stamps(idx_ts(i));
        
        % add additinal info per trial
        all.id(c)           = string(nms_SUBJ{s});
        all.trialnumber(c)  = i;
        
        c           = c+1;
       
    end

%     figure
%     subplot(1,2,1)
%     singleBoxplot({rt})
%     tune_BP([87, 95, 207]/255)
%         ylabel 'RT [s]'
%         xticklabels 'PVT'
%         
%     subplot(1,2,2)
%     plot(rt,'.','Color',[.8 .8 .8],'MarkerSize',15)
%     hline(mean(rt),'k--')
%         ylabel 'RT [s]'
%         xlabel 'Trial number'
%         box off
%     lsline
% 
%     save_fig(gcf,PATHOUT,[nms_SUBJ{s} '_pvt'])

end


writetable(all,[PATHOUT 'all_trials_rt.csv']);

%% plot & stats
max_s = 30
idx_in = all.rt < max_s;

close all
subplot(1,2,1)
histogram(all.rt(idx_in))   
xlim ([0,max_s ])
ylabel 'Total [n]'
xlabel 'RTs [s]'
box off

% test for normality
% [h,p] = kstest(all.rt(idx_in))
% title (['Assumption of norm. dist. p = ' num2str(p)])

subplot(1,2,2)
scatter(all.trialnumber(idx_in),all.rt(idx_in))
lsline
xlabel 'Trial number [n]'
ylabel 'RTs [s]'
ylim ([0 max_s])
box off
