def hgcallayout(i, p, *rows): i["HGCAL/Layouts/" + p] = DQMItem(layout=rows)

########### define varialbles for frequently used strings #############
hgcallink = "   >>> <a href=https://hgcaldocs.web.cern.ch/RawDataHandling/dqm_sysval/>Description</a>"
quality = "summary of module status"
summary = "wafer map for hgcal"
digis = "digis information"

################### Links to TOP Summary Histograms #################################
hgcallayout(dqmitems, "Layer 1: Average ADC",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/Cassette_1/hex_avgadc_layer_1", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Layer 2: Average ADC",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_2/Cassette_1/hex_avgadc_layer_2", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Layer 3: Average ADC",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_3/Cassette_1/hex_avgadc_layer_3", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Layer 4: Average ADC",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_4/Cassette_1/hex_avgadc_layer_4", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Layer 5: Average ADC",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_5/Cassette_1/hex_avgadc_layer_5", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Layer 6: Average ADC",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_6/Cassette_1/hex_avgadc_layer_6", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Layer 7: Average ADC",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_7/Cassette_1/hex_avgadc_layer_7", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Layer 8: Average ADC",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_8/Cassette_1/hex_avgadc_layer_8", 'description': quality + hgcallink }])
