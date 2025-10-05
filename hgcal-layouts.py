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
hgcallayout(dqmitems, "Layer 9: Average ADC",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_9/Cassette_1/hex_avgadc_layer_9", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Layer 10: Average ADC",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_10/Cassette_1/hex_avgadc_layer_10", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Layer 11: Average ADC",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_11/Cassette_1/hex_avgadc_layer_11", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Layer 12: Average ADC",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_12/Cassette_1/hex_avgadc_layer_12", 'description': quality + hgcallink }])

hgcallayout(dqmitems, "Noise - Layer 1: ADC Standard Deviation",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/Cassette_1/hex_stdadc_layer_1", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Noise - Layer 2: ADC Standard Deviation",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_2/Cassette_1/hex_stdadc_layer_2", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Noise - Layer 3: ADC Standard Deviation",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_3/Cassette_1/hex_stdadc_layer_3", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Noise - Layer 4: ADC Standard Deviation",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_4/Cassette_1/hex_stdadc_layer_4", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Noise - Layer 5: ADC Standard Deviation",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_5/Cassette_1/hex_stdadc_layer_5", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Noise - Layer 6: ADC Standard Deviation",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_6/Cassette_1/hex_stdadc_layer_6", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Noise - Layer 7: ADC Standard Deviation",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_7/Cassette_1/hex_stdadc_layer_7", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Noise - Layer 8: ADC Standard Deviation",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_8/Cassette_1/hex_stdadc_layer_8", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Noise - Layer 9: ADC Standard Deviation",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_9/Cassette_1/hex_stdadc_layer_9", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Noise - Layer 10: ADC Standard Deviation",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_10/Cassette_1/hex_stdadc_layer_10", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Noise - Layer 11: ADC Standard Deviation",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_11/Cassette_1/hex_stdadc_layer_11", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "Noise - Layer 12: ADC Standard Deviation",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_12/Cassette_1/hex_stdadc_layer_12", 'description': quality + hgcallink }])

#----------------------------------------------------------------------------------------------------
# Trigger Phase
#----------------------------------------------------------------------------------------------------
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ADC @ Layer 1",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/Cassette_1/Module_ML_F3WC_IH0197/seedadcvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ADC @ Layer 2",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_2/Cassette_1/Module_ML_F3WC_IH0196/seedadcvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ADC @ Layer 3",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_3/Cassette_1/Module_ML_F3WC_IH0198/seedadcvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ADC @ Layer 4",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_4/Cassette_1/Module_ML_F3WC_IH0190/seedadcvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ADC @ Layer 5",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_5/Cassette_1/Module_ML_F3WC_IH0192/seedadcvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ADC @ Layer 6",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_6/Cassette_1/Module_ML_F3WC_IH0191/seedadcvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ADC @ Layer 7",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_7/Cassette_1/Module_ML_F3WC_IH0195/seedadcvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ADC @ Layer 8",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_8/Cassette_1/Module_ML_F3WC_IH0193/seedadcvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ADC @ Layer 9",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_9/Cassette_1/Module_ML_F3WC_IH0181/seedadcvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ADC @ Layer 10",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_10/Cassette_1/Module_ML_F3WC_IH0182/seedadcvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ADC @ Layer 11",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_11/Cassette_1/Module_ML_F3WC_IH0194/seedadcvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ADC @ Layer 12",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_12/Cassette_1/Module_ML_F3WC_IH0183/seedadcvstrigtime", 'description': quality + hgcallink }])

hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ToA @ Layer 1",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/Cassette_1/Module_ML_F3WC_IH0197/seedtoavstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ToA @ Layer 2",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_2/Cassette_1/Module_ML_F3WC_IH0196/seedtoavstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ToA @ Layer 3",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_3/Cassette_1/Module_ML_F3WC_IH0198/seedtoavstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ToA @ Layer 4",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_4/Cassette_1/Module_ML_F3WC_IH0190/seedtoavstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ToA @ Layer 5",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_5/Cassette_1/Module_ML_F3WC_IH0192/seedtoavstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ToA @ Layer 6",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_6/Cassette_1/Module_ML_F3WC_IH0191/seedtoavstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ToA @ Layer 7",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_7/Cassette_1/Module_ML_F3WC_IH0195/seedtoavstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ToA @ Layer 8",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_8/Cassette_1/Module_ML_F3WC_IH0193/seedtoavstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ToA @ Layer 9",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_9/Cassette_1/Module_ML_F3WC_IH0181/seedtoavstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ToA @ Layer 10",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_10/Cassette_1/Module_ML_F3WC_IH0182/seedtoavstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ToA @ Layer 11",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_11/Cassette_1/Module_ML_F3WC_IH0194/seedtoavstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TrigPhase/Trigger Phase - ToA @ Layer 12",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_12/Cassette_1/Module_ML_F3WC_IH0183/seedtoavstrigtime", 'description': quality + hgcallink }])

