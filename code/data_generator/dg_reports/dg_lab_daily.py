### CS7810 Intro to Knowledge Engineering
### Fall 2024
### Project lab daily data generator
### Jason H. Nolte, nolte14@wright.edu
### https://github.com/jasonolte/cs7810-123

import random


def get_mrn():
   mrn_high = 1000000
   mrn = random.randint(0, mrn_high)
   return mrn

def generate_lab_daily_report(patients, date, output_filename):
   TODO_var = "TODO"

   column_headers = ['Medical_Record_Number','Discharge_ID','Billing_Number','Discharge_Date','Lab_Area','Lab_Area_Title','Test_Category','Test_Category_Title','Lab_Test','Lab_Test_Title','How_Lab_Ordered','How_Lab_Ordered_Title','Panel_Indicator','Panel_Indicator_Title','Specimen_Source','Specimen_Source_Title','Lab_Charges','Adj_Lab_Charges','Lab_Units_Billed','DI_DOS_Code','Date_Of_Service','Day_Of_Service','Lab_RCC_Bucket_Number','Lab_Standardized_Unit_Cost']

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
      lab_area = TODO_var
      lab_area_title = TODO_var
      test_category = TODO_var
      test_category_title = TODO_var
      lab_test = TODO_var
      lab_test_title = TODO_var
      lab_how_order = TODO_var
      lab_how_order_title = TODO_var
      panel_indicator = TODO_var
      panel_indicator_title = TODO_var
      specimen_src = TODO_var
      specimen_src_title = TODO_var
      lab_charges = TODO_var
      adj_lab_charges = TODO_var
      lab_units_billed = TODO_var
      di_dos_code = TODO_var
      date_of_service = TODO_var
      day_of_service = TODO_var
      lab_rcc_bucket_no = TODO_var
      lab_stnd_unit_cost = TODO_var

      data_line = [mrn, dc_id, bill_no, dc_date, lab_area, lab_area_title, test_category, test_category_title, lab_test, lab_test_title, lab_how_order, lab_how_order_title, panel_indicator, panel_indicator_title, specimen_src, specimen_src_title, lab_charges, adj_lab_charges, lab_units_billed, di_dos_code, date_of_service, day_of_service, lab_rcc_bucket_no, lab_stnd_unit_cost]

      for data in data_line:
         file_text += data
         file_text += ','
      file_text += '\n'

   with open(output_filename, 'w') as output_file:
      output_file.write(file_text)


if __name__ == "__main__":
   date = "10SEP2024"
   output_filename = "lab_daily_" + date + ".csv"
   patients = ['patient1', 'patient2', 'patient3']
   generate_lab_daily_report(patients, date, output_filename)