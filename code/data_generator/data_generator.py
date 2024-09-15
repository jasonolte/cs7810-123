### CS7810 Intro to Knowledge Engineering
### Fall 2024
### Project data generator
### Jason H. Nolte, nolte14@wright.edu
### https://github.com/jasonolte/cs7810-123

import dg_reports.dg_pharm_daily as pharm_daily
import dg_reports.dg_clinical_daily as clin_daily
import dg_reports.dg_imaging_daily as imag_daily
import dg_reports.dg_lab_daily as lab_daily
import dg_reports.dg_supply_daily as supp_daily
import dg_reports.dg_other_daily as other_daily
import dg_reports.dg_CPT_report as cpt_report
import dg_reports.dg_diagnosis_report as diagnosis_report
import dg_reports.dg_procedure_report as procedure_report
import dg_reports.dg_patient_report as patient_report

def data_generator():
   date = "10SEP2024"
   output_filename = "_daily_" + date + ".csv"
   patients = ['patient1', 'patient2', 'patient3']
   cpt_report.generate_cpt_report(patients, "cpt_report" + output_filename)
   diagnosis_report.generate_diag_report(patients, "diagnosis_report" + output_filename)
   procedure_report.generate_px_report(patients, "procedure_report" + output_filename)
   patient_report.generate_patient_abstract_report(patients, "patient_abstract_report" + output_filename)

   pharm_daily.generate_pharm_daily_report(patients, date, "pharm" + output_filename)
   clin_daily.generate_clin_daily_report(patients, date, "clinical" + output_filename)
   imag_daily.generate_imag_daily_report(patients, date, "imaging" + output_filename)
   lab_daily.generate_lab_daily_report(patients, date, "lab" + output_filename)
   supp_daily.generate_supp_daily_report(patients, date, "supply" + output_filename)
   other_daily.generate_other_daily_report(patients, date, "other" + output_filename)

if __name__ == "__main__":
   data_generator()