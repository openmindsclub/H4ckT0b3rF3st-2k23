import time

class player :
    def __init__(self,health:int,firewood:str,food:str,survival_supplies:str,radio:str,lighter:int,pistol:str,knife:str):
        self.health = health
        self.firewood = firewood
        self.food = food
        self.survival_supplies = survival_supplies
        self.radio = radio
        self.lighter = lighter
        self.pistol = pistol
        self.knife = knife
    
    def get_health(self):
        return self.health
    
    def new_health(self):
        self.health = 0
        return self.health
    
    def get_food(self):
        return self.food
    
    def get_survival_supplies(self):
        return self.survival_supplies
    
    def get_firewood(self):
        return self.firewood
    
    def get_radio(self):
        return self.radio
    
    def get_lighter(self):
        return self.lighter
    
    def get_pistol(self):
        return self.pistol
    
    def get_knife(self):
        return self.knife
    
def exit_mission():
    print(f"Health : {agent_42.new_health()}\n")
    print("YOUR DEAD, \nMISSION FAILED!\n")
    reponse = str(input("Retry ? (yes/no)")).lower()
    
    if reponse == "yes" :
        play()
        
    else :
        exit()

def complete_mission():
    print("================================")
    time.sleep(1)
    
    print("MISSION COMPLETE:\n")
    print(f"Health : {agent_42.get_health()}\n")
    print(f"Survival Supplies: {agent_42.get_survival_supplies()}\n")
    print(f"Food: {agent_42.get_food()}\n")
    print("Radio : Working\n")
    print("Lighter: 60%\n")
    print("Pistol: 0 bullets\n")
    print("MISSION INTEL: LAB DOCUMENTS , LAB RESEARCH")
    
    

def test_radio():
    print("================================")
    time.sleep(1)
    
    print("HQ: Agent 42? Can you hear me! Over?\n1_YES! I can hear you!\n2_Keep Trying radio")
    
    reponse_6 = int(input("choose 1 or 2 ? : "))
    while reponse_6 != 1 and reponse_6 != 2 :
        reponse_6= str(input("invalid answer, give another response : ")).lower()
    
    if reponse_6 == 2 :
        test_radio()
    
    if reponse_6 == 1 :
        print("================================")
        time.sleep(1)
        
        print("HQ: Agent 42, we have been trying to make contact ever since we lost signal with your aircraft!\nHQ: How is your condition? Have you completed the Mission?")
        print("Agent 42: Yes I have located the secret lab and collected all valuable intelligence and require extraction.\n")
        print("HQ: Good Job 42, extraction is on route to your location.\n")
        print("*Extract* Mission Complete!\n")
        
        complete_mission()

    

def weapon_lab():
    print("================================")
    time.sleep(1)
    
    reponse_1 = str(input("do you want to investigate the turret ? :")).lower()
    while reponse_1 != "yes" :
        reponse_1 = str(input("do you want to investigate the turret ? :")).lower()
    print("DESTROYED: salvageable for parts\n")
    
    reponse_2 = str(input("do you want to take documents ? :")).lower()
    while reponse_2 != "yes" :
        reponse_2 = str(input("do you want to investigate the turret ? :")).lower()
    
    reponse_3 = str(input("do you want to take research ? :")).lower()
    while reponse_3 != "yes" :
        reponse_3 = str(input("do you want to take research ? :")).lower()
    

def lab_workbench():
    print("================================")
    time.sleep(1)
    
    reponse_4 = str(input("do you want to Restock on survival gear ? :")).lower()
    while reponse_4 != "yes" :
        reponse_4 = str(input("do you want to Restock on survival gear ? :")).lower()
    
    reponse_5 = str(input("do you want to repair Radio ? :")).lower()
    while reponse_5 != "yes" :
        reponse_5 = str(input("do you want to repair radio ? :")).lower()
    print("Radio Repaired TEST\n")
    
    test_radio()
    
    
def discover_secret_weapon():
    print("================================")
    time.sleep(1)
    
    print("This is it the secret weapons lab you have been looking for!\nNow that you have found the lab, you must gather all the possible intel and return home!\nThere may be a way for me to regain contact with HQ by repairing my radio with the tools available here.\n")
    print("================================")
    
    print("WEAPONS LAB:\n*INVESTIGATE THE TURRET*\n*TAKE DOCUMENTS*\n*TAKE RESEARCH*\n")
    weapon_lab()
    
    print("LAB WORKBENCH:\n*Repair Radio*\n*Restock on survival gear*\n")
    lab_workbench()
    
    

