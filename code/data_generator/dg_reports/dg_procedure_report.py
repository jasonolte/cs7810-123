### CS7810 Intro to Knowledge Engineering
### Fall 2024
### Project procedure report data generator
### Jason H. Nolte, nolte14@wright.edu
### https://github.com/jasonolte/cs7810-123

import random


def get_mrn():
   mrn_high = 1000000
   mrn = random.randint(0, mrn_high)
   return mrn

def generate_px_report(patients, output_filename):
   TODO_var = "TODO"

   column_headers = ['Medical_Record_Number','Billing_Number','Discharge_Date','Discharge_ID','Px_Sequence_Number','Px_Operative_Episode_Number','Px_Number','Px_Code_(ICD)','Px_Title_(ICD)','Px_Physician','Px_Physician_Sub_Specialty','Physician_Sub_Specialty_Title','Px_Operative_Flag','DI_DOS_Code','Date_Of_Service','Year_Of_Service','Quarter_Of_Service','Month_Of_Service','Day_Of_Service','Px Version']

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
      px_seq_no = TODO_var
      px_op_episode_no = TODO_var
      px_no = TODO_var
      px_code_icd = TODO_var
      px_title_icd = TODO_var
      px_physician = TODO_var
      px_physician_sub_spec = TODO_var
      px_physician_sub_spec_title = TODO_var
      px_operative_flag = TODO_var
      di_dos_code = TODO_var
      date_of_service = TODO_var
      year_of_service = TODO_var
      qtr_of_service = TODO_var
      month_of_service = TODO_var
      day_of_service = TODO_var
      px_version = TODO_var

      data_line = [mrn, bill_no, dc_date, dc_id, px_seq_no, px_op_episode_no, px_no, px_code_icd, px_title_icd, px_physician, px_physician_sub_spec, px_physician_sub_spec_title, px_operative_flag, di_dos_code, date_of_service, year_of_service, qtr_of_service, month_of_service, day_of_service, px_version]

      for data in data_line:
         file_text += data
         file_text += ','
      file_text += '\n'

   with open(output_filename, 'w') as output_file:
      output_file.write(file_text)


if __name__ == "__main__":
   date = "10SEP2024"
   output_filename = "procedure_report_" + date + ".csv"
   patients = ['patient1', 'patient2', 'patient3']
   generate_px_report(patients, output_filename)