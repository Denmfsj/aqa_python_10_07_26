# DRY - dont repeat yourself


class BasePhone:

    def __init__(self, model, color, disc):
        self.model = model
        self.color = color
        self.disc = disc

    def send_sms(self, number, text):
         print(f'sending sms \n{text}\nTo: {number}')


class IPhone(BasePhone):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)  # BasePhone.__init__(model, color, disc)

    def __init__(self, model, color, disc):
        super().__init__(model, color, disc)  # BasePhone.__init__(model, color, disc)
        self.installed_apps = []

    def download_from_appstore(self, app_name: str):
        self.installed_apps.append(app_name)

    def send_sms(self, number, text):

        if 'iMessage' in self.installed_apps:
            print(f'sending sms via iMessage \n{text}\nTo: {number}')
        else:
            super().send_sms(number, text)


class Samsung(BasePhone):

    def download_from_googleplay(self, app_name: str):
        pass



class Nokia(BasePhone):

    def __init__(self, model, color, disc):
        super().__init__(model=model, color=color, disc=2)  # BasePhone.__init__(model, color, disc)



iphone_15 = IPhone(model='iphone15', color='Blue', disc=128)
iphone_16 = IPhone(model='iphone16', color='Blue', disc=128)
galaxy_24 = Samsung(model='g24', color='Grey', disc=128)
n1100 = Nokia(model='n1100', color='Grey', disc=4)

# n1100.send_sms(text='From nokia', number=38099)
# galaxy_24.send_sms(text='From Samsung ', number=38099)

iphone_15.download_from_appstore('iMessage')
iphone_15.send_sms(text='From iPhone ', number=38099)
iphone_16.send_sms(text='From iPhone ', number=38099)
print(n1100.disc)