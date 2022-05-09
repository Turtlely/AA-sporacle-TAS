from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Amino Acid lookup table
AA = {
    -320:"threonine",
    -1920: "aspartic acid",
    -1120: "proline",
    -1600: "cysteine",
    -2880: "tyrosine",
    -3040: "valine",
    -0: "lysine",
    -1280: "asparagine",
    -800: "phenylalanine",
    -640: "leucine",
    -960: "glutamic acid",
    -2720: "alanine",
    -2400: "serine",
    -1440: "tryptophan",
    -1760: "glycine",
    -480: "histidine",
    -160: "glutamine",
    -2560: "arginine",
    -2240: "methionine",
    -2080: "isoleucine"
}

#initialize
driver = webdriver.Firefox()

#load up the window
driver.get("https://www.sporcle.com/games/sproutcm/amino-acids-from-structures")

restart = 'Y'

epochs = int(input("How many times do you want to do the TAS?"))
iteration = 0

while restart == 'Y':
    iteration +=1

    #refresh the page for multiple attempts
    driver.refresh()
    
    #give time to load elements
    time.sleep(1)

    #find and click start quiz button
    start_quiz = driver.find_element(By.ID,'button-play')
    start_quiz.click()

    #start the program timer for more accurate timing
    start_time = time.time()

    #locate the amino acid that is being selected, find its number, look in dictionary, send in the input
    for i in range(20):
        AminoAcid = driver.find_element(By.CSS_SELECTOR,".selected")
        boxes = AminoAcid.find_elements(By.XPATH, "*")

        position = 0

        #this part finds the "position" style element, uniquely denotes the amino acid that is selected

        #find "box" element
        for boxid in boxes:
            #find "name" element (the background_position:center element is here)
            names = boxid.find_elements(By.XPATH,"*")
            #print("box: "+ boxid.get_attribute("id"))
            
            for nameid in names:
                #print("name" + nameid.get_attribute("id"))
                if nameid.get_attribute("id")[0:4] == "name":
                    #select the child that has the "name" tag, there is also a "slot" and "extra" tag that you dont want to get
                    style= nameid.get_attribute("style")
                    #print("position"+position)

        #extracts the amino acid number from the style attribute
        Amino_number = int('-'+''.join(c for c in style if c.isdigit()))
        '123456'

        #find the entry box, type in the amino acid name, using the AA dictionary as a lookup
        driver.find_element(By.ID,"gameinput").send_keys(AA.get(Amino_number))

    #end the timer for this iteration
    end_time = time.time()

    #calculate the time it took for the iteration
    iter_time = end_time-start_time

    #report iteration number and time
    print("Iteration #"+ str(iteration) + ", Time: "+ str(iter_time))

    #automated restart
    if iteration >= epochs:
        restart = "N"

    #uncomment these two lines below to enable manual restarts
    #restart?
    #restart = input('Restart? Y/N')

#close the window when done
driver.close()