#----------------------------------------------------------------------------------------------------
# ADC
#----------------------------------------------------------------------------------------------------
hgcallayout(dqmitems, "ADC/Average ADC @ Layer 1",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/Cassette_1/Module_ML_F3WC_IH0197/avgadc", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "ADC/Average ADC @ Layer 2",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_2/Cassette_1/Module_ML_F3WC_IH0196/avgadc", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "ADC/Average ADC @ Layer 3",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_3/Cassette_1/Module_ML_F3WC_IH0198/avgadc", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "ADC/Average ADC @ Layer 4",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_4/Cassette_1/Module_ML_F3WC_IH0190/avgadc", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "ADC/Average ADC @ Layer 5",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_5/Cassette_1/Module_ML_F3WC_IH0192/avgadc", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "ADC/Average ADC @ Layer 6",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_6/Cassette_1/Module_ML_F3WC_IH0191/avgadc", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "ADC/Average ADC @ Layer 7",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_7/Cassette_1/Module_ML_F3WC_IH0195/avgadc", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "ADC/Average ADC @ Layer 8",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_8/Cassette_1/Module_ML_F3WC_IH0193/avgadc", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "ADC/Average ADC @ Layer 9",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_9/Cassette_1/Module_ML_F3WC_IH0181/avgadc", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "ADC/Average ADC @ Layer 10",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_10/Cassette_1/Module_ML_F3WC_IH0182/avgadc", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "ADC/Average ADC @ Layer 11",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_11/Cassette_1/Module_ML_F3WC_IH0194/avgadc", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "ADC/Average ADC @ Layer 12",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_12/Cassette_1/Module_ML_F3WC_IH0183/avgadc", 'description': quality + hgcallink }])

#----------------------------------------------------------------------------------------------------
# TOT
#----------------------------------------------------------------------------------------------------
hgcallayout(dqmitems, "TOT/Average TOT @ Layer 1",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/Cassette_1/hex_avgtot_layer_1", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/Average TOT @ Layer 2",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_2/Cassette_1/hex_avgtot_layer_2", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/Average TOT @ Layer 3",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_3/Cassette_1/hex_avgtot_layer_3", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/Average TOT @ Layer 4",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_4/Cassette_1/hex_avgtot_layer_4", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/Average TOT @ Layer 5",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_5/Cassette_1/hex_avgtot_layer_5", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/Average TOT @ Layer 6",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_6/Cassette_1/hex_avgtot_layer_6", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/Average TOT @ Layer 7",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_7/Cassette_1/hex_avgtot_layer_7", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/Average TOT @ Layer 8",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_8/Cassette_1/hex_avgtot_layer_8", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/Average TOT @ Layer 9",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_9/Cassette_1/hex_avgtot_layer_9", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/Average TOT @ Layer 10",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_10/Cassette_1/hex_avgtot_layer_10", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/Average TOT @ Layer 11",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_11/Cassette_1/hex_avgtot_layer_11", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/Average TOT @ Layer 12",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_12/Cassette_1/hex_avgtot_layer_12", 'description': quality + hgcallink }])

hgcallayout(dqmitems, "TOT/TOT @ Layer 1",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/Cassette_1/Module_ML_F3WC_IH0197/tot", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/TOT @ Layer 2",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_2/Cassette_1/Module_ML_F3WC_IH0196/tot", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/TOT @ Layer 3",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_3/Cassette_1/Module_ML_F3WC_IH0198/tot", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/TOT @ Layer 4",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_4/Cassette_1/Module_ML_F3WC_IH0190/tot", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/TOT @ Layer 5",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_5/Cassette_1/Module_ML_F3WC_IH0192/tot", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/TOT @ Layer 6",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_6/Cassette_1/Module_ML_F3WC_IH0191/tot", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/TOT @ Layer 7",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_7/Cassette_1/Module_ML_F3WC_IH0195/tot", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/TOT @ Layer 8",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_8/Cassette_1/Module_ML_F3WC_IH0193/tot", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/TOT @ Layer 9",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_9/Cassette_1/Module_ML_F3WC_IH0181/tot", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/TOT @ Layer 10",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_10/Cassette_1/Module_ML_F3WC_IH0182/tot", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/TOT @ Layer 11",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_11/Cassette_1/Module_ML_F3WC_IH0194/tot", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOT/TOT @ Layer 12",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_12/Cassette_1/Module_ML_F3WC_IH0183/tot", 'description': quality + hgcallink }])

#----------------------------------------------------------------------------------------------------
# TOA
#----------------------------------------------------------------------------------------------------
hgcallayout(dqmitems, "TOA/Average TOA @ Layer 1",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/Cassette_1/hex_avgtoa_layer_1", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/Average TOA @ Layer 2",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_2/Cassette_1/hex_avgtoa_layer_2", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/Average TOA @ Layer 3",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_3/Cassette_1/hex_avgtoa_layer_3", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/Average TOA @ Layer 4",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_4/Cassette_1/hex_avgtoa_layer_4", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/Average TOA @ Layer 5",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_5/Cassette_1/hex_avgtoa_layer_5", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/Average TOA @ Layer 6",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_6/Cassette_1/hex_avgtoa_layer_6", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/Average TOA @ Layer 7",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_7/Cassette_1/hex_avgtoa_layer_7", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/Average TOA @ Layer 8",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_8/Cassette_1/hex_avgtoa_layer_8", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/Average TOA @ Layer 9",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_9/Cassette_1/hex_avgtoa_layer_9", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/Average TOA @ Layer 10",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_10/Cassette_1/hex_avgtoa_layer_10", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/Average TOA @ Layer 11",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_11/Cassette_1/hex_avgtoa_layer_11", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/Average TOA @ Layer 12",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_12/Cassette_1/hex_avgtoa_layer_12", 'description': quality + hgcallink }])

hgcallayout(dqmitems, "TOA/TOA @ Layer 1",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/Cassette_1/Module_ML_F3WC_IH0197/toa", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/TOA @ Layer 2",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_2/Cassette_1/Module_ML_F3WC_IH0196/toa", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/TOA @ Layer 3",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_3/Cassette_1/Module_ML_F3WC_IH0198/toa", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/TOA @ Layer 4",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_4/Cassette_1/Module_ML_F3WC_IH0190/toa", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/TOA @ Layer 5",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_5/Cassette_1/Module_ML_F3WC_IH0192/toa", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/TOA @ Layer 6",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_6/Cassette_1/Module_ML_F3WC_IH0191/toa", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/TOA @ Layer 7",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_7/Cassette_1/Module_ML_F3WC_IH0195/toa", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/TOA @ Layer 8",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_8/Cassette_1/Module_ML_F3WC_IH0193/toa", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/TOA @ Layer 9",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_9/Cassette_1/Module_ML_F3WC_IH0181/toa", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/TOA @ Layer 10",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_10/Cassette_1/Module_ML_F3WC_IH0182/toa", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/TOA @ Layer 11",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_11/Cassette_1/Module_ML_F3WC_IH0194/toa", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "TOA/TOA @ Layer 12",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_12/Cassette_1/Module_ML_F3WC_IH0183/toa", 'description': quality + hgcallink }])

#----------------------------------------------------------------------------------------------------
# RecHits
#----------------------------------------------------------------------------------------------------
hgcallayout(dqmitems, "RecHits/Layer 1: RecHit Energy vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/rechitenergyvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Layer 2: RecHit Energy vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_2/rechitenergyvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Layer 3: RecHit Energy vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_3/rechitenergyvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Layer 4: RecHit Energy vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_4/rechitenergyvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Layer 5: RecHit Energy vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_5/rechitenergyvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Layer 6: RecHit Energy vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_6/rechitenergyvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Layer 7: RecHit Energy vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_7/rechitenergyvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Layer 8: RecHit Energy vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_8/rechitenergyvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Layer 9: RecHit Energy vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_9/rechitenergyvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Layer 10: RecHit Energy vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_10/rechitenergyvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Layer 11: RecHit Energy vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_11/rechitenergyvstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Layer 12: RecHit Energy vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_12/rechitenergyvstrigtime", 'description': quality + hgcallink }])

