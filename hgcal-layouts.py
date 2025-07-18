def hgcallayout(i, p, *rows): i["HGCAL/Layouts/" + p] = DQMItem(layout=rows)

########### define varialbles for frequently used strings #############
hgcallink = "   >>> <a href=https://hgcaldocs.web.cern.ch/>Description</a>"
quality = "summary of module status"
summary = "wafer map for hgcal"
digis = "digis information"

################### Links to TOP Summary Histograms #################################
hgcallayout(dqmitems, "01-econdQuality",
          [{ 'path': "HGCAL/econdQuality", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "02-time_stamp",
          [{ 'path': "HGCAL/time_stamp", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "03-Layer1-Cassette1-econdQuality",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/Cassette_1/econdQualityCassette_1", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "04-Layer1-Cassette1-econdPayload",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/Cassette_1/econdPayloadCassette_1", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "05-Layer1-Cassette1-hex_avgadc",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/Cassette_1/hex_avgadc_layer_1", 'description': summary + hgcallink }])
hgcallayout(dqmitems, "06-Layer1-Cassette1-hex_occupancy",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/Cassette_1/hex_occupancy_layer_1", 'description': summary + hgcallink }])
hgcallayout(dqmitems, "07-Layer1-Cassette1-hex_stdadc",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/Cassette_1/hex_stdadc_layer_1", 'description': summary + hgcallink }])
hgcallayout(dqmitems, "08-Layer41-Cassette2-econdQuality",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_41/Cassette_2/econdQualityCassette_2", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "09-Layer41-Cassette2-econdPayload",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_41/Cassette_2/econdPayloadCassette_2", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "10-Layer41-Cassette2-hex_avgadc",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_41/Cassette_2/hex_avgadc_layer_41", 'description': summary + hgcallink }])
hgcallayout(dqmitems, "11-Layer41-Cassette2-hex_occupancy",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_41/Cassette_2/hex_occupancy_layer_41", 'description': summary + hgcallink }])
hgcallayout(dqmitems, "12-Layer41-Cassette2-hex_stdadc",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_41/Cassette_2/hex_stdadc_layer_41", 'description': summary + hgcallink }])
