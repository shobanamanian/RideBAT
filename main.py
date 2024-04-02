import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common import actions
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RideTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        time.sleep(2)

    def test_customer_login_check(self):
        driver = self.driver
        driver.get("http://localhost:4200/login")
        time.sleep(2)
        driver.set_window_size(300,700,"current")
        # driver.maximize_window()
        time.sleep(2)
        new = driver.find_element(By.XPATH,'/html/body/app-root/app-login/div/div[1]/div[3]/a')
        new.click()
        time.sleep(2)
        nick_name = driver.find_element(By.XPATH, '/html/body/app-root/app-signup/div/div[1]/form/div/div[1]/input')
        nick_name.send_keys("shobana")
        time.sleep(2)
        mobile_number = driver.find_element(By.XPATH,
                                            '/html/body/app-root/app-signup/div/div[1]/form/div/div[2]/div/input[2]')
        mobile_number.send_keys("8675596400")
        time.sleep(2)
        terms = driver.find_element(By.XPATH, '/html/body/app-root/app-signup/div/div[1]/form/div/div[3]/input')
        terms.click()
        time.sleep(2)
        next = driver.find_element(By.XPATH, '/html/body/app-root/app-signup/div/div[1]/div[3]/button')
        next.click()
        time.sleep(2)
        # back = driver.find_element(By.XPATH, '/html/body/app-root/app-signup-authentication/div/div[1]/div[1]/button')
        # back.click()
        otp1 = driver.find_element(By.XPATH, '/html/body/app-root/app-signup-authentication/div/div[1]/form/div/input[1]')
        otp1.send_keys("2")
        otp2 = driver.find_element(By.XPATH, '/html/body/app-root/app-signup-authentication/div/div[1]/form/div/input[2]')
        otp2.send_keys("9")
        otp3 = driver.find_element(By.XPATH, '/html/body/app-root/app-signup-authentication/div/div[1]/form/div/input[3]')
        otp3.send_keys("6")
        otp4 = driver.find_element(By.XPATH, '/html/body/app-root/app-signup-authentication/div/div[1]/form/div/input[4]')
        otp4.send_keys("0")
        # submit = driver.find_element(By.XPATH, '/html/body/app-root/app-signup-authentication/div/div[1]/div[3]/button')
        # submit.click()
        # time.sleep(2)
        # country_code = driver.find_element(By.XPATH,'/html/body/app-root/app-login/div/div[1]/div[2]/div[1]/input')
        # country_code.send_keys("91")
        # time.sleep(2)
        driver = self.driver
        driver.get("http://localhost:4200/login")
        time.sleep(2)
        driver.set_window_size(300, 700, "current")
        # driver.maximize_window()
        time.sleep(2)
        mobile_number = driver.find_element(By.XPATH,'/html/body/app-root/app-login/div/div[1]/form/div/div[2]/input')
        mobile_number.send_keys("8675596400")
        time.sleep(2)
        # next = driver.find_element(By.XPATH,'/html/body/app-root/app-login/div/div[1]/div[2]/button')
        # next.click()
        # time.sleep(2)
        # otp1 = driver.find_element(By.XPATH, '/html/body/app-root/app-authentication/div/div[1]/form/div/input[1]')
        # otp1.send_keys("2")
        # otp2 = driver.find_element(By.XPATH, '/html/body/app-root/app-authentication/div/div[1]/form/div/input[2]')
        # otp2.send_keys("9")
        # otp3 = driver.find_element(By.XPATH, '/html/body/app-root/app-authentication/div/div[1]/form/div/input[3]')
        # otp3.send_keys("6")
        # otp4 = driver.find_element(By.XPATH, '/html/body/app-root/app-authentication/div/div[1]/form/div/input[4]')
        # otp4.send_keys("0")
        # submit = driver.find_element(By.XPATH, '/html/body/app-root/app-authentication/div/div[1]/div[3]/button')
        # submit.click()
        # time.sleep(2)

        # driver = self.driver
        # driver.get("http://localhost:4200/choose-vehicle")
        # time.sleep(2)
        # driver.set_window_size(300, 700, "current")
        # time.sleep(2)
        # payment = driver.find_element(By.CLASS_NAME,'down-icon')
        # payment.click()
        # time.sleep(2)



        driver = self.driver
        driver.get("http://localhost:4200/destination")
        time.sleep(2)
        driver.set_window_size(300,700,"current")
        time.sleep(2)
        back = driver.find_element(By.XPATH,'/html/body/app-root/app-setting-destination-page/div/div/div[1]/button')
        back.click()
        time.sleep(2)
        driver = self.driver
        driver.get("http://localhost:4200/home")
        time.sleep(2)
        driver.set_window_size(300, 700, "current")
        time.sleep(2)
        your_location = driver.find_element(By.XPATH, '/html/body/app-root/app-home-page/div/div/div[1]/div/input')
        your_location.send_keys("velacherry")
        time.sleep(2)

        driver = self.driver
        driver.get("http://localhost:4200/destination")
        time.sleep(2)
        driver.set_window_size(300, 700, "current")
        time.sleep(2)
        your_location = driver.find_element(By.XPATH,'/html/body/app-root/app-setting-destination-page/div/div/form/div/div[1]/input')
        your_location.send_keys("kelambakkam")
        time.sleep(2)
        drop = driver.find_element(By.XPATH,'/html/body/app-root/app-setting-destination-page/div/div/form/div/div[2]/input')
        drop.send_keys("velacherry")
        time.sleep(2)





        driver = self.driver
        driver.get("http://localhost:4200/driver-login")
        time.sleep(2)
        driver.set_window_size(300, 700, "current")
        time.sleep(2)

        new = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-login/div/div[1]/div[3]/a')
        new.click()
        nick_name = driver.find_element(By.XPATH, '/html/body/app-root/app-driver-signup/div/div[1]/form/div/div[1]/input')
        nick_name.send_keys("raja")
        time.sleep(2)
        mobile_number = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-signup/div/div[1]/form/div/div[2]/div/input[2]')
        mobile_number.send_keys("8675596400")
        time.sleep(2)
        terms = driver.find_element(By.XPATH, '/html/body/app-root/app-driver-signup/div/div[1]/form/div/div[3]/input')
        terms.click()
        time.sleep(2)
        next = driver.find_element(By.XPATH, '/html/body/app-root/app-driver-signup/div/div[1]/div[3]/button')
        next.click()
        time.sleep(2)

        otp1 = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-signup-authentication/div/form/div[1]/div[3]/input[1]')
        otp1.send_keys("5")
        otp2 = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-signup-authentication/div/form/div[1]/div[3]/input[2]')
        otp2.send_keys("7")
        otp3 = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-signup-authentication/div/form/div[1]/div[3]/input[3]')
        otp3.send_keys("0")
        otp4 = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-signup-authentication/div/form/div[1]/div[3]/input[4]')
        otp4.send_keys("2")
        # submit = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-signup-authentication/div/form/div[1]/div[4]/button')
        # submit.click()
        # time.sleep(2)




        driver = self.driver
        driver.get("http://localhost:4200/driver-login")
        time.sleep(2)
        driver.set_window_size(300, 700, "current")
        time.sleep(2)
        mobile_number = driver.find_element(By.XPATH,
                                            '/html/body/app-root/app-driver-login/div/div[1]/form/div/div[2]/input')
        mobile_number.send_keys("8675596400")
        time.sleep(2)
        # next = driver.find_element(By.XPATH, '/html/body/app-root/app-driver-login/div/div[1]/div[2]/button')
        # next.click()
        # time.sleep(2)
        # otp1 = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-login-authentication/div/div[1]/form/div/input[1]')
        # otp1.send_keys("8")
        # otp2 = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-login-authentication/div/div[1]/form/div/input[2]')
        # otp2.send_keys("8")
        # otp3 = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-login-authentication/div/div[1]/form/div/input[3]')
        # otp3.send_keys("6")
        # otp4 = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-login-authentication/div/div[1]/form/div/input[4]')
        # otp4.send_keys("5")
        # time.sleep(2)
        # submit = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-login-authentication/div/div[1]/div[3]/button')
        # submit.click()
        # time.sleep(3)
        #
        # back = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-login-authentication/div/div[1]/div[1]/button')
        # back.click()
        # time.sleep(2)

        driver = self.driver
        driver.get("http://localhost:4200/further-details")
        time.sleep(2)
        driver.set_window_size(300, 700, "current")
        time.sleep(2)
        action = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-further-details/div/div[1]/form/div/div[1]/select')
        action.click()
        time.sleep(2)
        action = driver.find_elements(By.TAG_NAME,'option')
        action[1].click()
        time.sleep(2)
        email_id = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-further-details/div/div[1]/form/div/div[2]/input')
        email_id.send_keys("shobana@gmail.com")
        time.sleep(2)
        languages = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-further-details/div/div[1]/form/div/div[3]/input')
        languages.send_keys("tamil")
        time.sleep(2)
        submit = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-further-details/div/div[1]/div[2]/button')
        submit.click()
        time.sleep(2)
    #
    # #
    # # # def test_upload_documents_check(self):
    # #     driver = self.driver
    # #     driver.get("http://localhost:4200/driver-documents")
    # #     time.sleep(2)
    # #     driver.set_window_size(300, 700, "current")
    # #     time.sleep(2)
    # #
    # #     image_path = "D://tree-736885_1280.jpg"
    # #     driver.find_element(By.XPATH,'/html/body/app-root/app-driver-documents/div/div/form/div/div[1]/input').send_keys(image_path)
    # #     time.sleep(2)
    # #
    # #     image_path ="D://1.jpg"
    # #     driver.find_element(By.XPATH,'/html/body/app-root/app-driver-documents/div/div/form/div/div[2]/input').send_keys(image_path)
    # #     time.sleep(2)
    # #     image_path = "D://tree-736885_1280.jpg"
    # #     driver.find_element(By.XPATH,'/html/body/app-root/app-driver-documents/div/div/form/div/div[3]/input').send_keys(image_path)
    # #     time.sleep(2)
    # #     image_path = "D://3.jpg"
    # #     driver.find_element(By.XPATH,'/html/body/app-root/app-driver-documents/div/div/form/div/div[4]/input').send_keys(image_path)
    # #     time.sleep(2)
    # #     image_path = "D://tree-736885_1280.jpg"
    # #     driver.find_element(By.XPATH,'/html/body/app-root/app-driver-documents/div/div/form/div/div[5]/input').send_keys(image_path)
    # #     time.sleep(2)
    # #     image_path = "D://6.jpg"
    # #     driver.find_element(By.XPATH,'/html/body/app-root/app-driver-documents/div/div/form/div/div[6]/input').send_keys(image_path)
    # #     time.sleep(2)
    # #     submit = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-documents/div/div/div[2]/button')
    # #     submit.click()
    # #     time.sleep(2)
    #
    # #
    #     driver = self.driver
    #     driver.get("http://localhost:4200/image-upload")
    #     time.sleep(2)
    #     driver.set_window_size(300, 700, "current")
    #     time.sleep(2)
    #     image_path = "D://tree-736885_1280.jpg"
    #     driver.find_element(By.XPATH,'/html/body/app-root/app-profile-image-upload-page/div/div/div[6]/input').send_keys(image_path)
    #     time.sleep(2)
    #     submit = driver.find_element(By.XPATH,'/html/body/app-root/app-profile-image-upload-page/div/div/div[6]/button')
    #     submit.click()
    #     time.sleep(2)
    #
    #     driver = self.driver
    #     driver.get("http://localhost:4200/licence-upload")
    #     time.sleep(2)
    #     driver.set_window_size(300, 700, "current")
    #     time.sleep(2)
    #     licence_number = driver.find_element(By.XPATH,'/html/body/app-root/app-license-upload-page/div/div/form/div/div[1]/input')
    #     licence_number.send_keys("LTr45673")
    #     time.sleep(2)
    #     date_of_birth = driver.find_element(By.XPATH,'/html/body/app-root/app-license-upload-page/div/div/form/div/div[2]/input')
    #     date_of_birth.send_keys("06/23/2024")
    #     time.sleep(2)
    #     submit = driver.find_element(By.XPATH,'/html/body/app-root/app-license-upload-page/div/div/div[3]/button')
    #     submit.click()
    #     time.sleep(2)
    #
    #     driver = self.driver
    #     driver.get("http://localhost:4200/aadharcard-upload")
    #     time.sleep(2)
    #     driver.set_window_size(300, 700, "current")
    #     time.sleep(2)
    #     image_path = "D://6.jpg"
    #     driver.find_element(By.XPATH,'/html/body/app-root/app-aadharcard-upload-page/div/div/div[5]/input').send_keys(image_path)
    #     time.sleep(2)
    #     submit = driver.find_element(By.XPATH,'/html/body/app-root/app-aadharcard-upload-page/div/div/div[5]/button')
    #     submit.click()
    #     time.sleep(2)
    #
    #     driver = self.driver
    #     driver.get("http://localhost:4200/rc-upload")
    #     time.sleep(2)
    #     driver.set_window_size(300, 700, "current")
    #     time.sleep(2)
    #     licence_plate_number = driver.find_element(By.XPATH,'/html/body/app-root/app-rc-upload/div/div/div[4]/div[1]/input')
    #     licence_plate_number.send_keys("56473")
    #     time.sleep(2)
    #     submit = driver.find_element(By.XPATH,'/html/body/app-root/app-rc-upload/div/div/div[5]/button')
    #     submit.click()
    #     time.sleep(2)
    #
    #     driver = self.driver
    #     driver.get("http://localhost:4200/insurance-upload")
    #     time.sleep(2)
    #     driver.set_window_size(300, 700, "current")
    #     time.sleep(2)
    #     image_path = "D://3.jpg"
    #     driver.find_element(By.XPATH, '/html/body/app-root/app-insurance-page/div/div/div[5]/input').send_keys(image_path)
    #     time.sleep(2)
    #     submit = driver.find_element(By.XPATH, '/html/body/app-root/app-insurance-page/div/div/div[5]/button')
    #     submit.click()
    #     time.sleep(2)
    #
    #     driver = self.driver
    #     driver.get("http://localhost:4200/permit-upload")
    #     time.sleep(2)
    #     driver.set_window_size(300, 700, "current")
    #     time.sleep(2)
    #     image_path = "D://1.jpg"
    #     driver.find_element(By.XPATH, '/html/body/app-root/app-permit-upload-page/div/div/div[5]/input').send_keys(image_path)
    #     time.sleep(2)
    #     submit = driver.find_element(By.XPATH, '/html/body/app-root/app-permit-upload-page/div/div/div[5]/button')
    #     submit.click()
    #     time.sleep(2)

        driver = self.driver
        driver.get("http://localhost:4200/settings")
        time.sleep(2)
        driver.set_window_size(300, 700, "current")
        time.sleep(2)
        profile = driver.find_element(By.XPATH,'/html/body/app-root/app-settings/div/div/div[2]/ul/li[1]/a')
        profile.click()
        time.sleep(2)
        phone_number = driver.find_element(By.XPATH,'/html/body/app-root/app-profile/div/div/div[2]/div[2]/div[1]/div[2]/a')
        phone_number.click()
        time.sleep(2)
        phone_number = driver.find_element(By.XPATH,'/html/body/app-root/app-profile/div[2]/div/form[1]/div/input[2]')
        phone_number.send_keys("8675596400")
        time.sleep(2)
        otp1 = driver.find_element(By.XPATH,'/html/body/app-root/app-profile/div[2]/div/form[2]/div/div[1]/input[1]')
        otp1.send_keys("2")
        otp2 = driver.find_element(By.XPATH,'/html/body/app-root/app-profile/div[2]/div/form[2]/div/div[1]/input[2]')
        otp2.send_keys("5")
        otp3 = driver.find_element(By.XPATH,'/html/body/app-root/app-profile/div[2]/div/form[2]/div/div[1]/input[3]')
        otp3.send_keys("8")
        otp4 = driver.find_element(By.XPATH,'/html/body/app-root/app-profile/div[2]/div/form[2]/div/div[1]/input[4]')
        otp4.send_keys("6")

        # submit = driver.find_element(By.XPATH,'/html/body/app-root/app-profile/div[2]/div/div[3]/button')
        # submit.click()
        # time.sleep(2)
        close = driver.find_element(By.XPATH,'/html/body/app-root/app-profile/div[2]/div/div[1]/button')
        close.click()
        time.sleep(2)
        email= driver.find_element(By.XPATH,'/html/body/app-root/app-profile/div/div/div[2]/div[2]/div[2]/div[2]/a')
        email.click()
        time.sleep(2)
        email = driver.find_element(By.XPATH,'/html/body/app-root/app-profile/div[2]/div/div[3]/input')
        email.send_keys("shobana123@gmail.com")
        time.sleep(2)

        otp1 = driver.find_element(By.XPATH, '/html/body/app-root/app-profile/div[2]/div/form/div/div[1]/input[1]')
        otp1.send_keys("0")
        otp2 = driver.find_element(By.XPATH, '/html/body/app-root/app-profile/div[2]/div/form/div/div[1]/input[2]')
        otp2.send_keys("9")
        otp3 = driver.find_element(By.XPATH, '/html/body/app-root/app-profile/div[2]/div/form/div/div[1]/input[3]')
        otp3.send_keys("1")
        otp4 = driver.find_element(By.XPATH, '/html/body/app-root/app-profile/div[2]/div/form/div/div[1]/input[3]')
        otp4.send_keys("6")

        close = driver.find_element(By.XPATH,'/html/body/app-root/app-profile/div[2]/div/div[1]/button')
        close.click()
        time.sleep(2)
        authentication = driver.find_element(By.XPATH,'/html/body/app-root/app-profile/div/div/div[2]/div[2]/div[3]/div[2]/a')
        authentication.click()
        time.sleep(2)
        no = driver.find_element(By.XPATH,'/html/body/app-root/app-profile/div[2]/div/div[4]/div[2]/input')
        no.click()
        time.sleep(2)
        close = driver.find_element(By.XPATH,'/html/body/app-root/app-profile/div[2]/div/div[1]/button')
        close.click()
        time.sleep(2)
        back = driver.find_element(By.CLASS_NAME,'back-btn')
        back.click()
        time.sleep(2)

        driver = self.driver
        driver.get("http://localhost:4200/driver-documents")
        time.sleep(2)
        driver.set_window_size(300,700,"current")
        time.sleep(2)
        license_front = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-documents/div/div/form/div/div[1]/button')
        license_front.click()
        time.sleep(2)
        license_number = driver.find_element(By.XPATH,'/html/body/app-root/app-license-upload-page/div/div/form/div/div[1]/input')
        license_number.send_keys("LTR4536")
        time.sleep(2)
        dob = driver.find_element(By.XPATH,'/html/body/app-root/app-license-upload-page/div/div/form/div/div[2]/input')
        dob.send_keys("06/23/2024")
        image_path = "D://1.jpg"
        driver.find_element(By.XPATH,'/html/body/app-root/app-license-upload-page/div/div/form/div/div[3]/input').send_keys(image_path)
        time.sleep(2)
        submit = driver.find_element(By.XPATH,'/html/body/app-root/app-license-upload-page/div/div/div[3]/button')
        submit.click()
        profile_picture = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-documents/div/div/form/div/div[2]/button')
        profile_picture.click()
        time.sleep(2)
        image_path = "D://3.jpg"
        driver.find_element(By.XPATH,'/html/body/app-root/app-profile-image-upload-page/div/div/form/div[4]/input').send_keys(image_path)
        time.sleep(2)
        submit = driver.find_element(By.XPATH,'/html/body/app-root/app-profile-image-upload-page/div/div/div[3]/button')
        submit.click()
        time.sleep(2)


        aadhar_front = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-documents/div/div/form/div/div[3]/button')
        aadhar_front.click()
        time.sleep(2)
        image_path = "D://4.jpg"
        driver.find_element(By.XPATH, '/html/body/app-root/app-aadharcard-upload-page/div/div/form/div[3]/input').send_keys(image_path)
        time.sleep(2)
        submit = driver.find_element(By.XPATH, '/html/body/app-root/app-aadharcard-upload-page/div/div/div[3]/button')
        submit.click()
        time.sleep(2)
        rc = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-documents/div/div/form/div/div[4]/button')
        rc.click()
        time.sleep(2)
        license_plate_number = driver.find_element(By.XPATH,'/html/body/app-root/app-rc-upload/div/div/form/div[2]/div[1]/input')
        license_plate_number.send_keys("457348")
        time.sleep(2)
        image_path = "D://6.jpg"
        driver.find_element(By.XPATH,'/html/body/app-root/app-rc-upload/div/div/form/div[2]/div[2]/input')
        time.sleep(2)
        submit = driver.find_element(By.XPATH,'/html/body/app-root/app-rc-upload/div/div/div[3]/button')
        submit.click()
        time.sleep(2)
        vehicle = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-documents/div/div/form/div/div[5]/button')
        vehicle.click()
        time.sleep(2)
        image_path = "D://1.jpg"
        driver.find_element(By.XPATH,'/html/body/app-root/app-permit-upload-page/div/div/form/div[3]/input').send_keys(image_path)
        time.sleep(2)
        # submit = driver.find_element(By.XPATH,'/html/body/app-root/app-driver-documents/div/div/div[2]/button')
        # submit.click()
        # time.sleep(2)



    # def test_admin_login_check(self):
    #     # driver = self.driver
    #     # driver.get("http://localhost:4200/admin-login")
    #     # time.sleep(2)
    #     # driver.set_window_size(300,700,"current")
    #     # time.sleep(2)
    #     # mobile_number = driver.find_element(By.XPATH,'/html/body/app-root/app-admin-login/div/div[1]/form/div/div/div[1]/input[2]')
    #     # mobile_number.send_keys("8675596400")
    #     # time.sleep(2)
    #     # send_otp = driver.find_element(By.XPATH,'/html/body/app-root/app-admin-login/div/div[1]/form/div/div/div[2]/button')
    #     # send_otp.click()
    #     # time.sleep(2)
    #     #
    #     # otp1 = driver.find_element(By.XPATH,'/html/body/app-root/app-admin-login/div/div[1]/div[2]/form/div/input[1]')
    #     # otp1.send_keys("3")
    #     # otp2 = driver.find_element(By.XPATH,'/html/body/app-root/app-admin-login/div/div[1]/div[2]/form/div/input[2]')
    #     # otp2.send_keys("3")
    #     # otp3 = driver.find_element(By.XPATH,'/html/body/app-root/app-admin-login/div/div[1]/div[2]/form/div/input[3]')
    #     # otp3.send_keys("9")
    #     # otp4 = driver.find_element(By.XPATH,'/html/body/app-root/app-admin-login/div/div[1]/div[2]/form/div/input[4]')
    #     # otp4.send_keys("1")
    #     # time.sleep(2)
    #     # verify = driver.find_element(By.XPATH,'/html/body/app-root/app-admin-login/div/div[1]/div[2]/div/button')
    #     # verify.click()
    #     # time.sleep(2)
    #
    #
        driver= self.driver
        driver.get("http://localhost:4200/superadmin")
        time.sleep(2)
        # driver.set_window_size(300,700,"current")
        driver.maximize_window()
        time.sleep(2)
        customer = driver.find_element(By.CLASS_NAME,'icon')
        customer.click()
        time.sleep(2)
        view_all_customer = driver.find_element(By.XPATH,'/html/body/app-root/app-dashboard/div/div[1]/app-nav-bar/div/nav/div[1]/div[2]/ul/li[2]/a[1]')
        view_all_customer.click()
        time.sleep(10)

        email_id = driver.find_element(By.XPATH,'/html/body/app-root/app-dashboard/div/div[2]/app-customer-details/div/div/div[2]/div[1]/input')
        email_id.send_keys("shobana")
        time.sleep(10)
        # from_date = driver.find_element(By.XPATH,'/html/body/app-root/app-dashboard/div/div[2]/app-customer-details/div/div/div[2]/div[2]/input')
        # from_date.send_keys("08/22/2024")
        # time.sleep(2)
        # to_date = driver.find_element(By.XPATH,'/html/body/app-root/app-dashboard/div/div[2]/app-customer-details/div/div/div[2]/div[3]/input')
        # to_date.send_keys("09/16/2024")
        # time.sleep(2)
        # edit = driver.find_element(By.XPATH,'/html/body/app-root/app-dashboard/div/div[2]/app-customer-details/div/div/div[3]/table/tbody/tr[1]/td[6]/div/svg[2]')
        # edit.click()
        name = driver.find_element(By.XPATH,'/html/body/app-root/app-dashboard/div/div[2]/app-customer-details/div/app-edit-customer/div/div/form/div/div[1]/input')
        name.clear()
        name.send_keys("shobana")
        time.sleep(2)
        email = driver.find_element(By.XPATH,'/html/body/app-root/app-dashboard/div/div[2]/app-customer-details/div/app-edit-customer/div/div/form/div/div[2]/input')
        email.clear()
        email.send_keys("shobana@gmail.com")
        time.sleep(2)
        mobile_number = driver.find_element(By.XPATH,'/html/body/app-root/app-dashboard/div/div[2]/app-customer-details/div/app-edit-customer/div/div/form/div/div[3]/input')
        mobile_number.clear()
        mobile_number.send_keys("9787124968")
        time.sleep(2)
        is_verified = driver.find_element(By.XPATH,'/html/body/app-root/app-dashboard/div/div[2]/app-customer-details/div/app-edit-customer/div/div/form/div/div[4]/select')
        is_verified.click()
        time.sleep(2)
        action = driver.find_elements(By.TAG_NAME, 'option')
        action[0].click()
        time.sleep(2)

        is_active = driver.find_element(By.XPATH,'/html/body/app-root/app-dashboard/div/div[2]/app-customer-details/div/app-edit-customer/div/div/form/div/div[5]/select')
        is_active.click()
        time.sleep(2)
        action = driver.find_elements(By.TAG_NAME,'option')
        action[0].click()
        submit = driver.find_element(By.XPATH,'/html/body/app-root/app-dashboard/div/div[2]/app-customer-details/div/app-edit-customer/div/div/form/div/div[8]/button')
        submit.click()
        time.sleep(2)

        delete = driver.find_element(By.CLASS_NAME,'delete-icon')
        delete.click()
        time.sleep(2)
        proceed = driver.find_element(By.XPATH,'/html/body/app-root/app-dashboard/div/div[2]/app-customer-details/div/app-delete-customer/div/div/div[3]/button')
        proceed.click()
        time.sleep(2)
        close = driver.find_element(By.XPATH,'/html/body/app-root/app-dashboard/div/div[2]/app-customer-details/div/div[2]/div/div[1]/button')
        close.click()
        time.sleep(2)













unittest.main()





