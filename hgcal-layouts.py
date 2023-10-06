def hgcallayout(i, p, *rows): i["HGCAL/Layouts/" + p] = DQMItem(layout=rows)

########### define varialbles for frequently used strings #############
hgcallink = "   >>> <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftRPC>Description</a>"
summary = "summary map for hgcal, this is NOT an efficiency measurement. Each bin is normalized to 1 considering disconnected chamber"
noise = "Average number of noisy strip per roll, counted if a occupancy of single strip is greater than 3.5 times the average of a chamber"
hgcalevents = "Events processed by the RPC DQM"
fed = "FED Fatal Errors"
top = "RPC TOP Summary Histogram <br><font color=green><b>GREEN</b> - Good Chamber </font><br> <font color=blue><b>BLUE</b> - Chamber OFF</font><br> <font color=yellow><b>YELLOW</b> - Noisy Strip </font><br> <font color=orange><b>ORANGE</b> - Noisy Chamber </font><br> <font color=pink><b>PINK</b> - Partly Dead Chamber </font><br> <font color=red><b>RED</b> - Fully Dead Chamber </font><br> <font color=aqua><b>LIGHT BLUE</b> - Bad Occupancy Shape </font> <br>"
occupancy = "Occupancy "
clsize = "Cluster Size of RPC system"
nrofcl = "Number of clusters, i.e. reconstructed hits."
nrofdigi = "Number of single hits."
bx = "RPC BX distribution "
emtf = "RPC L1T EMTF information. "

################### Links to TOP Summary Histograms #################################
#hgcallayout(dqmitems, "00-Summary_Map",
#          [{ 'path': "HGCAL/Summary/p_adc", 'description': summary + hgcallink }])

hgcallayout(dqmitems, "01-ChannelId-0_1_5_0",
          [{ 'path': "HGCAL/Summary/hex_channelId0_1_5_0", 'description': summary + hgcallink }])
hgcallayout(dqmitems, "02-ChannelId-0_2_5_0",
          [{ 'path': "HGCAL/Summary/hex_channelId0_2_5_0", 'description': summary + hgcallink }])

hgcallayout(dqmitems, "03-Pedestal-0_1_5_0",
          [{ 'path': "HGCAL/Summary/hex_pedestal0_1_5_0", 'description': summary + hgcallink }])
hgcallayout(dqmitems, "04-Pedestal-0_2_5_0",
          [{ 'path': "HGCAL/Summary/hex_pedestal0_2_5_0", 'description': summary + hgcallink }])

#hgcallayout(dqmitems, "05-Correlation_Ch22",
#          [{ 'path': "HGCAL/Digis/h2d_adc_channel_22", 'description': summary + hgcallink }])

##Noisy summary
#hgcallayout(dqmitems, "01-Noisy_summary_Map",
#          [{ 'path': "HGCAL/EventInfo/noisySummaryMap", 'description': noise + hgcallink }])
#
##FED Fatal
#hgcallayout(dqmitems, "02-Fatal_FED_Errors",
#          [{ 'path': "HGCAL/FEDIntegrity_EvF/FEDFatal", 'description': fed + hgcallink }])
#
##HGCAL Events
#hgcallayout(dqmitems, "03-HGCAL_Events",
#          [{ 'path': "HGCAL/AllHits/HGCALEvents", 'description': hgcalevents + hgcallink }])
#