def after_turning_power_on():
    choice_8 = ["shoot","run"]
    print("================================")
    
    time.sleep(1)
    print("A turret emerges and is about to start shooting!\n")
    print("you have 5 seconds to get cover !\n")
    time.sleep(1)
    
    time_cover = time.time()
    
    choix_8 = str(input("1_*shoot* your pistol at the turret\n2_*run* away"))
    while choix_8 not in choice_8 :
        choix_8 = str(input("invalid answer, give another response : ")).lower()
        
    time_after_cover = time.time()
    
    cover = round(time_cover - time_after_cover,3)
    if cover >= 5 or choix_8 == "run" :
        exit_mission()
    elif cover < 5 and choix_8 == "shoot":
        print("Turret Destroyed\n")
        print("1_*Investigate* the lab.\n2_*run away*\n")
        
        decide = int(input("choose 1 or 2 ? :"))
        
        while decide != 1 and decide != 2 :
            decide = int(input("1 or 2 ? :"))
        
        if decide == 2 :
            print("You ran away and where unable to find the secret weopons lab...MISSION FAILED!\n")
            reponse = str(input("Retry ? (yes/no)")).lower()
            
            if reponse == "yes" :
                play()
            else :
                exit()
        
        if decide == 1 :
            discover_secret_weapon()
            

def enter_lab():
    print("================================")
    time.sleep(1)
    
    print("As you enter the lab, there is a control panal on the wall.\nCONTROL PANAL\n")
    str(input("go to control panal : ")).lower()
    
    str(input("TURN POWER *ON* : "))
    str(input("As you turn the power ON, you hear a loud BANG!\nA few seconds later all the lights in the lab turn on.\nAgent 42 eyes must adjusting to the light.\n*Open your eyes* ? : \n"))
    
    after_turning_power_on()
    

def after_opening_door():
    print("================================")
    time.sleep(1)
    
    print("As Agent 42 opens the door. He sees a laboratory of some sorts.\nThis could be the weopons lab you have been searching for.\n*Enter* to investigate the lab.\n")
    
    str(input("enter to investigate :")).lower()
    
    enter_lab()

def after_disarming():
    print("================================")
    time.sleep(1)
    
    print("Disarmed successfull!\n")
    print("*Open* and continue thought the big metal door.")
    input("press a button to open the door :")
    
    after_opening_door()
    

def attempt_to_disarm():
    print("================================")
    time.sleep(1)
    
    print("you have 3 seconds to disarm the mine !\n")
    time.sleep(1)
    start_time = time.time()
    input("press anything ! :")
    end_time = time.time()
    
    total_time = round(start_time - end_time,3)
    if total_time >= 3 :
        print("you run out of time !\n")
        exit_mission()
    elif total_time < 3 :
        after_disarming()

def look_closer():
    choice_7 = ["attempt to disarm","run"]
    
    print("================================")
    time.sleep(1)
    
    print("A massive, half open mechanical door, made of metal.\nAs you approach the door you hear a beeping noise.\n")
    print("You have spotted a Mine at the foot of the door. Do something.\n1_attempt to disarm\n2_turn and *run*!\n")
    
    choix_7 = str(input("what will you do ? :")).lower()
    while choix_7 not in choice_7 :
        choix_7 = str(input("invalid answer, give another response : ")).lower()
    
    if choix_7 == "run" :
        exit_mission()
    
    if choix_7 == "attempt to disarm" :
        attempt_to_disarm()
        

def explore_cave():
    print("================================")
    time.sleep(1)
    
    print(f"Health : {agent_42.get_health()}\n")
    print("After walking 100 meters into the cave Agent 42 hears the mechanical sounds again.\nAnother 50 meter into the cave you come across the source...*Look closer*\n")
    
    reponse = str(input("Look closer ? (yes/no):")).lower()
    while reponse != "yes" and reponse != "no" :
        reponse = str(input("invalid answer, give another response : ")).lower()
    
    if reponse == "no":
        exit_mission()
    
    if reponse == "yes" :
        look_closer()

