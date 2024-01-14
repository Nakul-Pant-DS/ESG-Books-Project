import pandas as pd
import numpy as np


# Replace 'Sample_data_100.csv' with the actual path to your CSV file
file_path = 'E:/NewDrive/DataScienceProjects/DataSets/ESG Books/sample_data_100.csv'

# Read the CSV file into a DataFrame, skipping the first column
df_dict = pd.read_csv(file_path)
df_dict.drop(df_dict.columns[0], axis=1,inplace=True)


# Replace NaN values only in specific columns with the mean of each column
columns_to_fill = ['em_60000','em_60100','em_60200','em_60300','em_60400','em_60500','em_60600','em_60700','em_60800','em_60900','em_61000','em_61100','em_61200','em_61300','em_61400',
'em_61500','em_61600','em_61700','em_61800'] 
# Replace with your actual column names
df_dict[columns_to_fill] = df_dict[columns_to_fill].apply(lambda col: col.fillna(col.mean()))



# Cleaning ISIN values
df_dict['isin'] = df_dict['isin'].str.strip()  # Remove leading and trailing whitespaces
df_dict['isin'] = df_dict['isin'].str.upper()  # Convert to uppercase

# Validate ISIN format (assuming a simple check for illustrative purposes)
def is_valid_isin(isin):
    # Check if the length is 12 characters
    if len(isin) != 12:
        return False
    
    # Check if the first two characters are letters
    if not isin[:2].isalpha():
        return False
    
    # Check if the next nine characters are alphanumeric
    if not isin[2:11].isalnum():
        return False
    
    # Check if the last character is a check digit (either a digit or 'X')
    if not (isin[11].isdigit() or isin[11] == 'X'):
        return False
    
    return True

# Apply the validation function and filter out invalid ISINs
df_dict[df_dict['isin'].apply(is_valid_isin)]


# Define a function to extract country code from ISIN
def extract_country_code(isin):
    return isin[:2]

# Apply the function to create a new column 'CountryCode'
df_dict['CountryCode'] = df_dict['isin'].apply(extract_country_code)

