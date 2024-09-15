### CS7810 Intro to Knowledge Engineering
### Fall 2024
### Project diagnosis data generator
### Jason H. Nolte, nolte14@wright.edu
### https://github.com/jasonolte/cs7810-123

import random


def get_mrn():
   mrn_high = 1000000
   mrn = random.randint(0, mrn_high)
   return mrn

def generate_diag_report(patients, output_filename):
   TODO_var = "TODO"

   column_headers = ['Medical_Record_Number','Discharge_Date','Billing_Number','Discharge_ID','Dx_Number','Dx_Code','Dx_Title','Dx_Fiscal_Year','Dx_Present_On_Admit','Dx_Present_On_Admit_Title','Dx_Mental_Health_Disorder_Group','Dx_Mental_Health_Disorder_Group_Title','Dx Version']

   file_text = ""
   for header in column_headers:
      file_text += header
      file_text += ','

   file_text += '\n'
   
   for patient in patients:
      mrn = str(get_mrn())
      bill_no = TODO_var
      dc_date = TODO_var
      dc_id = TODO_var
      dx_no = TODO_var
      dx_code = TODO_var
      dx_title = TODO_var
      dx_fiscal_yr = TODO_var
      dx_present_on_admit = TODO_var
      dx_present_on_admit_title = TODO_var
      dx_mental_health_disorder_grp = TODO_var
      dx_mental_health_disorder_grp_title = TODO_var
      dx_version = TODO_var

      data_line = [mrn, dc_date, bill_no, dc_id, dx_no, dx_code, dx_title, dx_fiscal_yr, dx_present_on_admit, dx_present_on_admit_title, dx_mental_health_disorder_grp, dx_mental_health_disorder_grp_title, dx_version]

      for data in data_line:
         file_text += data
         file_text += ','
      file_text += '\n'

   with open(output_filename, 'w') as output_file:
      output_file.write(file_text)


if __name__ == "__main__":
   date = "10SEP2024"
   output_filename = "diagnosis_report_" + date + ".csv"
   patients = ['patient1', 'patient2', 'patient3']
   generate_diag_report(patients, output_filename)