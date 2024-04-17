import pandas as pd

# Translating the columns for ease of analysis
crosswalk = {'Nome TI': 'Name of Indigenous Territory (TI)',
             'Nome Povo': 'Name of Indigenous People',
             'fase_ti': 'Phase of Demarcation',
             'Reestudo': 'Re-study',
             'municipio_TI': 'TI Municipality',
             'uf_TI': 'TI State',
             'Area_TI': 'Territory Area (mi^2)',
             'Nome fazenda': 'Farm Name',
             'NM_MUN': 'Municipality of Farm',
             'Area Sobreposta Total': 'Total Overlapping Area (mi^2)',
             '%do total sobreposto': 'Percent of Total Overlap on TI Area',
             'Proprietario (SNCR 2021)': 'Owner (SNCR 2021)',
             'Area_do_Imovel': 'Property Area (mi^2)',
             'parc_cert': 'Parcel Certificate (No.)',
             'cod_imovel': 'Property Code',
             'Area_pasto': 'Pasture Area (mi^2)',
             'Area_Silvicultura': 'Forestry Area (mi^2)',
             'Area_Cana': 'Sugarcane Area (mi^2)',
             'Area_Mineração': 'Mining Area (mi^2)',
             'Area_soja': 'Soybean Area (mi^2)',
             'Area_Outras_Lav_Temp': 'Area of Other Temporary Crops (mi^2)',
             'Cafe': 'Coffee (mi^2)',
             'Citrus': 'Citrus Fruits (mi^2)',
             'Outras_Lav_Perene': 'Other Perennial Crops (mi^2)',
             'SIGLA': 'State',  # 24
             'NM_REGIAO': 'Region',
             'CD_MUN': 'Municipal Code',
             'Area_mun_h': 'Area of Municipality (mi^2)'
             }

dict_of_dict = {'old_column': list(crosswalk.keys()),
                'new_column': list(crosswalk.values())}

crosswalk_df = pd.DataFrame(dict_of_dict)
crosswalk_df.to_csv('crosswalk.csv', index=False, header=True)