# Create a dictionary mapping country codes to country names
country_mapping = {
'AF':	'AFGHANISTAN',
'AX':	'ÅLAND ISLANDS',
'AL':	'ALBANIA',
'DZ':	'ALGERIA',
'AS':	'AMERICAN SAMOA',
'AD':	'ANDORRA',
'AO':	'ANGOLA',
'AI':	'ANGUILLA',
'AQ':	'ANTARCTICA',
'AG':	'ANTIGUA AND BARBUDA',
'AR':	'ARGENTINA',
'AM':	'ARMENIA',
'AW':	'ARUBA',
'AU':	'AUSTRALIA',
'AT':	'AUSTRIA',
'AZ':	'AZERBAIJAN',
'BS':	'BAHAMAS',
'BH':	'BAHRAIN',
'BD':	'BANGLADESH',
'BB':	'BARBADOS',
'BY':	'BELARUS',
'BE':	'BELGIUM',
'BZ':	'BELIZE',
'BJ':	'BENIN',
'BM':	'BERMUDA',
'BT':	'BHUTAN',
'BO':	'BOLIVIA, PLURINATIONAL STATE OF',
'BQ':	'BONAIRE, SINT EUSTATIUS AND SABA',
'BA':	'BOSNIA AND HERZEGOVINA',
'BW':	'BOTSWANA',
'BV':	'BOUVET ISLAND',
'BR':	'BRAZIL',
'IO':	'BRITISH INDIAN OCEAN TERRITORY',
'BN':	'BRUNEI DARUSSALAM',
'BG':	'BULGARIA',
'BF':	'BURKINA FASO',
'BI':	'BURUNDI',
'KH':	'CAMBODIA',
'CM':	'CAMEROON',
'CA':	'CANADA',
'CV':	'CAPE VERDE',
'KY':	'CAYMAN ISLANDS',
'CF':	'CENTRAL AFRICAN REPUBLIC',
'TD':	'CHAD',
'CL':	'CHILE',
'CN':	'CHINA',
'CX':	'CHRISTMAS ISLAND',
'CC':	'COCOS (KEELING) ISLANDS',
'CO':	'COLOMBIA',
'KM':	'COMOROS',
'CG':	'CONGO',
'CD':	'CONGO, THE DEMOCRATIC REPUBLIC OF THE',
'CK':	'COOK ISLANDS',
'CR':	'COSTA RICA',
'CI':	'CÔTE D’IVOIRE',
'HR':	'CROATIA',
'CU':	'CUBA',
'CW':	'CURAÇAO',
'CY':	'CYPRUS',
'CZ':	'CZECH REPUBLIC',
'DK':	'DENMARK',
'DJ':	'DJIBOUTI',
'DM':	'DOMINICA',
'DO':	'DOMINICAN REPUBLIC',
'EC':	'ECUADOR',
'EG':	'EGYPT',
'SV':	'EL SALVADOR',
'GQ':	'EQUATORIAL GUINEA',
'ER':	'ERITREA',
'EE':	'ESTONIA',
'ET':	'ETHIOPIA',
'FK':	'FALKLAND ISLANDS (MALVINAS)',
'FO':	'FAROE ISLANDS',
'FJ':	'FIJI',
'FI':	'FINLAND',
'FR':	'FRANCE',
'GF':	'FRENCH GUIANA',
'PF':	'FRENCH POLYNESIA',
'TF':	'FRENCH SOUTHERN TERRITORIES',
'GA':	'GABON',
'GM':	'GAMBIA',
'GE':	'GEORGIA',
'DE':	'GERMANY',
'GH':	'GHANA',
'GI':	'GIBRALTAR',
'GR':	'GREECE',
'GL':	'GREENLAND',
'GD':	'GRENADA',
'GP':	'GUADELOUPE',
'GU':	'GUAM',
'GT':	'GUATEMALA',
'GG':	'GUERNSEY',
'GN':	'GUINEA',
'GW':	'GUINEA-BISSAU',
'GY':	'GUYANA',
'HT':	'HAITI',
'HM':	'HEARD ISLAND AND MCDONALD ISLANDS',
'VA':	'HOLY SEE (VATICAN CITY STATE)',
'HN':	'HONDURAS',
'HK':	'HONG KONG',
'HU':	'HUNGARY',
'IS':	'ICELAND',
'IN':	'INDIA',
'ID':	'INDONESIA',
'IR':	'IRAN, ISLAMIC REPUBLIC OF',
'IQ':	'IRAQ',
'IE':	'IRELAND',
'IM':	'ISLE OF MAN',
'IL':	'ISRAEL',
'IT':	'ITALY',
'JM':	'JAMAICA',
'JP':	'JAPAN',
'JE':	'JERSEY',
'JO':	'JORDAN',
'KZ':	'KAZAKHSTAN',
'KE':	'KENYA',
'KI':	'KIRIBATI',
'KP':	'KOREA, DEMOCRATIC PEOPLE’S REPUBLIC OF',
'KR':	'KOREA, REPUBLIC OF',
'KW':	'KUWAIT',
'KG':	'KYRGYZSTAN',
'LA':	'LAO PEOPLE’S DEMOCRATIC REPUBLIC',
'LV':	'LATVIA',
'LB':	'LEBANON',
'LS':	'LESOTHO',
'LR':	'LIBERIA',
'LY':	'LIBYA',
'LI':	'LIECHTENSTEIN',
'LT':	'LITHUANIA',
'LU':	'LUXEMBOURG',
'MO':	'MACAO',
'MK':	'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF',
'MG':	'MADAGASCAR',
'MW':	'MALAWI',
'MY':	'MALAYSIA',
'MV':	'MALDIVES',
'ML':	'MALI',
'MT':	'MALTA',
'MH':	'MARSHALL ISLANDS',
'MQ':	'MARTINIQUE',
'MR':	'MAURITANIA',
'MU':	'MAURITIUS',
'YT':	'MAYOTTE',
'MX':	'MEXICO',
'FM':	'MICRONESIA, FEDERATED STATES OF',
'MD':	'MOLDOVA, REPUBLIC OF',
'MC':	'MONACO',
'MN':	'MONGOLIA',
'ME':	'MONTENEGRO',
'MS':	'MONTSERRAT',
'MA':	'MOROCCO',
'MZ':	'MOZAMBIQUE',
'MM':	'MYANMAR',
'NA':	'NAMIBIA',
'NR':	'NAURU',
'NP':	'NEPAL',
'NL':	'NETHERLANDS',
'NC':	'NEW CALEDONIA',
'NZ':	'NEW ZEALAND',
'NI':	'NICARAGUA',
'NE':	'NIGER',
'NG':	'NIGERIA',
'NU':	'NIUE',
'NF':	'NORFOLK ISLAND',
'MP':	'NORTHERN MARIANA ISLANDS',
'NO':	'NORWAY',
'OM':	'OMAN',
'PK':	'PAKISTAN',
'PW':	'PALAU',
'PS':	'PALESTINIAN TERRITORY, OCCUPIED',
'PA':	'PANAMA',
'PG':	'PAPUA NEW GUINEA',
'PY':	'PARAGUAY',
'PE':	'PERU',
'PH':	'PHILIPPINES',
'PN':	'PITCAIRN',
'PL':	'POLAND',
'PT':	'PORTUGAL',
'PR':	'PUERTO RICO',
'QA':	'QATAR',
'RE':	'RÉUNION',
'RO':	'ROMANIA',
'RU':	'RUSSIAN FEDERATION',
'RW':	'RWANDA',
'BL':	'SAINT BARTHÉLEMY',
'SH':	'SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA',
'KN':	'SAINT KITTS AND NEVIS',
'LC':	'SAINT LUCIA',
'MF':	'SAINT MARTIN (FRENCH PART)',
'PM':	'SAINT PIERRE AND MIQUELON',
'VC':	'SAINT VINCENT AND THE GRENADINES',
'WS':	'SAMOA',
'SM':	'SAN MARINO',
'ST':	'SAO TOME AND PRINCIPE',
'SA':	'SAUDI ARABIA',
'SN':	'SENEGAL',
'RS':	'SERBIA',
'SC':	'SEYCHELLES',
'SL':	'SIERRA LEONE',
'SG':	'SINGAPORE',
'SX':	'SINT MAARTEN (DUTCH PART)',
'SK':	'SLOVAKIA',
'SI':	'SLOVENIA',
'SB':	'SOLOMON ISLANDS',
'SO':	'SOMALIA',
'ZA':	'SOUTH AFRICA',
'GS':	'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS',
'SS':	'SOUTH SUDAN',
'ES':	'SPAIN',
'LK':	'SRI LANKA',
'SD':	'SUDAN',
'SR':	'SURINAME',
'SJ':	'SVALBARD AND JAN MAYEN',
'SZ':	'SWAZILAND',
'SE':	'SWEDEN',
'CH':	'SWITZERLAND',
'SY':	'SYRIAN ARAB REPUBLIC',
'TW':	'TAIWAN, PROVINCE OF CHINA',
'TJ':	'TAJIKISTAN',
'TZ':	'TANZANIA, UNITED REPUBLIC OF',
'TH':	'THAILAND',
'TL':	'TIMOR-LESTE',
'TG':	'TOGO',
'TK':	'TOKELAU',
'TO':	'TONGA',
'TT':	'TRINIDAD AND TOBAGO',
'TN':	'TUNISIA',
'TR':	'TURKEY',
'TM':	'TURKMENISTAN',
'TC':	'TURKS AND CAICOS ISLANDS',
'TV':	'TUVALU',
'UG':	'UGANDA',
'UA':	'UKRAINE',
'AE':	'UNITED ARAB EMIRATES',
'GB':	'UNITED KINGDOM',
'US':	'UNITED STATES',
'UM':	'UNITED STATES MINOR OUTLYING ISLANDS',
'UY':	'URUGUAY',
'UZ':	'UZBEKISTAN',
'VU':	'VANUATU',
'VE':	'VENEZUELA, BOLIVARIAN REPUBLIC OF',
'VN':	'VIET NAM',
'VG':	'VIRGIN ISLANDS, BRITISH',
'VI':	'VIRGIN ISLANDS, U.S.',
'WF':	'WALLIS AND FUTUNA',
'EH':	'WESTERN SAHARA',
'YE':	'YEMEN',
'ZM':	'ZAMBIA',
'ZW':	'ZIMBABWE'
}