def inventory_after_use_lighter():
    print("================================")
    time.sleep(1)
    
    print("INVENTORY:\n")
    print(f"Survival Supplies: {agent_42.get_survival_supplies()}(in use)\nFood: {agent_42.get_food()}\nRadio: Broken\nLighter: {agent_42.get_lighter() - 40}%\nPistol: {agent_42.get_pistol()}\nMISSION INTEL: 0 , 0\n")


def use_lighter():
    choice_6 = ["check your available supplies","uncover the source of the mechanical sounds"]
    
    print("================================")
    time.sleep(1)
    
    print(f"Health : {agent_42.get_health()}\n")
    print("*Inventory*\n")
    
    print("Now you have a source of light, you are able to descend further into the cave and *uncover the source of the mechanical sounds*, you heard over night.\n")
    
    choix_6 = str(input("select if you want to :\n1_check your available supplies\n2_uncover the source of the mechanical sounds\n"))
    while choix_6 not in choice_6 :
        choix_6 = str(input("invalid answer, give another response : ")).lower()
    
    if choix_6 == "check your available supplies" :
        inventory_after_use_lighter()
    
    print("================================")
    time.sleep(1)
    
    if choix_6 == "uncover the source of the mechanical sounds" :
        explore_cave()
    
    explore_cave()

def inventory_after_collecting_supplies():
    print("================================")
    time.sleep(1)
    
    print("INVENTORY:\n")
    
    print(f"Survival Supplies: {agent_42.get_survival_supplies()}\nFood: {agent_42.get_food()}\nRadio: Broken\nLighter: {agent_42.get_lighter() - 25}%\nPistol: {agent_42.get_pistol()}\nMISSION INTEL: 0 , 0\n")

def enter_cave():
    choice_5 = ["check your available supplies","use lighter to light the tourch stick"]
    
    print("================================")
    time.sleep(1)
    
    print(f"Health : {agent_42.get_health()}\n")
    print(f"Firewood: {agent_42.get_food()}\nFood: {agent_42.get_firewood()}\n")
    print("With the supplies collected, Agent 42 was able to survive the night and restore his health.\n")
    print("You gather your thing and must continue your mission to find the hidden weapon's lab.\n")
    print("With the remaining sticks from the camp fire, you where able to make a torch stick.\nCheck your available supplies.(new tourch stick available) *Inventory*\n")
    print("Over night you heard some odd mechanical sounds coming deep from within the cave. *Use lighter to light the tourch stick* and explore the cave.\n")
    
    choix_5 = str(input("select if you want to :\n1_check your available supplies\n2_use lighter to light the tourch stick\n")).lower()
    
    while choix_5 not in choice_5 :
        choix_5 = str(input("invalid answer, give another response : ")).lower()
    
    if choix_5 == "check your available supplies" :
        inventory_after_collecting_supplies()
    
    print("================================")
    time.sleep(1)
    
    if choix_5 == "use lighter to light the tourch stick" :
        use_lighter()
    
    use_lighter()
    
def start_looking_firewood():
    print("================================")
    time.sleep(1)
    
    print("After foraging the surrounding area, for about twenty minutes.\nAgent 42 has managed to gather some sticks to use to build a fire.\n")
    print(f"Firewood : {agent_42.get_firewood()}\n")
    print("*Go back* to the cave entrance\n")
    
    
def start_looking_food():
    print("================================")
    time.sleep(1)
    
    print("After searching the surrounding area for a few hours.\nAgent 42 comes across some rotten carcasses as well as some blue berry bushes..\n")
    print(f"Food : {agent_42.get_food()}\n")
    print("*Go back* to the cave entrance\n")
    

