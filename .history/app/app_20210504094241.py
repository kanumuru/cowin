from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)
data =[]

@app.route('/webhook', methods=['POST'])
def index():
    data1 = request.get_json(force=True)

    data.append(data1)

    return "sucess"


@app.route('/listner', methods=['GET'])
def data_listner():
    r =requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/districts/2')
    print(r.json())
    if len(data)==0:
        data.append({"data":"NO data found"})
    json_formatted_str = json.loads(json.dumps(data[-1], indent=4))
    return render_template('listner.html', data=json_formatted_str)



@app.route("/", methods=["GET","POST"])
def get_districts():
    if request.method == "GET":
        r =requests.get('https://cdn-api.co-vin.in/api/v2/admin/location/districts/2')
        # print(r.json())
        result = r.json()
        print(result['districts'])
        return render_template("district.html", all_districts=result['districts'])
    if request.method == "POST":
        id = request.form.get("id")
        print(id)
        date = request.form.get("date")
        z = 
        print(date)
        basicurl = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=" + str(id) + "&date=" + str(date)
        # r =requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=13&date=03-05-2021')
        print(basicurl)
        r = requests.get(basicurl)
        # print(r.json())
        result = r.json()
        return render_template("sessions.html", all_seesions=result['sessions'])

@app.route("/sessions", methods=["GET","POST"])
def get_sessions():
    print("I am in sessions ")
    if request.method == "GET":
        r =requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=13&date=04-05-2021')
        print(r.json())
        result = r.json()
        # print(result['sessions'])
        return render_template("sessions.html", all_seesions=result['sessions'])
    if request.method == "POST":
        id = request.form.get("id")
        print(id)
        date = request.form.get("date")
        print(date)
        basicurl = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=" + str(id) + "&date=" + str(date)
        # r =requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=13&date=03-05-2021')
        print(basicurl)
        r = requests.get(basicurl)
        print(r.json())
        return render_template("sessions.html", all_seesions=result['sessions'])
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



        
