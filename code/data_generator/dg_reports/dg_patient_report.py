### CS7810 Intro to Knowledge Engineering
### Fall 2024
### Project pharmacy daily data generator
### Jason H. Nolte, nolte14@wright.edu
### https://github.com/jasonolte/cs7810-123

def generate_patient_abstract_report(patients, output_filename):
   TODO_var = "TODO"

   column_headers = ['Hospital_Number','Hospital_City','Hospital_Name','Campus_Name','Medical_Record_Number','Discharge_ID','Billing_Number','Patient_Type','Patient_Type_Title','Admit_Age_In_Days','Admit_Age_In_Years','Birthweight_Grams','Birth_Weight_Indicator','Birth_Weight_Indicator_Title','Gestational_Age_In_Weeks','DOB','Gender','Gender_Title','Ethnicity','Ethnicity_Title','CTC_Flag','Race_White','Race_Black','Race_Asian','Race_Pacific_Islander','Race_American_Indian','Race_Other','Race_Version_1','Race_Title_Version_1','Length_Of_Stay','Disposition','Disposition_Title','Disposition_Version_1','Disposition_Title_Version_1','ED_Charge_Flag','NICU_Flag','ICU_Flag','Mechanical_Vent_Flag','ECMO_Flag','TPN_Flag','Operating_Room_Charge_Flag','Infection_Flag','Medical_Complication_Flag','Surgical_Complication_Flag','Version_1_Flag','Priority_Of_Admission','Priority_Of_Admission_Title','Priority_Of_Admission_V1','Priority_Of_Admission_Title_V1','Source_Of_Admission','Source_Of_Admission_Title','Source_Of_Admission_Digit_1','Source_Of_Admission_Digit_2','Source_Of_Admission_Version_1','Admit_Date','Discharge_Date','Discharge_Year','Discharge_Quarter','Discharge_Month','Principal_Dx','Principal_Dx_Title','Principal_Dx_Present_On_Admit','Principal_Dx_POA_Admit_Title','Principal_Px','Principal_Px_Title','Operative_Prin_Px_Flag','Pre_Operative_LOS','Post_Operative_LOS','Admit_Dx','Admit_Dx_Title','Cardiovascular_Flag','Gastrointestinal_Flag','Hematologic_or_Immunologic_Flag','Malignancy_Flag','Metabolic_Flag','Neurologic_and_Neuromuscular_Flag','Congenital_or_Genetic_Defect_Flg','Renal_and_Urologic_Flag','Respiratory_Flag','Primary_Source_Of_Payment','Primary_Source_Of_Payment_Title','Principal_Payer_Version_1','Principal_Payer_Title_V1','Census_Division','Census_Region','Premature_And_Neonatal_Flag','Technology_Dependent_Flag','Transplant_Flag','Complex_Chronic_Condition_Flag','Zip_Code','Urban_Flag','Median_Household_Income','Predicted_Median_Household_Income','Rural_Urban_Commuting_Area_Code','Discharge_Mortality_Flag','RACHS_Score','Abstract_Based_Charges','Billed_Charges','Clinical_Charges','Imaging_Charges','Lab_Charges','Other_Charges','Pharmacy_Charges','Supply_Charges','Unmapped_Charges','Estimated_Cost','Adj_Abstract_Based_Charges','Adj_Billed_Charges','Adj_Clinical_Charges','Adj_Imaging_Charges','Adj_Lab_Charges','Adj_Other_Charges','Adj_Pharmacy_Charges','Adj_Supply_Charges','Adj_Unmapped_Charges','Adj_Est_Cost','PMCA_Category','PMCA_Category_Title','Mental_Health_Disorder_Flag','Prin_Dx_Mental_Health_Disorder_Flag','Secondary_Dx_Mental_Health_Flag','Prin_Dx_Mental_Health_Group','Prin_Dx_Mental_Health_Group_Ttl','Clinical_Standardized_Costs','Imaging_Standardized_Costs','Lab_Standardized_Costs','Other_Standardized_Costs','Pharmacy_Standardized_Costs','Supply_Standardized_Costs']

   file_text = ""
   for header in column_headers:
      file_text += header
      file_text += ','

   file_text += '\n'
   
   for patient in patients:
      hospital_number = TODO_var
      hospital_city = TODO_var
      hospital_name = TODO_var
      campus_name = TODO_var
      medical_record_number = TODO_var
      discharge_id = TODO_var
      billing_number = TODO_var
      patient_type = TODO_var
      patient_type_title = TODO_var
      admit_age_in_days = TODO_var
      admit_age_in_years = TODO_var
      birthweight_grams = TODO_var
      birth_Weight_indicator = TODO_var
      birth_Weight_indicator_title = TODO_var
      gestational_age_in_Weeks = TODO_var
      dob = TODO_var
      gender = TODO_var
      gender_title = TODO_var
      ethnicity = TODO_var
      ethnicity_title = TODO_var
      ctc_flag = TODO_var
      race_White = TODO_var
      race_black = TODO_var
      race_asian = TODO_var
      race_pacific_islander = TODO_var
      race_american_indian = TODO_var
      race_other = TODO_var
      race_version_1 = TODO_var
      race_title_version_1 = TODO_var
      length_of_stay = TODO_var
      disposition = TODO_var
      disposition_title = TODO_var
      disposition_version_1 = TODO_var
      disposition_title_version_1 = TODO_var
      ed_charge_flag = TODO_var
      nicu_flag = TODO_var
      icu_flag = TODO_var
      mechanical_vent_flag = TODO_var
      ecmo_flag = TODO_var
      tpn_flag = TODO_var
      operating_room_charge_flag = TODO_var
      infection_flag = TODO_var
      medical_complication_flag = TODO_var
      surgical_complication_flag = TODO_var
      version_1_flag = TODO_var
      priority_of_admission = TODO_var
      priority_of_admission_title = TODO_var
      priority_of_admission_v1 = TODO_var
      priority_of_admission_title_v1 = TODO_var
      source_of_admission = TODO_var
      source_of_admission_title = TODO_var
      source_of_admission_digit_1 = TODO_var
      source_of_admission_digit_2 = TODO_var
      source_of_admission_version_1 = TODO_var
      admit_date = TODO_var
      discharge_date = TODO_var
      discharge_year = TODO_var
      discharge_quarter = TODO_var
      discharge_month = TODO_var
      principal_dx = TODO_var
      principal_dx_title = TODO_var
      principal_dx_present_on_admit = TODO_var
      principal_dx_poa_admit_title = TODO_var
      principal_px = TODO_var
      principal_px_title = TODO_var
      operative_prin_px_flag = TODO_var
      pre_operative_los = TODO_var
      post_operative_los = TODO_var
      admit_dx = TODO_var
      admit_dx_title = TODO_var
      cardiovascular_flag = TODO_var
      gastrointestinal_flag = TODO_var
      hematologic_or_immunologic_flag = TODO_var
      malignancy_flag = TODO_var
      metabolic_flag = TODO_var
      neurologic_and_neuromuscular_flag = TODO_var
      congenital_or_genetic_defect_flg = TODO_var
      renal_and_urologic_flag = TODO_var
      respiratory_flag = TODO_var
      primary_source_of_payment = TODO_var
      primary_source_of_payment_title = TODO_var
      principal_payer_version_1 = TODO_var
      principal_payer_title_v1 = TODO_var
      census_division = TODO_var
      census_region = TODO_var
      premature_and_neonatal_flag = TODO_var
      technology_dependent_flag = TODO_var
      transplant_flag = TODO_var
      complex_chronic_condition_flag = TODO_var
      zip_code = TODO_var
      urban_flag = TODO_var
      median_household_income = TODO_var
      predicted_median_household_income = TODO_var
      rural_urban_commuting_area_code = TODO_var
      discharge_mortality_flag = TODO_var
      rachs_score = TODO_var
      abstract_based_charges = TODO_var
      billed_charges = TODO_var
      clinical_charges = TODO_var
      imaging_charges = TODO_var
      lab_charges = TODO_var
      other_charges = TODO_var
      pharmacy_charges = TODO_var
      supply_charges = TODO_var
      unmapped_charges = TODO_var
      estimated_cost = TODO_var
      adj_abstract_based_charges = TODO_var
      adj_billed_charges = TODO_var
      adj_clinical_charges = TODO_var
      adj_imaging_charges = TODO_var
      adj_lab_charges = TODO_var
      adj_other_charges = TODO_var
      adj_pharmacy_charges = TODO_var
      adj_supply_charges = TODO_var
      adj_unmapped_charges = TODO_var
      adj_est_cost = TODO_var
      pmca_category = TODO_var
      pmca_category_title = TODO_var
      mental_health_disorder_flag = TODO_var
      prin_dx_mental_health_disorder_flag = TODO_var
      secondary_dx_mental_health_flag = TODO_var
      prin_dx_mental_health_group = TODO_var
      prin_dx_mental_health_group_ttl = TODO_var
      clinical_standardized_costs = TODO_var
      imaging_standardized_costs = TODO_var
      lab_standardized_costs = TODO_var
      other_standardized_costs = TODO_var
      pharmacy_standardized_costs = TODO_var
      supply_standardized_costs = TODO_var

      data_line = [hospital_number,hospital_city,hospital_name,campus_name,medical_record_number,discharge_id,billing_number,patient_type,patient_type_title,admit_age_in_days,admit_age_in_years,birthweight_grams,birth_Weight_indicator,birth_Weight_indicator_title,gestational_age_in_Weeks,dob,gender,gender_title,ethnicity,ethnicity_title,ctc_flag,race_White,race_black,race_asian,race_pacific_islander,race_american_indian,race_other,race_version_1,race_title_version_1,length_of_stay,disposition,disposition_title,disposition_version_1,disposition_title_version_1,ed_charge_flag,nicu_flag,icu_flag,mechanical_vent_flag,ecmo_flag,tpn_flag,operating_room_charge_flag,infection_flag,medical_complication_flag,surgical_complication_flag,version_1_flag,priority_of_admission,priority_of_admission_title,priority_of_admission_v1,priority_of_admission_title_v1,source_of_admission,source_of_admission_title,source_of_admission_digit_1,source_of_admission_digit_2,source_of_admission_version_1,admit_date,discharge_date,discharge_year,discharge_quarter,discharge_month,principal_dx,principal_dx_title,principal_dx_present_on_admit,principal_dx_poa_admit_title,principal_px,principal_px_title,operative_prin_px_flag,pre_operative_los,post_operative_los,admit_dx,admit_dx_title,cardiovascular_flag,gastrointestinal_flag,hematologic_or_immunologic_flag,malignancy_flag,metabolic_flag,neurologic_and_neuromuscular_flag,congenital_or_genetic_defect_flg,renal_and_urologic_flag,respiratory_flag,primary_source_of_payment,primary_source_of_payment_title,principal_payer_version_1,principal_payer_title_v1,census_division,census_region,premature_and_neonatal_flag,technology_dependent_flag,transplant_flag,complex_chronic_condition_flag,zip_code,urban_flag,median_household_income,predicted_median_household_income,rural_urban_commuting_area_code,discharge_mortality_flag,rachs_score,abstract_based_charges,billed_charges,clinical_charges,imaging_charges,lab_charges,other_charges,pharmacy_charges,supply_charges,unmapped_charges,estimated_cost,adj_abstract_based_charges,adj_billed_charges,adj_clinical_charges,adj_imaging_charges,adj_lab_charges,adj_other_charges,adj_pharmacy_charges,adj_supply_charges,adj_unmapped_charges,adj_est_cost,pmca_category,pmca_category_title,mental_health_disorder_flag,prin_dx_mental_health_disorder_flag,secondary_dx_mental_health_flag,prin_dx_mental_health_group,prin_dx_mental_health_group_ttl,clinical_standardized_costs,imaging_standardized_costs,lab_standardized_costs,other_standardized_costs,pharmacy_standardized_costs,supply_standardized_costs]

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
   generate_patient_abstract_report(patients, output_filename)