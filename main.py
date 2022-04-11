import pandas as pd
import matplotlib.pyplot as plt
import webbrowser as wb
import os
import matplotlib.image as mpimg

def Campusgraph():
    x=["2015-16","2016-17","2017-18","2018-19","2019-20"]
    y=[48.18,58.02,68.89,84.4 ,81.85]
    plt.title("Placement Campus selection %")
    plt.xlabel('Years')
    plt.plot(x,y,color='red',linewidth=2,marker='D',markersize=5)
    plt.show()

os.system("cls")
print("****** Welcome  ******")
img = mpimg.imread('logo.jpg')
plt.imshow(img)
plt.show()

while(True):
    os.system("cls")
    print("**************************************************")
    print(" R C Patel Institute of Technology Shirpur, Dhule")
    print("      College Admission Process System")
    print("\n# Main Menu :)")
    print("\n     ENTER [1]:About us\n           [2]:Admission\n           [3]:Department\n           [4]:Placement Cell\n           [5]:Contact us\n           [6]:To view our College website\n           [7]:Exit\n")
    a=int(input("Enter Your Choice : "))
    #Option 1
    if(a==1):
        while(True):
            b=int(input("\nWhat do you want to know about us\n1.About Institute\n2.Our Patrons\n3.Scope of Engineering\n4.Approvals and Affilations\n5.Return to Menu\n"))
            if(b==1):
                print('''
                R. C. Patel Institute of Technology was set up as a part of the self-powered plans of Shirpur Education 
                \nSociety in 2001 with the objective to erect a truly world class institute in the rural part where students
                \nfrom the vicinity would be benefited from the services that matched global standards. RCPIT was conceived by 
                \nvisionary leader, Hon. Shri. Amrishbhai R. Patel, former cabinet minister for School Education, sports and 
                \nYouth Welfare for Maharashtra State. The institute has grown at a remarkable pace and has gone on to become 
                \nan institute of repute within the country. It is spread on lush green land providing an ambience congenial 
                \nto the pursuit of high quality technical education. Every single detail of the institute has been implemented 
                \nat par with global standards in accordance to the norms of AICTE, New Delhi. The strength of RCPIT lies in its 
                \nstate of art Laboratories, IIT virtual Classrooms & Laboratories, Digital Library, and an advanced workshop.
                \nThe success of RCPIT is largely attributed to the exuberant faculty members who are rich in qualification, high in 
                \nspirits, disciplined and devoted to the core. Perhaps the most productive and effective method of teaching and monitoring 
                \nis the one implemented at this institute, called - Tutor System, wherein, a batch of students are entrusted to a teacher for
                \nnot just instruction but as much for care, parenting and counseling. Problems faced by the students are thus resolved and even 
                \nthe head of the department pitches in to help. In addition there are periodical appraisal and evaluation of students and teachers  
                \n(by the students). This methodology ensures that the students feature in the University Merit List during each and every academic year.
                \nThe institute has highly qualified professionals from the reputed institutes like I.I.T.s who are devoted, committed and dedicated to the
                \ncore. Besides, they possess rich of experience in their respective streams and many of them have presented technical papers at National and International levels.
                \nRCPIT has a Memorandum of Understanding to facilitate and co-ordinate institute-industry interactions. Industry expert and technical staff work as a team with the
                \ninstitute's staff and participate in workshops, conferences and short courses. Students' vacations are effectively utilized by arranging them to work in the industry
                \nwith small incentives. The staff is involved in co-ordinating above interactions with the industry. The involvement of students under the guidance of faculty members
                \nfor undertaking industry-oriented projects is not only useful to the students and academic staff, but also to the promotion of interactive networking between the institute 
                \nand involved industries.
                ''')
            elif(b==2):
                wb.open("https://www.rcpit.ac.in/our-patrons")
            elif(b==3):
                print('''
                \nAs you know technical education plays a vital role in human resource development of the country by creating skilled manpower, enhancing industrial productivity, creating 
                \nself-employment and improving the quality of life. 70% population of India belongs to rural population. On the contradictory, only 23% of technical education has been 
                \ncontributed by the rural population. As per the NASSCOM report 10 millions of technical professionals are required by India by 2020, in IT sector itself, most of them
                \nwill be exported to Japan and USA. This has left major role and responsibility on the organizations/colleges like us to aware our rural students, to create fondness regarding 
                \ntechnical education and make them technically professionals to fulfill the industry demand.
                
                \nIndia produces the largest number of engineers. Even with such a huge qualified workforce generated annually from the engineering stream, the I.T industry is on an aggressive and
                \nincessant recruitment spree. Firstly it implies that there still exists a huge demand-supply gap and secondly it also raises a question about the quality of engineers produced in 
                \nterms of industry specific practical orientation. This presents a real challenge to the institutions offering Engineering degree to produce technically competent engineers. The dynamic
                \nnature of the profession calls for designing education programs with a global perspective. Bachelors degree in Engineering is still considered to be the most rewarding career option which 
                \nlays the foundation for imparting design and analytical skills required for the profession. The global scope of the profession has resulted in large scale transmigration inquest of greener 
                \npastures. Wherever one goes, what stands the test of time is the quality of education that has really unleashed the latent potential within and transformed it into a tangible skill. A very
                \nserious point of concern, especially in the Indian context, that needs attention is the accessibility of institutes to the rural population. Even meritorious students at times may face financial 
                \nconstraints or traveling problems to get enrolled into colleges in the metros. There are very few engineering colleges like us in the rural regions which offer quality education and which is worth 
                \nthe money spent.
                ''')
            elif(b==4):
                wb.open("https://www.rcpit.ac.in/approvals-and-affiliation")
            elif(b==5):
                break
            else:
                print('\ninvalid choice')
    #Option 2
    elif(a==2):
        while True:
            b=int(input("Select option\n1.Fees Structure\n2.To apply for Admission\n3.To see upadted of your data\n4.Return to main menu"))
            if(b==1):
                
                user_1=[
                     {"Caste":'OPEN','Tuition Fee':"90%",'Development Fee':"10%"},
                    {"Caste":'EBC','Tuition Fee':"50%",'Development Fee':"10%"},
                    {"Caste":'OBC','Tuition Fee':"50%",'Development Fee':"10%"},
                    {"Caste":'SC / SBC / NT / DT-VJ / ST','Tuition Fee':"0",'Development Fee':"10%"},
                     {"Caste":'TFWS','Tuition Fee':"0%",'Development Fee':"10%"}
                       ]
                data_1=[
            {'Interim Fee (Subject To Change) ':'First Year Engineering  ','Total(Tuition Fee & Development Fee )':"115000/-"}
                ]
                data_1=pd.DataFrame(data_1)
                user_1=pd.DataFrame(user_1)
                print("\n")
                print(data_1)
                print("\n")
                print(user_1)
            elif(b==2):
                data=pd.read_csv("addmission Students 1.csv")
                user=data.append({"Name OF Student":input("Enter name"),'Category':input("Category"),'SSC':input("Enter SSc score")
                                 ,'HSC':input("Enter HSc marks"),'CET Percentile':input("CET Percentile")
                                 ,'JEE Percentile':input('JEE Percentile'),'Preferred Branch 1st':input('Preferred Branch 1st')
                                 ,'Prefererred Branch 2nd':input("Prefererred Branch 2nd"),'Phone No':input('Phone No'),
                                 'Address':input("Address")},ignore_index=True)
            elif(b==3):
                print('\n')
                
                print(user)
            elif(b==4):
                break
            else:
                print('\n')
                print("\nInvalid choice")
            
    #Option 3
    elif(a==3):
        print('''\n
        DEPARTMENTS
        1.Computer Engineering
        2.Electronics & Telecommunication Engineering
        3.Mechanical Engineering
        4.Electrical Engineering
        5.Civil Engineering
        6.Computer Science & Engineering ( Data Science )
        7.Artificial Intelligence and Machine Learning
        8.Applied Sciences & Humanities
        9.Research Center
        ''')
        input("PRESS 'enter' to back...")
    #Option 4
    elif(a==4):
        while(True):
            b=int(input("\nWhat do you want to view\n1.About Placement Cell\n2.Placement Records\n3.Campus selection %\n4.Industry Association\n5.Return to Menu\n"))
            if(b==1):
                img = mpimg.imread('placement.jpg')
                imgplot = plt.imshow(img)
                plt.show()

            elif(b==2):
                user_2=[
                       {'Branch':'E & TC',"2019-20":68,'2018-19':55,'2017-18':60,'2016-17':79,'2015-16':50},
                       {'Branch':'Computer',"2019-20":118,'2018-19':125,'2017-18':60,'2016-17':69,'2015-16':48},
                       {'Branch':'IT',"2019-20":39,'2018-19':21,'2017-18':16,'2016-17':12,'2015-16':8},
                       {'Branch':'Mechanical',"2019-20":136 ,'2018-19':75,'2017-18':56,'2016-17':58,'2015-16':59},
                       {'Branch':'Electrical',"2019-20":47 ,'2018-19':53,'2017-18':45,'2016-17':39,'2015-16':26},
                       {'Branch':'Mechanical',"2019-20":136 ,'2018-19':75,'2017-18':56,'2016-17':58,'2015-16':59},
                       {'Branch':'Civil',"2019-20":7 ,'2018-19':28,'2017-18':18,'2016-17':25,'2015-16':21},
                       {'Branch':"Total","2019-20":418 ,'2018-19':357,'2017-18':255,'2016-17':282,'2015-16':212}

                       ]


                user_2=pd.DataFrame(user_2)
                print('\n')
                print(user_2)
            elif(b==3):
            #using graph method to print graph
                Campusgraph()
            elif(b==4):
                data=pd.read_csv("A.csv")
                print('\n')
                print(data)
            elif(b==5):
                break
            else:
                print("\nInvalid choice")
    #Option 5
    elif(a==5):
        while(True):
            b=int(input("\n1.OUR OFFICE LOCATION\n2.OUR CONTACT NUMBER\n3.OUR CONTACT E-MAIL\n4.Return to Main menu"))
            if(b==1):
                print("\nNear Nimzari Naka, Shahada Road,\nShirpur Dist. Dhule (M.S.) Maharashtra,\nIndia - 425405")
            elif(b==2):
                print("\n(02563)259600,801,802")
            elif(b==3):
                print("\ndirector@rcpit.ac.in")
            elif(b==4):
                break
            else:
                print("\nInvalid Choice")
    #Option 6
    elif(a==6):
        wb.open("https://www.rcpit.ac.in/")
    #Option 7
    elif(a==7):
        print("\n************Thanks for viewing our site************")
        break
    else:
        print("\nInvalid choice")