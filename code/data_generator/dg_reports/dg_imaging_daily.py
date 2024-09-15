### CS7810 Intro to Knowledge Engineering
### Fall 2024
### Project imaging daily data generator
### Jason H. Nolte, nolte14@wright.edu
### https://github.com/jasonolte/cs7810-123

import random


def get_mrn():
   mrn_high = 1000000
   mrn = random.randint(0, mrn_high)
   return mrn

def generate_imag_daily_report(patients, date, output_filename):
   TODO_var = "TODO"

   column_headers = ['Medical_Record_Number','Discharge_ID','Billing_Number','Discharge_Date','Imaging_Category','Imaging_Category_Title','Imaging_Procedure','Imaging_Procedure_Title','Imaging_Technique','Imaging_Technique_Title','Imaging_Service','Imaging_Service_Title','How_Image_Ordered','How_Image_Ordered_Title','Contrast_Media','Contrast_Media_Title','Route_Of_Contrast','Route_Of_Contrast_Title','Imaging_Charges','Adj_Imaging_Charges','Imaging_Units_Billed','DI_DOS_Code','Date_Of_Service','Day_Of_Service','Imaging_RCC_Bucket_Number','Imaging_Standardized_Unit_Cost']

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
      imag_cat = TODO_var
      imag_cat_title = TODO_var
      imag_proc = TODO_var
      imag_proc_title = TODO_var
      imag_technique = TODO_var
      imag_technique_title = TODO_var
      imag_serv = TODO_var
      imag_serv_title = TODO_var
      imag_how_order = TODO_var
      imag_how_order_title = TODO_var
      contrast_media = TODO_var
      contrast_media_title = TODO_var
      rte_of_contrast = TODO_var
      rte_of_contrast_title = TODO_var
      imag_charges = TODO_var
      adj_imag_charges = TODO_var
      imag_units_billed = TODO_var
      di_dos_code = TODO_var
      date_of_service = TODO_var
      day_of_service = TODO_var
      imag_rcc_bucket_no = TODO_var
      imag_stnd_unit_cost = TODO_var

      data_line = [mrn, dc_id, bill_no, dc_date, imag_cat, imag_cat_title, imag_proc, imag_proc_title, imag_technique, imag_technique_title, imag_serv, imag_serv_title, imag_how_order, imag_how_order_title, contrast_media, contrast_media_title, rte_of_contrast, rte_of_contrast_title, imag_charges, adj_imag_charges, imag_units_billed, di_dos_code, date_of_service, day_of_service, imag_rcc_bucket_no, imag_stnd_unit_cost]

      for data in data_line:
         file_text += data
         file_text += ','
      file_text += '\n'

   with open(output_filename, 'w') as output_file:
      output_file.write(file_text)


if __name__ == "__main__":
   date = "10SEP2024"
   output_filename = "imag_daily_" + date + ".csv"
   patients = ['patient1', 'patient2', 'patient3']
   generate_imag_daily_report(patients, date, output_filename)