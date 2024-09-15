### CS7810 Intro to Knowledge Engineering
### Fall 2024
### Project clinical daily data generator
### Jason H. Nolte, nolte14@wright.edu
### https://github.com/jasonolte/cs7810-123

import random


def get_mrn():
   mrn_high = 1000000
   mrn = random.randint(0, mrn_high)
   return mrn

def generate_clin_daily_report(patients, date, output_filename):
   TODO_var = "TODO"

   column_headers = ['Medical_Record_Number','Discharge_ID','Billing_Number','Discharge_Date','Clinical_Area','Clinical_Area_Title','Clinical_Service','Clinical_Service_Title','Clinical_Labor_Component','Clinical_Labor_Component_Title','Clinical_Charge_Method','Clinical_Charge_Method_Title','Clinical_Charges','Adj_Clinical_Charges','Clinical_Units_Billed','DI_DOS_Code','Date_Of_Service','Day_Of_Service','Clinical_RCC_Bucket_Number','Clinical_Standardized_Unit_Cost']

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
      clin_area = TODO_var
      clin_area_title = TODO_var
      clin_serv = TODO_var
      clin_serv_title = TODO_var
      clin_labor_comp = TODO_var
      clin_labor_comp_title = TODO_var
      clin_charg_method = TODO_var
      clin_charg_method_title = TODO_var
      clin_charges = TODO_var
      adj_clin_charges = TODO_var
      clin_units_billed = TODO_var
      di_dos_code = TODO_var
      date_of_service = TODO_var
      day_of_service = TODO_var
      clin_rcc_bucket_no = TODO_var
      clin_stnd_unit_cost = TODO_var

      data_line = [mrn, dc_id, bill_no, dc_date, clin_area, clin_area_title, clin_serv, clin_serv_title, clin_labor_comp, clin_labor_comp_title, clin_charg_method, clin_charg_method_title, clin_charges, adj_clin_charges, clin_units_billed, di_dos_code, date_of_service, day_of_service, clin_rcc_bucket_no, clin_stnd_unit_cost]

      for data in data_line:
         file_text += data
         file_text += ','
      file_text += '\n'

   with open(output_filename, 'w') as output_file:
      output_file.write(file_text)


if __name__ == "__main__":
   date = "10SEP2024"
   output_filename = "clin_daily_" + date + ".csv"
   patients = ['patient1', 'patient2', 'patient3']
   generate_clin_daily_report(patients, date, output_filename)