from bs4 import BeautifulSoup
import requests
import json
import csv

def Therapist_count_per_zipcode():
    
    wayne_county_zip = [48180, 48228,48126, 48187, 48185, 48235, 48188, 48183, 48111, 48219, 
                        48212, 48224, 48127, 48170, 48221, 48227, 48146, 48239, 48154, 48186, 
                        48124, 48234, 48205,48174,48152,48195, 48236, 48101, 48209, 48150, 48210, 
                        48135, 48141, 48223, 48238, 48192, 48167, 48168, 48203, 48125, 48204, 48134,
                        48213, 48207, 48214, 48240, 48184, 48193, 48201, 48206, 48225, 48202, 48230, 
                        48173, 48122, 48128, 48164, 48215, 48138, 48229, 48120, 48208, 48218, 48211,
                        48217, 48102, 48226, 48216, 48243, 48242, 48112, 48121, 48123, 48136, 48151,
                        48153, 48222, 48232, 48231, 48233, 48255, 48244, 48264, 48260, 48266, 48265,
                        48268, 48267, 48272, 48269, 48277, 48275, 48279, 48278, 48288]

    with open("Therapists_of_Wayne_County.csv", "w") as f:

        f.write("Zip Codes, Number of Therapists and Conselors\n")

        for zip in wayne_county_zip:

            url = "https://www.psychologytoday.com/us/therapists/" + str(zip)

            headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

            response = requests.get(url, headers=headers)

            soup = BeautifulSoup(response.content, 'html.parser')

            try:
                js_data = soup.head.find("script", {"data-hid": "gtm"})
                js_data = js_data.string.strip()
                start = js_data.find('push({"s')+5

                end = js_data.rfind("e}});")+3
                script_data = js_data[start:end]
                        

                json_data = json.loads(script_data)
                        
                            
                result_count = json_data['search']['resultCount']
            except:
                result_count = "NULL"

            f.write(str(zip)+ "," +str(result_count)+"\n")
            
            

print(Therapist_count_per_zipcode())



