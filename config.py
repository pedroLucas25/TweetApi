import pymysql.cursors

class Config:
    
    #*************
    #DATABSE SETUP
    #*************
    local_db_host=''
    local_db=''
    local_db_user=''
    local_db_password=''
    
    development_db_host=''
    development_db=''
    development_db_user=''
    development_db_password=''
    
    homolog_db_host=''
    homolog_db=''
    homolog_db_user=''
    homolog_db_password=''
    
    production_db_host=''
    production_db=''
    production_db_user=''
    production_db_password=''

    cursorclass=pymysql.cursors.DictCursor
    charset='utf8mb4'
    autocommit=True

    #***********
    #EMAIL SETUP
    #***********
    local_email_identifier = ''
    local_email_base_url = ''
    local_email_base_url_adm = ''
    local_email_sender = ''
    local_email_password = ''

    development_email_identifier = ''
    development_email_base_url = ''
    development_email_base_url_adm = ''
    development_email_sender = ''
    development_email_password = ''        
    
    homolog_email_identifier = ''
    homolog_email_base_url = ''
    homolog_email_base_url_adm = ''
    homolog_email_sender = ''
    homolog_email_password= '' 

    production_email_identifier = ''
    production_email_base_url = ''
    production_email_base_url_adm = ''
    production_email_sender = ''
    production_email_password= ''

    #************************
    #InfoData
    #************************
    infodata_url_active = False
    local_infodata_url = 'http://127.0.0.1:5399/'
    development_infodata_url = ''
    homolog_infodata_url = ''
    production_infodata_url = ''