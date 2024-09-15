### CS7810 Intro to Knowledge Engineering
### Fall 2024
### Project supply daily data generator
### Jason H. Nolte, nolte14@wright.edu
### https://github.com/jasonolte/cs7810-123

import random


def get_mrn():
   mrn_high = 1000000
   mrn = random.randint(0, mrn_high)
   return mrn

def generate_supp_daily_report(patients, date, output_filename):
   TODO_var = "TODO"

   column_headers = ['Medical_Record_Number','Discharge_ID','Billing_Number','Discharge_Date','Supply_Category','Supply_Category_Title','Supply_Item','Supply_Item_Title','Delivery_Method','Delivery_Method_Title','Supply_Charges','Adj_Supply_Charges','Supply_Units_Billed','DI_DOS_Code','Date_Of_Service','Day_Of_Service','Supply_RCC_Bucket_Number','Supply_Standardized_Unit_Cost']

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
      supp_cat = TODO_var
      supp_cat_title = TODO_var
      supp_item = TODO_var
      supp_item_title = TODO_var
      delivery_method = TODO_var
      delivery_method_title = TODO_var
      supp_charges = TODO_var
      adj_supp_charges = TODO_var
      supp_units_billed = TODO_var
      di_dos_code = TODO_var
      date_of_service = TODO_var
      day_of_service = TODO_var
      supp_rcc_bucket_no = TODO_var
      supp_stnd_unit_cost = TODO_var

      data_line = [mrn, dc_id, bill_no, dc_date, supp_cat, supp_cat_title, supp_item, supp_item_title, delivery_method, delivery_method_title, supp_charges, adj_supp_charges, supp_units_billed, di_dos_code, date_of_service, day_of_service, supp_rcc_bucket_no, supp_stnd_unit_cost]

      for data in data_line:
         file_text += data
         file_text += ','
      file_text += '\n'

   with open(output_filename, 'w') as output_file:
      output_file.write(file_text)


if __name__ == "__main__":
   date = "10SEP2024"
   output_filename = "supply_daily_" + date + ".csv"
   patients = ['patient1', 'patient2', 'patient3']
   generate_supp_daily_report(patients, date, output_filename)