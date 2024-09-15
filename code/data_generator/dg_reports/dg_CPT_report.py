### CS7810 Intro to Knowledge Engineering
### Fall 2024
### Project CPT data generator
### Jason H. Nolte, nolte14@wright.edu
### https://github.com/jasonolte/cs7810-123

import random


def get_mrn():
   mrn_high = 1000000
   mrn = random.randint(0, mrn_high)
   return mrn

def generate_cpt_report(patients, output_filename):
   TODO_var = "TODO"

   column_headers = ['Medical_Record_Number','Billing_Number','Discharge_Date','Discharge_ID','CPT_Number','CPT_Code','CPT_Title','CPT_Modifier_1','CPT_Modifier_1_Title','CPT_Modifier_2','CPT_Modifier_2_Title','CPT_Modifier_3','CPT_Modifier_3_Title','CPT_Modifier_4','CPT_Modifier_4_Title']

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
      cpt_no = TODO_var
      cpt_code = TODO_var
      cpt_title = TODO_var
      cpt_mod_1 = TODO_var
      cpt_mod_1_title = TODO_var
      cpt_mod_2 = TODO_var
      cpt_mod_2_title = TODO_var
      cpt_mod_3 = TODO_var
      cpt_mod_3_title = TODO_var
      cpt_mod_4 = TODO_var
      cpt_mod_4_title = TODO_var

      data_line = [mrn, bill_no, dc_date, dc_id, cpt_no, cpt_code, cpt_title, cpt_mod_1, cpt_mod_1_title, cpt_mod_2, cpt_mod_2_title, cpt_mod_3, cpt_mod_3_title, cpt_mod_4, cpt_mod_4_title]

      for data in data_line:
         file_text += data
         file_text += ','
      file_text += '\n'

   with open(output_filename, 'w') as output_file:
      output_file.write(file_text)


if __name__ == "__main__":
   date = "10SEP2024"
   output_filename = "cpt_report_" + date + ".csv"
   patients = ['patient1', 'patient2', 'patient3']
   generate_cpt_report(patients, output_filename)