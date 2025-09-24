def hgcallayout(i, p, *rows): i["HGCAL/Layouts/" + p] = DQMItem(layout=rows)

########### define varialbles for frequently used strings #############
hgcallink = "   >>> <a href=https://hgcaldocs.web.cern.ch/RawDataHandling/dqm_sysval/>Description</a>"
quality = "summary of module status"
summary = "wafer map for hgcal"
digis = "digis information"

################### Links to TOP Summary Histograms #################################
hgcallayout(dqmitems, "01-layer_1_hex_avgadc",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/Cassette_1/hex_avgadc_layer_1", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "02-layer_2_hex_avgadc",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_2/Cassette_1/hex_avgadc_layer_2", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "03-layer_3_hex_avgadc",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_3/Cassette_1/hex_avgadc_layer_3", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "04-layer_4_hex_avgadc",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_4/Cassette_1/hex_avgadc_layer_4", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "05-layer_5_hex_avgadc",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_5/Cassette_1/hex_avgadc_layer_5", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "06-layer_6_hex_avgadc",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_6/Cassette_1/hex_avgadc_layer_6", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "07-layer_7_hex_avgadc",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_7/Cassette_1/hex_avgadc_layer_7", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "08-layer_8_hex_avgadc",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_8/Cassette_1/hex_avgadc_layer_8", 'description': quality + hgcallink }])
