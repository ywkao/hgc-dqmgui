def hgcallayout(i, p, *rows): i["HGCAL/Layouts/" + p] = DQMItem(layout=rows)

########### define varialbles for frequently used strings #############
hgcallink = "   >>> <a href=https://hgcaldocs.web.cern.ch/RawDataHandling/dqm_sysval/>Description</a>"
quality = "summary of module status"
summary = "wafer map for hgcal"
digis = "digis information"

tb_modules = [
    'ML_F3WC_IH0197', 'ML_F3WC_IH0196', 'ML_F3WC_IH0198', 'ML_F3WC_IH0190',
    'ML_F3WC_IH0192', 'ML_F3WC_IH0191', 'ML_F3WC_IH0194', 'ML_F3WC_IH0182',
    'ML_F3WC_IH0180', 'ML_F3WC_IH0199', 'ML_NA',          'ML_NA'
]

################### Links to TOP Summary Histograms #################################
for i in range(12):
    layer = i+1
    hgcallayout(dqmitems, f"Layer {layer}: Average ADC",
          [{ 'path':  f"HGCAL/EndCap_Minus/Layer_{layer}/Cassette_1/hex_avgadc_layer_{layer}", 'description': quality + hgcallink }])

    hgcallayout(dqmitems, f"Noise - Layer {layer}: ADC Standard Deviation",
          [{ 'path':  f"HGCAL/EndCap_Minus/Layer_{layer}/Cassette_1/hex_stdadc_layer_{layer}", 'description': quality + hgcallink }])

#----------------------------------------------------------------------------------------------------
# Trigger Phase
#----------------------------------------------------------------------------------------------------
for i in range(12):
    layer = i+1
    hgcallayout(dqmitems, f"TrigPhase/Trigger Phase - ADC @ Layer {layer}",
          [{ 'path':  f"HGCAL/EndCap_Minus/Layer_{layer}/Cassette_1/Module_{tb_modules[i]}/seedadcvstrigtime", 'description': quality + hgcallink }])

for i in range(12):
    layer = i+1
    hgcallayout(dqmitems,  f"TrigPhase/Trigger Phase - ToA @ Layer {layer}",
                [{ 'path': f"HGCAL/EndCap_Minus/Layer_{layer}/Cassette_1/Module_{tb_modules[i]}/seedtoavstrigtime", 'description': quality + hgcallink }])

#----------------------------------------------------------------------------------------------------
# ADC
#----------------------------------------------------------------------------------------------------
for i in range(12):
    layer = i+1
    hgcallayout(dqmitems, f"ADC/Average ADC @ Layer {layer}",
                [{ 'path': f"HGCAL/EndCap_Minus/Layer_{layer}/Cassette_1/Module_{tb_modules[i]}/avgadc", 'description': quality + hgcallink }])

#----------------------------------------------------------------------------------------------------
# TOT
#----------------------------------------------------------------------------------------------------
for i in range(12):
    layer = i+1
    hgcallayout(dqmitems, f"TOT/Average TOT @ Layer {layer}",
          [{ 'path':  f"HGCAL/EndCap_Minus/Layer_{layer}/Cassette_1/hex_avgtot_layer_{layer}", 'description': quality + hgcallink }])

for i in range(12):
    layer = i+1
    hgcallayout(dqmitems, f"TOT/TOT @ Layer {layer}",
          [{ 'path': f"HGCAL/EndCap_Minus/Layer_{layer}/Cassette_1/Module_{tb_modules[i]}/tot", 'description': quality + hgcallink }])

#----------------------------------------------------------------------------------------------------
# TOA
#----------------------------------------------------------------------------------------------------
for i in range(12):
    layer = i+1
    hgcallayout(dqmitems, f"TOA/Average TOA @ Layer {layer}",
          [{ 'path':  f"HGCAL/EndCap_Minus/Layer_{layer}/Cassette_1/hex_avgtoa_layer_{layer}", 'description': quality + hgcallink }])

for i in range(12):
    layer = i+1
    hgcallayout(dqmitems, f"TOA/TOA @ Layer {layer}",
                [{ 'path': f"HGCAL/EndCap_Minus/Layer_{layer}/Cassette_1/Module_{tb_modules[i]}/toa", 'description': quality + hgcallink }])

#----------------------------------------------------------------------------------------------------
# RecHits
#----------------------------------------------------------------------------------------------------
for i in range(12):
    layer = i+1
    hgcallayout(dqmitems, f"RecHits/Layer {layer}: RecHit Energy vs. TrigPhase",
          [{ 'path':  f"HGCAL/EndCap_Minus/Layer_{layer}/rechitenergyvstrigtime", 'description': quality + hgcallink }])

    hgcallayout(dqmitems, f"RecHits/ Layer {layer}: RecHit Time vs. TrigPhase",
          [{ 'path':  f"HGCAL/EndCap_Minus/Layer_{layer}/rechittimevstrigtime", 'description': quality + hgcallink }])

    hgcallayout(dqmitems, f"RecHits/Time vs. Energy @ Layer {layer}",
          [{ 'path':  f"HGCAL/EndCap_Minus/Layer_{layer}/rechittimevsenergy", 'description': quality + hgcallink }])
