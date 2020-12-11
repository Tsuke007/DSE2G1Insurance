
import numpy as np
from flask import Flask, request
import joblib
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def home():
    return "Hello DSE2G1"


@app.route('/predict', methods = ['GET'])
def predict():

    #import model ชื่อ 'model.pkl'	
    model = joblib.load('model.pkl')

    #เช็คว่า Method ส่งที่มา เป็นแบบ GET
    if request.method == 'GET':

        #อ่านค่า value จาก parameter ที่ชื่อ age เก็บไว้ที่ตัวแปร Age  datatype number
        Age = int(request.args.get("age"))


        #อ่านค่า value จาก parameter ที่ชื่อ region_code เก็บไว้ที่ตัวแปร Region_Code Datatype number
        Region_Code = int(request.args.get("region_code"))

        #อ่านค่า value จาก parameter ที่ชื่อ annual_premium เก็บไว้ที่ตัวแปร Annual_Premium Datatype number
        Annual_Premium = int(request.args.get("annual_premium"))

        #อ่านค่า value จาก parameter ที่ชื่อ policy_sales_channel เก็บไว้ที่ตัวแปร Policy_Sales_Channel Datatype number
        Policy_Sales_Channel = int(request.args.get("policy_sales_channel"))

        #อ่านค่า value จาก parameter ที่ชื่อ vintage เก็บไว้ที่ตัวแปร Vintage Datatype number
        Vintage = int(request.args.get("vintage"))
        
        #Tic เนื่องจาก future ที่จะส่งไป Model Predicion ได้ทำ one hot encodinge แต่เรา ต้องรับ Value จากผู้ใช้งาน เพียง 1 ตัวแปร เพื่อลดการ คีย์ข้อมูลที่ซ้ำซ้อน

        #จึงต้องมีการเขียน Code อ่านค่า value จาก parameter ที่ชื่อ driving_license และเช็คว่า Value ที่รับมา เป็น Yes หรือ No
        #ถ้าเป้น Yes ก็กำหนดค่าให้ตัวแปร Driving_License_No = 0 ถ้าเป็น No Driving_License_No = 1
        Driving_License_No = 1
        if str(request.args.get("driving_license")) == "Yes":
            Driving_License_No = 0

        #อ่านค่า value จาก parameter ที่ชื่อ driving_license และเช็คว่า Value ที่รับมา เป็น Yes หรือ No
        #ถ้าเป้น Yes ก็กำหนดค่าให้ตัวแปร Driving_License_Yes = 1 ถ้าเป็น No Driving_License_Yes = 0
        Driving_License_Yes = 0
        if str(request.args.get("driving_license")) == "Yes":
           Driving_License_Yes = 1

        #อ่านค่า value จาก parameter ที่ชื่อ previously_insured และเช็คว่า Value ที่รับมา เป็น Yes หรือ No
        #ถ้าเป้น Yes ก็กำหนดค่าให้ตัวแปร Previously_Insured_No = 0 ถ้าเป็น No Previously_Insured_No = 1
        Previously_Insured_No = 1
        if str(request.args.get("previously_insured")) == "Yes":
           Previously_Insured_No = 0

        #อ่านค่า value จาก parameter ที่ชื่อ previously_insured และเช็คว่า Value ที่รับมา เป็น Yes หรือ No
        #ถ้าเป้น Yes ก็กำหนดค่าให้ตัวแปร Previously_Insured_Yes = 1 ถ้าเป็น No Previously_Insured_Yes = 0
        Previously_Insured_Yes = 0
        if str(request.args.get("previously_insured")) == "Yes":
           Previously_Insured_Yes = 1

        #อ่านค่า value จาก parameter ที่ชื่อ gender และเช็คว่า Value ที่รับมา เป็น Male หรือ Female
        #ถ้าเป้น Female ก็กำหนดค่าให้ตัวแปร Gender_Female = 1 ถ้าเป็น Male Gender_Female = 0
        Gender_Female = 0
        if str(request.args.get("gender")) == "Female":
           Gender_Female = 1

        #อ่านค่า value จาก parameter ที่ชื่อ gender และเช็คว่า Value ที่รับมา เป็น Male หรือ Female
        #ถ้าเป้น Female ก็กำหนดค่าให้ตัวแปร Gender_Male = 0 ถ้าเป็น Male Gender_Male = 1
        Gender_Male = 1
        if str(request.args.get("gender")) == "Female":
           Gender_Male = 0


        #อ่านค่า value จาก parameter ที่ชื่อ vehicle_age และเช็คว่า Value ที่รับมา เป็น < 1 Year หรือ 1-2 Year หรือ > 2 Years
        #ถ้าเป้น < 1 Year ก็กำหนดค่าให้ตัวแปร Vehicle_Age_1_Year = 1 
        #ถ้าเป้น 1-2 Year ก็กำหนดค่าให้ตัวแปร Vehicle_Age_1_2_Year = 1 
        #ถ้าเป้น > 2 Years ก็กำหนดค่าให้ตัวแปร Vehicle_Age_2_Years = 1 
        Vehicle_Age_1_Year = 0
        Vehicle_Age_1_2_Year = 0
        Vehicle_Age_2_Years = 0

        if str(request.args.get("vehicle_age")) == "< 1 Year":
            Vehicle_Age_1_Year = 1
        elif str(request.args.get("vehicle_age")) == "1-2 Year":
            Vehicle_Age_1_2_Year = 1
        elif str(request.args.get("vehicle_age")) == "> 2 Years":   
            Vehicle_Age_2_Years=1


        #อ่านค่า value จาก parameter ที่ชื่อ vehicle_damage และเช็คว่า Value ที่รับมา เป็น Yes หรือ No
        #ถ้าเป้น Yes ก็กำหนดค่าให้ตัวแปร Vehicle_Damage_Yes = 1 ถ้าเป็น No Vehicle_Damage_Yes = 0
        Vehicle_Damage_Yes = 0
        if str(request.args.get("vehicle_damage")) == "Yes":
           Vehicle_Damage_Yes = 1
        
        #อ่านค่า value จาก parameter ที่ชื่อ vehicle_damage และเช็คว่า Value ที่รับมา เป็น Yes หรือ No
        #ถ้าเป้น Yes ก็กำหนดค่าให้ตัวแปร Vehicle_Damage_No = 0 ถ้าเป็น No Vehicle_Damage_No = 1
        if str(request.args.get("vehicle_damage")) == "Yes":
           Vehicle_Damage_No = 0

        #เตรียมข้อมูลของแต่ละตัวแปร กำหนดค่าไว้ที่ ตัวแปร feature
        feature = [Age, Region_Code, Annual_Premium, Policy_Sales_Channel, Vintage, Gender_Female, Gender_Male, Driving_License_No, Driving_License_Yes, Previously_Insured_No, Previously_Insured_Yes, Vehicle_Age_1_Year, Vehicle_Age_1_2_Year, Vehicle_Age_2_Years, Vehicle_Damage_No, Vehicle_Damage_Yes]
        feature = np.array(feature).reshape(1,-1)

        #เช็คผลลัพธ์ที่ Model Predic ได้ 
        #ถ้า Predic ได้ 1 ให้ return Customer is interested
        #ถ้า Predic ได้ 0 ให้ return Customer is not interested
        if model.predict(feature)[0] == 1:
            return "Customer is interested"
        elif model.predict(feature)[0] == 0:
            return "Customer is not interested"
            
   
if __name__ == '__main__':
    app.run()

    #import os
    #host = os.environ.get('server_host', 'localhost')
    #try:
    #    port = int(os.environ.get('server_port', '5555'))
    #except valueerror:
    #    port = 5555

    #app.run(host, port)
