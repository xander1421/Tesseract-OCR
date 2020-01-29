import pyautogui, time
import pytesseract as tess
import cv2
import imutils
import numpy as np

tess.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

############# # get the current location of the mouse pointer
def get_cursor_possition():
    position = pyautogui.position()
    time.sleep(3)
    print(position)

############################## take a screenshot of the Values
def take_screenshots():
    pyautogui.screenshot()  # returns a Pillow/PIL Image object
    pyautogui.screenshot('Screenshot_ROLES2.png')

##############
def get_smn_module():
    pyautogui.doubleClick(x=466, y=545) #location of SAP_SMN in SAP_GUI full screen
    # distance = 400
    time.sleep(4)

#######################
########## Press the maximize window button if its located
def check_if_needs_to_maximize():
    try:
        x, y = pyautogui.locateCenterOnScreen('foo.png')
        print(x,y)
        #Point(x=1559, y=38) test pos
        if x <= 1646 or y <=179:
            time.sleep(4)
            pyautogui.click(x, y)
    except TypeError as identifier:
        print('no need to maximize the window it has already started in maximized mode')
        print(identifier)
        pass

#######################
def user_login():
    # pyautogui.click('Screenshot_maximize_window.jpg')
    time.sleep(4)
    pyautogui.click(x=196, y=196) # ->  click on user_name login field 
    pyautogui.typewrite('USERNAME', interval=0.1)
    time.sleep(0.5)
    pyautogui.click(x=190, y=216) # click the password field
    pyautogui.typewrite('PASSWORD \n', interval=0.1)  # useful for entering text, newline ( /n ) is Enter
################################### GET transaction
def get_transaction():
    pyautogui.click(x=132, y=48) # click on the transaction code field
    time.sleep(0.9)
    pyautogui.typewrite('/nsu01 \n', interval=0.1)   # input the transaction code to copy one emp to another one
    time.sleep(0.9)
##################################################### Type the userFrom and the userTO
def copy_userFrom_and_userTO():
    pyautogui.click(x=105, y=194) # click on the user_original(from whom we will copy all the permissions) fiend
    time.sleep(0.5)
    pyautogui.typewrite('USERNAME', interval=0.1)   # input the EMPLOYEE USERNAME to copy from one emp to another one
    pyautogui.click(x=155, y=114) # Click the copy button
    pyautogui.click(x=342, y=404) # click on the user_original(from whom we will copy all the permissions) fiend
    time.sleep(0.5)
    pyautogui.typewrite('USERNAME', interval=0.1)   # input the EMPLOYEE USERNAME of the second user, to whom we will copy all the SAP permissions from
    pyautogui.click(x=380, y=723) # click the copy button
    time.sleep(0.9)

######################################################## Set-up the password
def setup_initial_password():
    pyautogui.click(x=198, y=349) # Click the password field
    time.sleep(0.9)
    pyautogui.typewrite('PASSWORD', interval=0.1) # type in the password
    pyautogui.press('tab') # press tab to get to the seccong password field
    pyautogui.typewrite('PASSWORD', interval=0.1) # type in the innitial password in the 2nd Field
    time.sleep(0.9)

######################################################### Adress tab in Navigation panel
def set_personal_details():
    pyautogui.click(x=58, y=218) # Click the Adress tab in Navigation panel
    time.sleep(0.9)
    pyautogui.click(x=135, y=304) # Click the Last name field
    time.sleep(0.9)
    pyautogui.hotkey('ctrl', 'a')# select all characters and clear the field
    pyautogui.typewrite('Last_name', interval=0.1) # type in the Last name
    pyautogui.press('tab') # press tab to get to First Name Field thats right bellow of Last name field
    pyautogui.typewrite('First_name', interval=0.1) # type in the First name
    pyautogui.click(x=138, y=591) # Click the E-mail field
    time.sleep(0.9)
    pyautogui.typewrite('USERNAME@EMAIL.COM', interval=0.1) # type in the E-mail

def set_SNC_name():
    pyautogui.click(x=208, y=217) # # Click TAB in Navigation panel
    pyautogui.click(x=140, y=371) # Click the E-mail field
    time.sleep(0.9)
    pyautogui.typewrite('p:' + 'USERNAME@EMAIL.COM', interval=0.1)
    
    

def get_Roles_tab():
    time.sleep(0.9)
    pyautogui.click(x=501, y=217) # # Click the ROLES tab in Navigation panel
    time.sleep(0.4)
    pyautogui.click(x=370, y=461)
    time.sleep(0.4)
    pyautogui.click(x=476, y=329) # Click the VALID TO DATES field
    

    try:
        x, y = pyautogui.locateCenterOnScreen('C:\\autoSAP\\images\\ROLES\\ROLE_NAME.png')
        print(x,y)
        while  True:
            # ads points to the x coordenate so it can click on the X to select the ROLE
            x,y = x - 192, y
            print('after chage: ', x,y)
            break
        time.sleep(4)
        pyautogui.click(x, y)

    except Exception as identifier:
        print('couldnt find it')
        print(identifier)
        pass

def all_points():
    # im = pyautogui.screenshot(region=(107, 380, 215, 21))
    button7location = pyautogui.locateOnScreen('C:\\autoSAP\\images\\ROLES\\ROLE_NAME2.png') # returns (left, top, width, height) of matching region
    print(button7location)
    #pyautogui.click(button7location)
####################
def get_roles_text_V1():
    pyautogui.click(x=476, y=329) # Click the VALID TO DATES field
    start = [107, 338, 216, 21]
    all_roles = []
    while True:
        im = pyautogui.screenshot(region=(start[0], start[1], start[2], start[3]))
        # time.sleep(0.9)
        text = tess.image_to_string(cv2.cvtColor(np.array(im), cv2.COLOR_BGR2GRAY))
        # text = text.replace("_", " ") # some of the text doesnt have all the _ (underscores)
        print(text)
        all_roles.append(text)
        start = [start[0], start[1] + start[3], start[2], start[3]]
        # print('this is all1', all_roles)
        if not text: # not text is an idiomatic way to say text == ''
            all_roles.pop() # remove the last value that returns empty always
            print('this is all2', all_roles)
            print(len(all_roles))
            return all_roles





def get_roles_text_V2():
    pyautogui.click(x=476, y=329) # Click the VALID TO DATES field
    start = [107, 338, 216, 21]
    all_roles = []
    while True:
        im = pyautogui.screenshot(region=(start[0], start[1], start[2], start[3]))
        # time.sleep(0.9)
        text = tess.image_to_string(cv2.cvtColor(np.array(im), cv2.COLOR_BGR2GRAY))
        text = text.replace("_", " ") # some of the text doesnt have all the _ (underscores)
        print(text)
        
        all_roles.append(text)
        start = [start[0], start[1] + start[3], start[2], start[3]]
        # print('this is all1', all_roles)
    if all_roles[-2] is text:
        print('yes')
        if not text: # not text is an idiomatic way to say text == ''
            print('this is all2', all_roles)
            print(len(all_roles))
            return all_roles





# take_screenshots()
# get_cursor_possition()
# ###########
# get_smn_module()
# check_if_needs_to_maximize()
# user_login() 
# get_transaction() 
# copy_userFrom_and_userTO()
# setup_initial_password()
# set_personal_details()
# set_SNC_name()
# get_Roles_tab()
# # all_points()
# #############
# get_roles_text_V1()
# get_roles_text_V2()


