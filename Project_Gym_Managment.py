class Gym:
    member_data = {}
    BMI_tables = {
        'BMI1': {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Rest', 'Thu': 'Back', 'Fri': 'Triceps', 'Sat': 'Rest',
                 'Sun': 'Rest'},
        'BMI2': {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Cardio/Abs', 'Thu': 'Back', 'Fri': 'Triceps',
                 'Sat': 'Legs', 'Sun': 'Rest'},
        'BMI3': {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Abs/Cardio', 'Thu': 'Back', 'Fri': 'Triceps',
                 'Sat': 'Legs', 'Sun': 'Cardio'},
        'BMI4': {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Cardio', 'Thu': 'Back', 'Fri': 'Triceps',
                 'Sat': 'Cardio', 'Sun': 'Cardio'}}

    def __init__(self):
        print('Select option from below (Provide Index number): ')
        print('1:   Member Creation \n2:   Member Login\n3:   Super-User Login\n0:   Exit')
        val = input("Enter Selection: ")
        while True:
            print('')
            if val == '1':
                self.member_creation()
            elif val == '2':
                if self.member_data == {}:
                    print('There are no admission in gym till now.')
                else:
                    self.member_login()
            elif val == '3':
                self.super_user()
            elif val == '0':
                exit()
            print('\n1:   Member Creation \n2:   Member Login\n3:   Super-User Login\n0:   Exit')
            val = input("Enter Selection: ")

    def member_creation(self):
        def is_float(s):
            try:
                float(s)
                return True
            except ValueError:
                return False

        name = input('Full Mame: ')
        age = input('Age: ')
        gender = input('Gender: ')
        mobile_no = input('Mobile number: ')
        email = input('Email: ')
        bmi = input('BMI: ')
        while not is_float(bmi):
            bmi = input('Provide Proper BMI: ')
            if is_float(bmi):
                bmi = float(bmi)

        membership = input('Enter Membership Duration in Months (1, 3, 6 or 12): ')
        while membership not in ('1', '3', '6', '12'):
            membership = input('Enter membership duration in mentioned time period (1, 3, 6, 12): ')
        password = input('Enter Password(must be within 7 - 10 characters): ')
        while 7 > len(password) or len(password) > 10:
            password = input('Enter Password(must be within 7 - 10 characters): ')

        print('\nFull Name:', name, '\nAge: ', age, '\nGender: ', gender, '\nMobile number: ', mobile_no,
              '\nEmail: ', email, '\nBMI: ', bmi, '\nMembership Duration: ', membership, '\nPassword: ', password)
        confirmation = input('\nEnter 1 for confirmation, enter anything else to cancel: ')
        if confirmation == '1':
            self.member_data["{}".format(mobile_no)] = [name, age, gender, mobile_no, email, float(bmi), membership,
                                                        password]
            print('Welcome {}. You have been registered with our Gym. Login for more details.'.format(name))

    def member_login(self):
        contact_no = input('Enter contact number: ')
        login_password = input('Enter Password(enter 0 to exit): ')
        while True:
            if contact_no in self.member_data:
                if login_password == self.member_data[contact_no][7]:
                    break
                elif login_password == '0':
                    break
            print('\nContact No. or Password is wrong.')
            contact_no = input('Enter contact number: ')
            login_password = input('Enter Password(enter 0 to exit): ')
        if login_password == self.member_data[contact_no][7]:
            print('\n1:   View My Regimen\n2:   View My Profile\n3:   Update Profile\n4:   Logout')
            member_value = input('Select from Above: ')
            while member_value != '4':
                print('')
                if member_value == '1':
                    if self.member_data[contact_no][5] <= 18.5:
                        for j in self.BMI_tables['BMI1'].items():
                            print(j[0], ' : ', j[1])
                    elif 18.5 < self.member_data[contact_no][5] <= 25:
                        for j in self.BMI_tables['BMI2'].items():
                            print(j[0], ' : ', j[1])
                    elif 25 < self.member_data[contact_no][5] <= 30:
                        for j in self.BMI_tables['BMI3'].items():
                            print(j[0], ' : ', j[1])
                    elif 30 < self.member_data[contact_no][5]:
                        for j in self.BMI_tables['BMI4'].items():
                            print(j[0], ' : ', j[1])
                elif member_value == '2':
                    print('Full Name:', self.member_data[contact_no][0], '\nAge: ', self.member_data[contact_no][1],
                          '\nGender: ', self.member_data[contact_no][2], '\nMobile number: ',
                          self.member_data[contact_no][3],
                          '\nEmail: ', self.member_data[contact_no][4], '\nBMI: ', self.member_data[contact_no][5],
                          '\nMembership Duration: ', self.member_data[contact_no][6], '\nPassword: ',
                          self.member_data[contact_no][7])
                elif member_value == '3':
                    self.member_data.pop(contact_no)
                    self.member_creation()
                print('\n1:   View My Regimen\n2:   View My Profile\n3:   Update Profile\n4:    Logout')
                member_value = input('Select from Above: ')

    def super_user(self):
        print('1:   Create Member\n2:   View Member\n3:   Delete Member\n4:   Update Member\n5:   Create Regimen'
              '\n6:   View Regimen\n7:   Delete Regimen\n8:   Update Regimen\n9:   Logout')
        super_val = input('Select option from above: ')
        while super_val != '9':
            if super_val == '1':
                self.member_creation()
            elif super_val == '2':
                contact = input('Enter Contact number of Member: ')
                print('')
                if contact in self.member_data:
                    print('Full Name:', self.member_data[contact][0], '\nAge: ', self.member_data[contact][1],
                          '\nGender: ', self.member_data[contact][2], '\nMobile number: ',
                          self.member_data[contact][3],
                          '\nEmail: ', self.member_data[contact][4], '\nBMI: ', self.member_data[contact][5],
                          '\nMembership Duration: ', self.member_data[contact][6])
                else:
                    print('No data associated with provided contact number.')
            elif super_val == '3':
                contact = input('Enter Contact number of Member: ')
                if contact in self.member_data:
                    print('Full Name:', self.member_data[contact][0], '\nAge: ', self.member_data[contact][1],
                          '\nGender: ', self.member_data[contact][2], '\nMobile number: ',
                          self.member_data[contact][3],
                          '\nEmail: ', self.member_data[contact][4], '\nBMI: ', self.member_data[contact][5],
                          '\nMembership Duration: ', self.member_data[contact][6])
                    confirmation = input('\nEnter 1 for confirmation, enter anything else to cancel: ')
                    if confirmation == '1':
                        self.member_data.pop(contact)
                else:
                    print('No data associated with provided contact number.')
            elif super_val == '4':
                contact = input('Enter Contact number of Member: ')
                if contact in self.member_data:
                    self.member_data.pop(contact)
                    self.member_creation()
                else:
                    print('No data associated with provided contact number.')
            elif super_val == '5':
                self.create_regimen()
            elif super_val == '6':
                for number, i in enumerate(self.BMI_tables):
                    print(number + 1, ':   ' + i)
                selection = input('Select from above (Enter table title): ')
                while selection not in self.BMI_tables:
                    selection = input('Entered regimen table does not exist (Enter table title): ')
                for j in self.BMI_tables[selection].items():
                    print(j[0], ' : ', j[1])
            elif super_val == '7':
                for number, i in enumerate(self.BMI_tables):
                    print(number + 1, ':   ' + i)
                selection = input('Select from above (Enter table title): ')
                while selection not in self.BMI_tables:
                    selection = input('Entered regimen table does not exist (Enter table title): ')
                for j in self.BMI_tables[selection].items():
                    print(j[0], ' : ', j[1])
                confirmation = input('Enter 1 for confirmation/ enter anything else to cancel: ')
                if confirmation == '1':
                    self.BMI_tables.pop(selection)
            elif super_val == '8':
                for number, i in enumerate(self.BMI_tables):
                    print(number + 1, ':   ' + i)
                selection = input('Select from above (Enter table title): ')
                while selection not in self.BMI_tables:
                    selection = input('Entered regimen table does not exist (Enter table title): ')
                self.BMI_tables.pop(selection)
                self.create_regimen()
            print('\n1:   Create Member\n2:   View Member\n3:   Delete Member\n4:   Update Member\n5:   Create Regimen'
                  '\n6:   View Regimen\n7:   Delete Regimen\n8:   Update Regimen\n9:   Logout')
            super_val = input('Select option from above: ')

    def create_regimen(self):
        regimen_name = input('Enter Regimen Title: ')
        while regimen_name in self.BMI_tables:
            print('Table with given name already exists.')
            regimen_name = input('Enter New Regimen Title (Enter 0 to cancel): ')
            if regimen_name == '0':
                break
        mon = input('Mon Regimen: ')
        tue = input('Tue Regimen: ')
        wed = input('Wed Regimen: ')
        thu = input('Thu Regimen: ')
        fri = input('Fri Regimen: ')
        sat = input('Sat Regimen: ')
        sun = input('Sun Regimen: ')
        self.BMI_tables[regimen_name] = {'Mon': mon, 'Tue': tue, 'Wed': wed, 'Thu': thu, 'Fri': fri, 'sat': sat,
                                         'sun': sun}


Power_Zone = Gym()
