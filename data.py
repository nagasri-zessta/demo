import streamlit as st
import pandas as pd
import numpy as np

a = [1,2,3,4,5,6,7,8]
n=np.array(a)
nd = n.reshape((2,4))

dic={
  "invoice_details": {
    "Vendor_name": "HARIKA SHIPPING AND LOGISTICS",
    "vendor_address": "D.No: 8-50-10, F.F-2, OLD CBI DOWN CHINA WALTAIR, VISAKHAPATNAM 17",
    "phone": "0801-2573868, 2573858",
    "email": "",
    "Vendor_GST": "37ABZPV8982E1ZF",
    "laurus_GST": "37AABCL1170C1Z0",
    "PAN_NO": "ABZPV8982E",
    "PO_No": "14000003036",
    "CIN_NO": "",
    "invoice_no": "IN/123/0582/23",
    "regd_office": "PLOT NO. 21, J N PHARMA CITY, PARAWADA VILLAGE & MANDAL, VISAKHAPATNAM DIST., State Andhra Pradesh - 37",
    "invoice_date": "2023/05/24",
    "charges": {
      "Storage": "4800.00",
      "C&F": "34775.00",
      "Detention": "23204.50",
      "Transport": ""
    },
    "Total_Basic_Value": "83242.27",
    "taxes": {
      "CGST": "7491.80",
      "SGST": "7491.80",
      "IGST": ""
    },
    "Invoice_Total_Amount": "98225.88",
    "TDS": "",
    "Net_Payable": "98226.00",
    "Plant": "",
    "CC": "",
    "Shipping_Address": "",
    "vendor_code": "",
    "GST_Tax_code": "",
    "withholding_Tax_code": "",
    "GL_Code": "",
    "Detention_GL": "",
    "Scan_File_Name": "",
    "FI_Doc_No": "",
    "Status": ""
  }
}

data1 = pd.read_csv("Salary_Data.csv")
st.dataframe(data1,width=500,height=500)
st.table(dic)
st.json(dic)
st.write(data1)

