### CS7810 Intro to Knowledge Engineering
### Fall 2024
### Project pharmacy daily data generator
### Jason H. Nolte, nolte14@wright.edu
### https://github.com/jasonolte/cs7810-123

import random


def get_mrn():
   mrn_high = 1000000
   mrn = random.randint(0, mrn_high)
   return mrn

def generate_pharm_daily_report(patients, date, output_filename):
   TODO_var = "TODO"

   column_headers = ['Medical_Record_Number', 'Discharge_ID', 'Billing_Number', 'Discharge_Date', 'Drug_Class', 'Drug_Class_Title', 'Therapeutic_Category', 'Therapeutic_Category_Title', 'Generic_Drug', 'Generic_Drug_Title', 'Route_Of_Administration', 'Route_Of_Administration_Title', 'Dosage_Form', 'Dosage_Form_Title', 'Dosage_Strength', 'Dosage_Strength_Title', 'Unit_Of_Measure', 'Unit_Of_Measure_Title', 'Pharmacy_Charges', 'Adj_Pharmacy_Charges', 'Pharm_Units_Billed', 'DI_DOS_Code', 'Date_Of_Service', 'Day_Of_Service', 'Pharmacy_RCC_Bucket_Number', 'Pharmacy_Standardized_Unit_Cost']

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
      drug_class = TODO_var
      drug_class_title = TODO_var
      therap_cat = TODO_var
      therap_cat_title = TODO_var
      gen_drug = TODO_var
      gen_drug_title = TODO_var
      route_of_admin = TODO_var
      route_of_admin_title = TODO_var
      dos_form = TODO_var
      dos_form_title = TODO_var
      dos_str = TODO_var
      dos_str_title = TODO_var
      unit_of_meas = TODO_var
      unit_of_meas_title = TODO_var
      pharm_charges = TODO_var
      adj_pharm_charges = TODO_var
      pharm_units_billed = TODO_var
      di_dos_code = TODO_var
      date_of_service = TODO_var
      day_of_service = TODO_var
      pharm_rcc_bucket_no = TODO_var
      pharm_stnd_unit_cost = TODO_var

      data_line = [mrn, dc_id, bill_no, dc_date, drug_class, drug_class_title, therap_cat, therap_cat_title, gen_drug, gen_drug_title, route_of_admin, route_of_admin_title, dos_form, dos_form_title, dos_str, dos_str_title, unit_of_meas, unit_of_meas_title, pharm_charges, adj_pharm_charges, pharm_units_billed, di_dos_code, date_of_service, day_of_service, pharm_rcc_bucket_no, pharm_stnd_unit_cost]

      for data in data_line:
         file_text += data
         file_text += ','
      file_text += '\n'

   with open(output_filename, 'w') as output_file:
      output_file.write(file_text)


if __name__ == "__main__":
   date = "10SEP2024"
   output_filename = "pharm_daily_" + date + ".csv"
   patients = ['patient1', 'patient2', 'patient3']
   generate_pharm_daily_report(patients, date, output_filename)