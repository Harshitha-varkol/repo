from django.shortcuts import render

students=[
    {'name':'akshitha','rollno':1,'email':'akshitha1234@gmail.com','add':'hyd','per':98,'YOP':2025,'DOB':'12-09-2003','stream':'cs','branch':'Pyspiders','age':'21','courseopted':'python'},
    {'name':'nisha','rollno':2,'email':'nisha321@gmail.com','add':'bangalore','per':85,'YOP':2024,'DOB':'15-07-2002','stream':'it','branch':'Pyspiders','age':'22','courseopted':'python'},
    {'name':'raj','rollno':3,'email':'raj456@gmail.com','add':'mumbai','per':88,'YOP':2025,'DOB':'09-01-2003','stream':'ece','branch':'Pyspiders','age':'21','courseopted':'python'},
    {'name':'diya','rollno':4,'email':'diya789@gmail.com','add':'delhi','per':93,'YOP':2023,'DOB':'20-12-2001','stream':'cs','branch':'Pyspiders','age':'23','courseopted':'python'},
    {'name':'karthik','rollno':5,'email':'karthik111@gmail.com','add':'chennai','per':95,'YOP':2024,'DOB':'11-11-2002','stream':'mech','branch':'Pyspiders','age':'22','courseopted':'python'},
    {'name':'meena','rollno':6,'email':'meena222@gmail.com','add':'vizag','per':82,'YOP':2025,'DOB':'01-06-2003','stream':'it','branch':'Pyspiders','age':'21','courseopted':'python'},
    {'name':'akash','rollno':7,'email':'akash333@gmail.com','add':'pune','per':89,'YOP':2024,'DOB':'30-08-2002','stream':'cs','branch':'Pyspiders','age':'22','courseopted':'python'},
    {'name':'sana','rollno':8,'email':'sana444@gmail.com','add':'hyd','per':92,'YOP':2025,'DOB':'17-02-2003','stream':'ece','branch':'Pyspiders','age':'21','courseopted':'python'},
    {'name':'vinay','rollno':9,'email':'vinay555@gmail.com','add':'bangalore','per':87,'YOP':2023,'DOB':'05-04-2001','stream':'eee','branch':'Pyspiders','age':'23','courseopted':'python'},
    {'name':'rekha','rollno':10,'email':'rekha666@gmail.com','add':'delhi','per':90,'YOP':2024,'DOB':'25-09-2002','stream':'civil','branch':'Pyspiders','age':'22','courseopted':'python'},
    {'name':'ravi','rollno':11,'email':'ravi777@gmail.com','add':'mumbai','per':94,'YOP':2025,'DOB':'13-03-2003','stream':'cs','branch':'Pyspiders','age':'21','courseopted':'python'},
    {'name':'priya','rollno':12,'email':'priya888@gmail.com','add':'chennai','per':91,'YOP':2023,'DOB':'21-01-2001','stream':'it','branch':'Pyspiders','age':'23','courseopted':'python'},
    {'name':'rahul','rollno':13,'email':'rahul999@gmail.com','add':'vizag','per':84,'YOP':2024,'DOB':'08-05-2002','stream':'ece','branch':'Pyspiders','age':'22','courseopted':'python'},
    {'name':'sita','rollno':14,'email':'sita000@gmail.com','add':'hyd','per':97,'YOP':2025,'DOB':'27-07-2003','stream':'cs','branch':'Pyspiders','age':'21','courseopted':'python'},
    {'name':'vamsi','rollno':15,'email':'vamsi112@gmail.com','add':'pune','per':89,'YOP':2024,'DOB':'03-03-2002','stream':'eee','branch':'Pyspiders','age':'22','courseopted':'python'},
    {'name':'anita','rollno':16,'email':'anita223@gmail.com','add':'bangalore','per':86,'YOP':2023,'DOB':'10-10-2001','stream':'civil','branch':'Pyspiders','age':'23','courseopted':'python'},
    {'name':'manoj','rollno':17,'email':'manoj334@gmail.com','add':'delhi','per':88,'YOP':2024,'DOB':'04-12-2002','stream':'mech','branch':'Pyspiders','age':'22','courseopted':'python'},
    {'name':'latha','rollno':18,'email':'latha445@gmail.com','add':'chennai','per':92,'YOP':2025,'DOB':'14-06-2003','stream':'cs','branch':'Pyspiders','age':'21','courseopted':'python'},
    {'name':'sandeep','rollno':19,'email':'sandeep556@gmail.com','add':'mumbai','per':90,'YOP':2023,'DOB':'29-09-2001','stream':'it','branch':'Pyspiders','age':'23','courseopted':'python'},
    {'name':'deepa','rollno':20,'email':'deepa667@gmail.com','add':'hyd','per':95,'YOP':2024,'DOB':'12-08-2002','stream':'ece','branch':'Pyspiders','age':'22','courseopted':'python'},
    {'name':'teja','rollno':21,'email':'teja778@gmail.com','add':'vizag','per':87,'YOP':2025,'DOB':'22-10-2003','stream':'cs','branch':'Pyspiders','age':'21','courseopted':'python'},
    {'name':'lavanya','rollno':22,'email':'lavanya889@gmail.com','add':'pune','per':93,'YOP':2024,'DOB':'06-02-2002','stream':'eee','branch':'Pyspiders','age':'22','courseopted':'python'},
    {'name':'naveen','rollno':23,'email':'naveen990@gmail.com','add':'bangalore','per':91,'YOP':2023,'DOB':'16-06-2001','stream':'civil','branch':'Pyspiders','age':'23','courseopted':'python'},
    {'name':'usha','rollno':24,'email':'usha111@gmail.com','add':'delhi','per':89,'YOP':2024,'DOB':'02-11-2002','stream':'mech','branch':'Pyspiders','age':'22','courseopted':'python'},
    {'name':'tarun','rollno':25,'email':'tarun222@gmail.com','add':'chennai','per':96,'YOP':2025,'DOB':'30-04-2003','stream':'cs','branch':'Pyspiders','age':'21','courseopted':'python'},
    {'name':'geeta','rollno':26,'email':'geeta333@gmail.com','add':'mumbai','per':90,'YOP':2023,'DOB':'19-07-2001','stream':'it','branch':'Pyspiders','age':'23','courseopted':'python'},
    {'name':'anil','rollno':27,'email':'anil444@gmail.com','add':'hyd','per':85,'YOP':2024,'DOB':'01-09-2002','stream':'ece','branch':'Pyspiders','age':'22','courseopted':'python'},
    {'name':'keerthi','rollno':28,'email':'keerthi555@gmail.com','add':'vizag','per':92,'YOP':2025,'DOB':'24-03-2003','stream':'cs','branch':'Pyspiders','age':'21','courseopted':'python'},
    {'name':'harsha','rollno':29,'email':'harsha666@gmail.com','add':'pune','per':88,'YOP':2024,'DOB':'13-01-2002','stream':'eee','branch':'Pyspiders','age':'22','courseopted':'python'},
    {'name':'jyothi','rollno':30,'email':'jyothi777@gmail.com','add':'bangalore','per':91,'YOP':2023,'DOB':'28-05-2001','stream':'civil','branch':'Pyspiders','age':'23','courseopted':'python'},
    {'name':'suman','rollno':31,'email':'suman888@gmail.com','add':'delhi','per':95,'YOP':2024,'DOB':'07-06-2002','stream':'mech','branch':'Pyspiders','age':'22','courseopted':'python'},
    {'name':'shruti','rollno':32,'email':'shruti999@gmail.com','add':'chennai','per':94,'YOP':2025,'DOB':'10-12-2003','stream':'cs','branch':'Pyspiders','age':'21','courseopted':'python'},
    {'name':'lokesh','rollno':33,'email':'lokesh000@gmail.com','add':'mumbai','per':89,'YOP':2023,'DOB':'18-08-2001','stream':'it','branch':'Pyspiders','age':'23','courseopted':'python'},
    {'name':'rekha','rollno':34,'email':'rekha123@gmail.com','add':'hyd','per':86,'YOP':2024,'DOB':'23-11-2002','stream':'ece','branch':'Pyspiders','age':'22','courseopted':'python'},
    {'name':'yash','rollno':35,'email':'yash234@gmail.com','add':'vizag','per':92,'YOP':2025,'DOB':'14-09-2003','stream':'cs','branch':'Pyspiders','age':'21','courseopted':'python'},
    {'name':'aditya','rollno':36,'email':'aditya123@gmail.com','add':'bangalore','per':90,'YOP':2025,'DOB':'03-03-2003','stream':'it','branch':'Jspiders','age':'21','courseopted':'java'},
    {'name':'neha','rollno':37,'email':'neha456@gmail.com','add':'delhi','per':88,'YOP':2024,'DOB':'11-09-2002','stream':'cs','branch':'Jspiders','age':'22','courseopted':'java'},
    {'name':'rohit','rollno':38,'email':'rohit789@gmail.com','add':'mumbai','per':86,'YOP':2023,'DOB':'06-01-2001','stream':'ece','branch':'Jspiders','age':'23','courseopted':'java'},
    {'name':'ananya','rollno':39,'email':'ananya987@gmail.com','add':'hyd','per':91,'YOP':2024,'DOB':'29-07-2002','stream':'mech','branch':'Jspiders','age':'22','courseopted':'java'},
    {'name':'sai','rollno':40,'email':'sai654@gmail.com','add':'chennai','per':93,'YOP':2025,'DOB':'17-05-2003','stream':'cs','branch':'Jspiders','age':'21','courseopted':'java'},
    {'name':'riya','rollno':41,'email':'riya321@gmail.com','add':'vizag','per':84,'YOP':2023,'DOB':'21-02-2001','stream':'civil','branch':'Jspiders','age':'23','courseopted':'java'},
    {'name':'arav','rollno':42,'email':'arav987@gmail.com','add':'pune','per':89,'YOP':2024,'DOB':'12-08-2002','stream':'it','branch':'Jspiders','age':'22','courseopted':'java'},
    {'name':'pooja','rollno':43,'email':'pooja1234@gmail.com','add':'bangalore','per':95,'YOP':2025,'DOB':'04-04-2003','stream':'ece','branch':'Jspiders','age':'21','courseopted':'java'},
    {'name':'kiran','rollno':44,'email':'kiran4567@gmail.com','add':'delhi','per':87,'YOP':2023,'DOB':'15-06-2001','stream':'cs','branch':'Jspiders','age':'23','courseopted':'java'},
    {'name':'swathi','rollno':45,'email':'swathi321@gmail.com','add':'mumbai','per':90,'YOP':2024,'DOB':'01-11-2002','stream':'mech','branch':'Jspiders','age':'22','courseopted':'java'},
    {'name':'dinesh','rollno':46,'email':'dinesh654@gmail.com','add':'hyd','per':92,'YOP':2025,'DOB':'19-09-2003','stream':'cs','branch':'Jspiders','age':'21','courseopted':'java'},
    {'name':'lavina','rollno':47,'email':'lavina123@gmail.com','add':'chennai','per':85,'YOP':2023,'DOB':'07-12-2001','stream':'ece','branch':'Jspiders','age':'23','courseopted':'java'},
    {'name':'gopal','rollno':48,'email':'gopal234@gmail.com','add':'vizag','per':89,'YOP':2024,'DOB':'25-01-2002','stream':'it','branch':'Jspiders','age':'22','courseopted':'java'},
    {'name':'aisha','rollno':49,'email':'aisha456@gmail.com','add':'pune','per':93,'YOP':2025,'DOB':'18-10-2003','stream':'cs','branch':'Jspiders','age':'21','courseopted':'java'},
    {'name':'rahim','rollno':50,'email':'rahim678@gmail.com','add':'bangalore','per':88,'YOP':2024,'DOB':'10-03-2002','stream':'civil','branch':'Jspiders','age':'22','courseopted':'java'},
    {'name':'zara','rollno':51,'email':'zara999@gmail.com','add':'delhi','per':90,'YOP':2023,'DOB':'30-08-2001','stream':'ece','branch':'Jspiders','age':'23','courseopted':'java'},
    {'name':'nithin','rollno':52,'email':'nithin432@gmail.com','add':'mumbai','per':91,'YOP':2024,'DOB':'03-06-2002','stream':'mech','branch':'Jspiders','age':'22','courseopted':'java'},
    {'name':'tanya','rollno':53,'email':'tanya111@gmail.com','add':'hyd','per':86,'YOP':2025,'DOB':'22-09-2003','stream':'cs','branch':'Jspiders','age':'21','courseopted':'java'},
    {'name':'vishal','rollno':54,'email':'vishal222@gmail.com','add':'chennai','per':94,'YOP':2023,'DOB':'13-07-2001','stream':'it','branch':'Jspiders','age':'23','courseopted':'java'},
    {'name':'megha','rollno':55,'email':'megha333@gmail.com','add':'vizag','per':89,'YOP':2024,'DOB':'09-02-2002','stream':'cs','branch':'Jspiders','age':'22','courseopted':'java'},
    {'name':'abhinav','rollno':56,'email':'abhinav444@gmail.com','add':'pune','per':92,'YOP':2025,'DOB':'06-05-2003','stream':'ece','branch':'Jspiders','age':'21','courseopted':'java'},
    {'name':'sneha','rollno':57,'email':'sneha555@gmail.com','add':'bangalore','per':87,'YOP':2023,'DOB':'01-01-2001','stream':'cs','branch':'Jspiders','age':'23','courseopted':'java'},
    {'name':'rakesh','rollno':58,'email':'rakesh666@gmail.com','add':'delhi','per':90,'YOP':2024,'DOB':'27-04-2002','stream':'civil','branch':'Jspiders','age':'22','courseopted':'java'},
    {'name':'isha','rollno':59,'email':'isha777@gmail.com','add':'mumbai','per':93,'YOP':2025,'DOB':'17-06-2003','stream':'cs','branch':'Jspiders','age':'21','courseopted':'java'},
    {'name':'sachin','rollno':60,'email':'sachin888@gmail.com','add':'hyd','per':88,'YOP':2023,'DOB':'05-09-2001','stream':'it','branch':'Jspiders','age':'23','courseopted':'java'},
    {'name':'divya','rollno':61,'email':'divya999@gmail.com','add':'chennai','per':91,'YOP':2024,'DOB':'15-11-2002','stream':'ece','branch':'Jspiders','age':'22','courseopted':'java'},
    {'name':'dev','rollno':62,'email':'dev000@gmail.com','add':'vizag','per':89,'YOP':2025,'DOB':'11-03-2003','stream':'cs','branch':'Jspiders','age':'21','courseopted':'java'},
    {'name':'shraddha','rollno':63,'email':'shraddha111@gmail.com','add':'pune','per':94,'YOP':2023,'DOB':'23-10-2001','stream':'mech','branch':'Jspiders','age':'23','courseopted':'java'},
    {'name':'arvind','rollno':64,'email':'arvind222@gmail.com','add':'bangalore','per':90,'YOP':2024,'DOB':'28-08-2002','stream':'cs','branch':'Jspiders','age':'22','courseopted':'java'},
    {'name':'malvika','rollno':65,'email':'malvika333@gmail.com','add':'delhi','per':95,'YOP':2025,'DOB':'19-01-2003','stream':'it','branch':'Jspiders','age':'21','courseopted':'java'},
    {'name':'sudhir','rollno':66,'email':'sudhir444@gmail.com','add':'mumbai','per':86,'YOP':2023,'DOB':'31-07-2001','stream':'ece','branch':'Jspiders','age':'23','courseopted':'java'},
    {'name':'anjali','rollno':67,'email':'anjali555@gmail.com','add':'hyd','per':88,'YOP':2024,'DOB':'02-10-2002','stream':'cs','branch':'Jspiders','age':'22','courseopted':'java'},
    {'name':'rishi','rollno':68,'email':'rishi666@gmail.com','add':'chennai','per':90,'YOP':2025,'DOB':'25-12-2003','stream':'civil','branch':'Jspiders','age':'21','courseopted':'java'},
    {'name':'kavya','rollno':69,'email':'kavya777@gmail.com','add':'vizag','per':91,'YOP':2023,'DOB':'14-06-2001','stream':'mech','branch':'Jspiders','age':'23','courseopted':'java'},
    {'name':'ajay','rollno':70,'email':'ajay888@gmail.com','add':'pune','per':87,'YOP':2024,'DOB':'20-03-2002','stream':'cs','branch':'Jspiders','age':'22','courseopted':'java'},
    {'name':'manasa','rollno':71,'email':'manasa123@gmail.com','add':'bangalore','per':88,'YOP':2025,'DOB':'12-03-2003','stream':'cs','branch':'Qspiders','age':'21','courseopted':'testing'},
    {'name':'pranav','rollno':72,'email':'pranav456@gmail.com','add':'hyd','per':91,'YOP':2024,'DOB':'03-06-2002','stream':'it','branch':'Qspiders','age':'22','courseopted':'testing'},
    {'name':'isha','rollno':73,'email':'isha789@gmail.com','add':'chennai','per':85,'YOP':2023,'DOB':'28-01-2001','stream':'ece','branch':'Qspiders','age':'23','courseopted':'testing'},
    {'name':'rahul','rollno':74,'email':'rahul321@gmail.com','add':'mumbai','per':90,'YOP':2024,'DOB':'11-09-2002','stream':'cs','branch':'Qspiders','age':'22','courseopted':'testing'},
    {'name':'divya','rollno':75,'email':'divya654@gmail.com','add':'delhi','per':92,'YOP':2025,'DOB':'14-07-2003','stream':'mech','branch':'Qspiders','age':'21','courseopted':'testing'},
    {'name':'omkar','rollno':76,'email':'omkar987@gmail.com','add':'vizag','per':87,'YOP':2023,'DOB':'19-04-2001','stream':'civil','branch':'Qspiders','age':'23','courseopted':'testing'},
    {'name':'reema','rollno':77,'email':'reema111@gmail.com','add':'pune','per':89,'YOP':2024,'DOB':'25-10-2002','stream':'it','branch':'Qspiders','age':'22','courseopted':'testing'},
    {'name':'siddharth','rollno':78,'email':'sid123@gmail.com','add':'bangalore','per':90,'YOP':2025,'DOB':'02-05-2003','stream':'cs','branch':'Qspiders','age':'21','courseopted':'testing'},
    {'name':'sneha','rollno':79,'email':'sneha456@gmail.com','add':'hyd','per':86,'YOP':2023,'DOB':'07-02-2001','stream':'ece','branch':'Qspiders','age':'23','courseopted':'testing'},
    {'name':'vivek','rollno':80,'email':'vivek789@gmail.com','add':'chennai','per':88,'YOP':2024,'DOB':'10-11-2002','stream':'cs','branch':'Qspiders','age':'22','courseopted':'testing'},
    {'name':'kavya','rollno':81,'email':'kavya123@gmail.com','add':'mumbai','per':91,'YOP':2025,'DOB':'30-06-2003','stream':'mech','branch':'Qspiders','age':'21','courseopted':'testing'},
    {'name':'naveen','rollno':82,'email':'naveen456@gmail.com','add':'delhi','per':93,'YOP':2023,'DOB':'05-01-2001','stream':'cs','branch':'Qspiders','age':'23','courseopted':'testing'},
    {'name':'anu','rollno':83,'email':'anu789@gmail.com','add':'vizag','per':85,'YOP':2024,'DOB':'18-08-2002','stream':'it','branch':'Qspiders','age':'22','courseopted':'testing'},
    {'name':'vijay','rollno':84,'email':'vijay321@gmail.com','add':'pune','per':90,'YOP':2025,'DOB':'09-09-2003','stream':'ece','branch':'Qspiders','age':'21','courseopted':'testing'},
    {'name':'lavanya','rollno':85,'email':'lavanya654@gmail.com','add':'bangalore','per':88,'YOP':2023,'DOB':'22-03-2001','stream':'cs','branch':'Qspiders','age':'23','courseopted':'testing'},
    {'name':'rishi','rollno':86,'email':'rishi987@gmail.com','add':'hyd','per':89,'YOP':2024,'DOB':'16-12-2002','stream':'mech','branch':'Qspiders','age':'22','courseopted':'testing'},
    {'name':'shruti','rollno':87,'email':'shruti111@gmail.com','add':'chennai','per':94,'YOP':2025,'DOB':'26-07-2003','stream':'cs','branch':'Qspiders','age':'21','courseopted':'testing'},
    {'name':'lokesh','rollno':88,'email':'lokesh222@gmail.com','add':'mumbai','per':90,'YOP':2023,'DOB':'01-10-2001','stream':'civil','branch':'Qspiders','age':'23','courseopted':'testing'},
    {'name':'deepa','rollno':89,'email':'deepa333@gmail.com','add':'delhi','per':87,'YOP':2024,'DOB':'13-02-2002','stream':'ece','branch':'Qspiders','age':'22','courseopted':'testing'},
    {'name':'harsha','rollno':90,'email':'harsha444@gmail.com','add':'vizag','per':91,'YOP':2025,'DOB':'04-06-2003','stream':'cs','branch':'Qspiders','age':'21','courseopted':'testing'},
    {'name':'meena','rollno':91,'email':'meena555@gmail.com','add':'pune','per':86,'YOP':2023,'DOB':'12-01-2001','stream':'cs','branch':'Qspiders','age':'23','courseopted':'testing'},
    {'name':'sagar','rollno':92,'email':'sagar666@gmail.com','add':'bangalore','per':88,'YOP':2024,'DOB':'19-09-2002','stream':'it','branch':'Qspiders','age':'22','courseopted':'testing'},
    {'name':'rekha','rollno':93,'email':'rekha777@gmail.com','add':'hyd','per':92,'YOP':2025,'DOB':'23-08-2003','stream':'cs','branch':'Qspiders','age':'21','courseopted':'testing'},
    {'name':'mukesh','rollno':94,'email':'mukesh888@gmail.com','add':'chennai','per':85,'YOP':2023,'DOB':'06-04-2001','stream':'ece','branch':'Qspiders','age':'23','courseopted':'testing'},
    {'name':'anusha','rollno':95,'email':'anusha999@gmail.com','add':'mumbai','per':89,'YOP':2024,'DOB':'15-12-2002','stream':'mech','branch':'Qspiders','age':'22','courseopted':'testing'},
    {'name':'teja','rollno':96,'email':'teja000@gmail.com','add':'delhi','per':90,'YOP':2025,'DOB':'27-11-2003','stream':'cs','branch':'Qspiders','age':'21','courseopted':'testing'},
    {'name':'keerthi','rollno':97,'email':'keerthi101@gmail.com','add':'vizag','per':93,'YOP':2023,'DOB':'02-06-2001','stream':'it','branch':'Qspiders','age':'23','courseopted':'testing'},
    {'name':'pavan','rollno':98,'email':'pavan202@gmail.com','add':'pune','per':87,'YOP':2024,'DOB':'20-10-2002','stream':'ece','branch':'Qspiders','age':'22','courseopted':'testing'},
    {'name':'anjali','rollno':99,'email':'anjali303@gmail.com','add':'bangalore','per':90,'YOP':2025,'DOB':'08-03-2003','stream':'cs','branch':'Qspiders','age':'21','courseopted':'testing'},
    {'name':'yash','rollno':100,'email':'yash404@gmail.com','add':'hyd','per':89,'YOP':2023,'DOB':'31-05-2001','stream':'civil','branch':'Qspiders','age':'23','courseopted':'testing'}
]


# Create your views here.
def index(request):
    return render(request,'index.html',
    context={
        'data':students
        })

#gender,age,course_opted
def index1(request):
    return render(request,'index1.html',
    context={
        'data':students[35:70]
        })

def index2(request):
    return render(request,'index2.html',
    context={
        'data':students[70:101]
        })

def home(request):
    return render(request,'home.html')