### CS7810 Intro to Knowledge Engineering
### Fall 2024
### Project other daily data generator
### Jason H. Nolte, nolte14@wright.edu
### https://github.com/jasonolte/cs7810-123

import random


def get_mrn():
   mrn_high = 1000000
   mrn = random.randint(0, mrn_high)
   return mrn

def generate_other_daily_report(patients, date, output_filename):
   TODO_var = "TODO"

   column_headers = ['Medical_Record_Number','Discharge_ID','Billing_Number','Discharge_Date','Other_Category','Other_Category_Title','Other_Service','Other_Service_Title','Charge_Method','Charge_Method_Title','Other_Charges','Adj_Other_Charges','Other_Units_Billed','DI_DOS_Code','Date_Of_Service','Day_Of_Service','Other_RCC_Bucket_Number','Other_Standardized_Unit_Cost']

   file_text = ""
   for header in column_headers:
      file_text += header
      file_text += ','

   file_text += '\n'
   
   for patient in patients:
      mrn = str(get_mrn())
      dc_id = TODO_var
      bill_no = TODO_var
      dc_date = TODO_var
      other_cat = TODO_var
      other_cat_title = TODO_var
      other_serv = TODO_var
      other_serv_title = TODO_var
      charge_method = TODO_var
      charge_method_title = TODO_var
      other_charges = TODO_var
      adj_other_charges = TODO_var
      other_units_billed = TODO_var
      di_dos_code = TODO_var
      date_of_service = TODO_var
      day_of_service = TODO_var
      other_rcc_bucket_no = TODO_var
      other_stnd_unit_cost = TODO_var

      data_line = [mrn, dc_id, bill_no, dc_date, other_cat, other_cat_title, other_serv, other_serv_title, charge_method, charge_method_title, other_charges, adj_other_charges, other_units_billed, di_dos_code, date_of_service, day_of_service, other_rcc_bucket_no, other_stnd_unit_cost]

      for data in data_line:
         file_text += data
         file_text += ','
      file_text += '\n'

   with open(output_filename, 'w') as output_file:
      output_file.write(file_text)


if __name__ == "__main__":
   date = "10SEP2024"
   output_filename = "other_daily_" + date + ".csv"
   patients = ['patient1', 'patient2', 'patient3']
   generate_other_daily_report(patients, date, output_filename)