# Map country codes to country names and create a new column 'CountryName'
df_dict['CountryName'] = df_dict['CountryCode'].map(country_mapping)

df_dict['CountryName'] = df_dict['CountryName'].astype(str)


# Conversion factors od emission data
conversion_factor_kg_to_tonnes = 0.001 # Convert kilograms to metric tons
float_to_int = ['em_60000','em_60100','em_60200','em_60300','em_60400','em_60500','em_60600','em_60700','em_60800','em_60900','em_61000','em_61100','em_61200','em_61300','em_61400',
'em_61500','em_61600','em_61700','em_61800']
# Apply conversion factors to all columns
df_dict[float_to_int] = df_dict[float_to_int].apply(lambda x: x * conversion_factor_kg_to_tonnes)



# Converting data to int
float_to_int = ['em_60000','em_60100','em_60200','em_60300','em_60400','em_60500','em_60600','em_60700','em_60800','em_60900','em_61000','em_61100','em_61200','em_61300','em_61400',
'em_61500','em_61600','em_61700','em_61800']
df_dict[float_to_int] = df_dict[float_to_int].astype(int) # Convert to int if not already



# Drop Unnecessary columns created during data cleaning process
columns_to_drop = ['CountryCode']
df_dict.drop(columns=columns_to_drop, inplace=True)


# Relacing column names in sample data from their corresponding values in description files 
replace_column_names = {
'em_60000':	'Scope 1',
'em_60100':	'Scope 2 (location based)',
'em_60200':	'Scope 2 (market based)',
'em_60300':	'Scope 3 (total)',
'em_60400':	'Scope 3 (cat 1)',
'em_60500':	'Scope 3 (cat 2)',
'em_60600':	'Scope 3 (cat 3)',
'em_60700':	'Scope 3 (cat 4)',
'em_60800':	'Scope 3 (cat 5)',
'em_60900':	'Scope 3 (cat 6)',
'em_61000':	'Scope 3 (cat 7)',
'em_61100':	'Scope 3 (cat 8)',
'em_61200':	'Scope 3 (cat 9)',
'em_61300':	'Scope 3 (cat 10)',
'em_61400':	'Scope 3 (cat 11)',
'em_61500':	'Scope 3 (cat 12)',
'em_61600':	'Scope 3 (cat 13)',
'em_61700':	'Scope 3 (cat 14)',
'em_61800':	'Scope 3 (cat 15)',
}
# Rename columns
df_dict.rename(columns=replace_column_names, inplace=True)


df_dict.to_csv('E:/NewDrive/DataScienceProjects/DataSets/ESG Books/Solutions/Cleaned_DataSet.csv', index=False)