def start_looking():
    choice_4 = ["gather firewood","search for food","enter cave"]
    
    print("================================")
    time.sleep(1)
    
    print(f"Health : {agent_42.get_health()}\n")
    print("After walking thought the jungle for a few hours, agent 42 discovers the entrance to a cave.\nPossible Objectives:\n")
    print("*Gather* firewood: 0\n*Search* for food: 0\n")
    print("*Enter Cave* without food and fireWood\n")
    
    choix_4 = str(input("select if you want to start doing:\n1_Gathering firewood\n2_Searching for food\n3_Enter cave\n "))
    while choix_4 not in choice_4 :
        choix_4 = str(input("invalid answer, give another response : ")).lower()
        
    if choix_4 == "enter cave" :
        exit_mission()
        
    if choix_4 != "enter cave" and choix_4 in choice_4 :
        if choix_4 == "gather firewood" :
            start_looking_firewood()
            print("================================")
            time.sleep(1)
            
            print("after gathering the firewood, agent 42 will keep searching for some food\n")
            print(f"current firewood:{agent_42.get_firewood()}\n")
            
            start_looking_food()
            print("================================")
            time.sleep(1)
            
            print("After searching for the food, agent 42 returns to the cave\n")
            print(f"current food: {agent_42.get_food()}\n")
    
    
    if choix_4 != "enter cave" and choix_4 in choice_4 :
        if choix_4 == "search for food" :
            start_looking_food()
            print("================================")
            time.sleep(1)
            
            print("After searching for the food, agent 42 returns to the cave\n")
            print(f"current food: {agent_42.get_food()}\n")
            
            start_looking_firewood()
            print("================================")
            time.sleep(1)
            
            print("after gathering the firewood, agent 42 will keep searching for some food\n")
            print(f"current firewood:{agent_42.get_firewood()}\n")
            
    
    print("================================")
    
    print("After walking thought the jungle for a few hours, agent 42 discovers the entrance to a cave.\nPossible Objectives:\n")
    print(f"firewood: {agent_42.get_food()}\nfood: {agent_42.get_firewood()}\n")
    print("*Enter Cave* with your current supplies.\n")
    
    enter_cave()
    

def use_radio():
    choice_3 = ["keep Trying radio","start looking","wait for help"]
    
    print("================================")
    time.sleep(1)
    
    print(f"Health : {agent_42.get_health()}\n")
    print("No noise\n")
    print("*Keep Trying radio*")
    print("Night approches.\nWithout the necessary resources agent 42 may not survive the cold night.\n")
    print("*Start looking* for shelter & fire Wood.\nStay at the crash site and *wait for help*.\n")
    choix_3 = str(input("select if you want to :\n1_keep trying radio\n2_start looking\n3_wait for help\n "))
    
    while choix_3 not in choice_3 :
        choix_3 = str(input("invalid answer, give another response : ")).lower()
    
    if choix_3 == "wait for help" :
        exit_mission()
    elif choix_3 == "keep Trying radio" :
        use_radio()
    elif choix_3 == "start looking" :
        start_looking()
                
    
        
    
def start_mission():
    choice_2 = ["go back to sleep and give up","open your eyes"]
    
    print("================================")
    time.sleep(1)
    
    print("\nAgent 42 approaches the island. \nHis aircraft takes damage, losses power and crash lands. \nA few hours later, Agent 42 awakes!\n")
    print(f"Health : {agent_42.get_health() - 50}\n")
    
    print("1_go back to sleep and give up.\n2_open your eyes \n")
    choix_2 = str(input("select if you want to go back to sleep and give up or to open your eyes:\n")).lower()
    
    while choix_2 not in choice_2 :
        print("please insert another response")
        choix_2 = str(input()).lower()
    
    if choix_2 == choice_2[0] :
        exit_mission()
    
    elif choix_2 == choice_2[1] :
        print(f"Health : {agent_42.get_health() - 50}\n")
        print("Agent 42 tries to use his radio.\n")
        print("Use radio\n")
        use_radio()
        

agent_42 = player(100,"Bundle of sticks","A couple douzen blue berries","Tourch Stick","Broken",100,"Full Magazine of Bullets","Good state")
choice = ["start mission","abort the mission"]

def play():
    
    print("================================")
    time.sleep(1)
    
    print(f"Health : {agent_42.get_health()}")
    print("NAME: Agent 42 \nAGE: 32 \nGENDER: Male \nRACE/ETHNICITY: Caucasian\n")
    print("NOTES: \nAgent 42, one of the best the agency has ever trained. His skills are in his knowledge of survival techniques, making him the number one pick for this mission.")
    print("MISSION BRIEF: \nThe mission, explore an uncharted island located in the Pacific ocean. \nYou will be exploring the island in the hopes of finding a secret weapon's lab. \nGood Luck Agent.\n")
    print("EQUIPMENT: \nRadio, Lighter, Pistol, knife\n")
    
    print("1_start mission \n2_abort the mission\n")
    choix_1 = str(input("please select what do you want to choose :\n")).lower()
    
    while choix_1 not in choice :
        print("please insert another response")
        choix_1=str(input())
        
    if choix_1 == choice[1] :
        exit_mission()
    
    elif choix_1 == choice[0] :
        start_mission()

play()




