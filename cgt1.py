import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred=credentials.Certificate("cgtest1-38ec4-firebase-adminsdk-en5vx-0857ce601e.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

db.collection('Person').add({'Name':'Kishalay', 'Age':23, 'Company':'CG'})

data1={'Name':'K.Bhattacharya', 'Age':23, 'Company':'CG'}
db.collection('Person').document("emp1").set(data1)


db.collection('Person').document("emp1").set({"phn no":123456}, merge=True)
pl='language'
v='Java'
d1={pl:v}
db.collection('Person').document("emp1").set(d1, merge=True)


t1={"training1":"Python","training2":"devops","training3":"GCP"}
db.collection('Person').document("emp1").collection("ANZ").document("Trainings").add(t1)
