def hgcallayout(i, p, *rows): i["HGCAL/Layouts/" + p] = DQMItem(layout=rows)

########### define varialbles for frequently used strings #############
hgcallink = "   >>> <a href=https://hgcaldocs.web.cern.ch/RawDataHandling/dqm_sysval/>Description</a>"
quality = "summary of module status"
summary = "wafer map for hgcal"
digis = "digis information"

################### Links to TOP Summary Histograms #################################
hgcallayout(dqmitems, "01-econdQuality",
          [{ 'path': "HGCAL/econdQuality", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "02-layer_summary_avgadc",
          [{ 'path': "HGCAL/layer_summary_avgadc", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "03-layer_summary_avgcm",
          [{ 'path': "HGCAL/layer_summary_avgcm", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "04-layer_summary_avgtoa",
          [{ 'path': "HGCAL/layer_summary_avgtoa", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "05-layer_summary_avgtot",
          [{ 'path': "HGCAL/layer_summary_avgtot", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "06-layer_summary_deltaadc",
          [{ 'path': "HGCAL/layer_summary_deltaadc", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "07-layer_summary_n_vacant_channels",
          [{ 'path': "HGCAL/layer_summary_n_vacant_channels", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "08-layer_summary_occupancy",
          [{ 'path': "HGCAL/layer_summary_occupancy", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "09-layer_summary_stdadc",
          [{ 'path': "HGCAL/layer_summary_stdadc", 'description': quality + hgcallink }])