hgcallayout(dqmitems, "RecHits/ Layer 1: RecHit Time vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/rechittimevstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/ Layer 2: RecHit Time vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_2/rechittimevstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/ Layer 3: RecHit Time vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_3/rechittimevstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/ Layer 4: RecHit Time vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_4/rechittimevstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/ Layer 5: RecHit Time vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_5/rechittimevstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/ Layer 6: RecHit Time vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_6/rechittimevstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/ Layer 7: RecHit Time vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_7/rechittimevstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/ Layer 8: RecHit Time vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_8/rechittimevstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/ Layer 9: RecHit Time vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_9/rechittimevstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/ Layer 10: RecHit Time vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_10/rechittimevstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/ Layer 11: RecHit Time vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_11/rechittimevstrigtime", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/ Layer 12: RecHit Time vs. TrigPhase",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_12/rechittimevstrigtime", 'description': quality + hgcallink }])

hgcallayout(dqmitems, "RecHits/Time vs. Energy @ Layer 1",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_1/rechittimevsenergy", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Time vs. Energy @ Layer 2",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_2/rechittimevsenergy", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Time vs. Energy @ Layer 3",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_3/rechittimevsenergy", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Time vs. Energy @ Layer 4",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_4/rechittimevsenergy", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Time vs. Energy @ Layer 5",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_5/rechittimevsenergy", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Time vs. Energy @ Layer 6",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_6/rechittimevsenergy", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Time vs. Energy @ Layer 7",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_7/rechittimevsenergy", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Time vs. Energy @ Layer 8",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_8/rechittimevsenergy", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Time vs. Energy @ Layer 9",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_9/rechittimevsenergy", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Time vs. Energy @ Layer 10",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_10/rechittimevsenergy", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Time vs. Energy @ Layer 11",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_11/rechittimevsenergy", 'description': quality + hgcallink }])
hgcallayout(dqmitems, "RecHits/Time vs. Energy @ Layer 12",
          [{ 'path': "HGCAL/EndCap_Minus/Layer_12/rechittimevsenergy", 'description': quality + hgcallink }])

