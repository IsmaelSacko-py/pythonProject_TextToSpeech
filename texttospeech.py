import customtkinter as ctk
from PIL import Image
# import gtts
import pyttsx3
# from pygame import mixer, time


# root = ctk.CTk()
tts = pyttsx3.init()


# gtts = gtts.gTTS(text="Vous n'avez saisi aucun text", lang="fr")
# mixer.init()


class TextToSpeech():

    foreground_color = "#333333"
    label_text_color = "#ffffff"
    input_text_color = "#ffffff"

    def __init__(self, gui):
        
        self.gui = gui

        self.gui.configure(fg_color = self.foreground_color)


        self.main_div = ctk.CTkFrame(self.gui, fg_color = self.foreground_color)
        self.center_div = ctk.CTkFrame(self.main_div, fg_color=self.foreground_color, bg_color="transparent", width=700)
        self.top_div = ctk.CTkFrame(self.main_div, fg_color = self.foreground_color, width=700, height=100)
        self.logo_div = ctk.CTkFrame(self.top_div, fg_color=self.foreground_color, width=0)
        self.top_div.pack_propagate(False)
        self.center_div.pack_propagate(False)
        # self.logo_div.pack_propagate(False)
        self.scan_div = ctk.CTkFrame(self.center_div, fg_color=self.foreground_color)
        self.action_div = ctk.CTkFrame(self.center_div, fg_color=self.foreground_color )
        self.select_div = ctk.CTkFrame(self.action_div, fg_color=self.foreground_color)
        self.btn_div = ctk.CTkFrame(self.action_div, fg_color=self.foreground_color)
        
        self.speach_image = ctk.CTkImage(Image.open("Images/speak.png"), size = (40, 40))
        self.save_image = ctk.CTkImage(Image.open("Images/save.png"), size=(25,40))
        self.logo = ctk.CTkImage(Image.open("Images/TTS_BG.png"), size = (110, 110))
        self.inputText = ctk.CTkTextbox(self.scan_div, width=400, height=200, font=('Arial', 16),border_width=1, border_color="white", fg_color="black", text_color=self.input_text_color)

        self.label_voice = ctk.CTkLabel(self.select_div, text='VOICE', font=('Arial',15, 'bold'), text_color = self.label_text_color)
        self.label_speed = ctk.CTkLabel(self.select_div, text="SPEED", font=('Arial',15, 'bold'), text_color = self.label_text_color)
        self.label_logo = ctk.CTkLabel(self.logo_div, image = self.logo, text="")
        self.label_logo_text = ctk.CTkLabel(self.logo_div, text_color = "white", text='text to speech'.upper(), font=('Arial', 24, 'bold'))

        self.select_voice = ctk.CTkComboBox(self.select_div, button_color='gray', fg_color="black", text_color=self.input_text_color, values=['Male', 'Female'], state = 'readonly', width=100, font=('Arial',12, 'bold'))
        self.select_speed = ctk.CTkComboBox(self.select_div, button_color='gray', fg_color="black", text_color=self.input_text_color, values = ['Fast','Normal', 'Slow'], state = 'readonly', width=100, font=('Arial',12, 'bold'))
        self.play_btn = ctk.CTkButton(self.btn_div, image=self.speach_image, text='Speak', width=100, height=50, font=('Arial',14, 'bold'), command = self.readText)
        self.save_btn = ctk.CTkButton(self.btn_div, image = self.save_image, text='Save', fg_color = '#339933', hover_color = "#006600", width=100, height=50, font=('Arial',14, 'bold'), command = self.saveText)
        self.switch = ctk.CTkSwitch(self.top_div, text="Light Mode", text_color = 'white', fg_color = 'white', font=("Arial", 14), bg_color = self.foreground_color, command=self.change_gui_apparance)

        
        self.main_div.pack()
        self.top_div.pack(pady = (0, 40), padx=20)
        self.center_div.pack()
        self.logo_div.pack(side="left")
        self.scan_div.grid(row=0, column=0)
        self.action_div.grid(row=0, column=1, padx=(20, 0))
        self.select_div.grid()
        self.btn_div.grid(pady=(40, 0))
        self.switch.pack(side='right')

        self.inputText.grid()

        self.label_voice.grid(row=0, column=0)
        self.label_speed.grid(row=0, column=1, padx=(40, 0))
        self.label_logo.grid(row=0, column=0, padx=(0, 20))
        self.label_logo_text.grid(row=0, column=1)

        self.select_voice.grid(row=1, column=0)
        self.select_speed.grid(row=1, column=1, padx=(40, 0))

        self.play_btn.grid(row=2, column=0)
        self.save_btn.grid(row=2, column=1, padx=(40, 0))

        self.choice_speed = tts.getProperty('rate')
        self.current_voice = tts.getProperty("voices")

        self.select_speed.set(self.select_speed.cget('values')[1])
        self.select_voice.set(self.select_voice.cget("values")[1])


    

    def Events(self, event):
        print(event)
        if event.keysym == "Return":
            print("Hello")


    def readText(self):
        texte = self.inputText.get("1.0", "end-1c") if self.inputText.get("1.0", "end-1c") else "Vous n'avez saisi aucun texte"

        match self.select_speed.get():
            case "Fast":
                tts.setProperty('rate', self.choice_speed*2)
            case "Normal":
                tts.setProperty('rate', self.choice_speed)
            case "Slow":
                tts.setProperty('rate', self.choice_speed//2)
            case _:
                tts.say("Vitesse non prise en compte")

        #tts.setProperty('voice', self.current_voice[0].id if self.select_voice.get() == "Male" else self.current_voice[1].id)

        tts.say(texte)
        tts.runAndWait()

    def change_gui_apparance(self):
        foregroundColor = "#d7d3d3" if self.switch.get() == 1 else self.foreground_color
        textColor = "black" if self.switch.get() == 1 else "white"
        other_foreground = "white" if self.switch.get() == 1 else "black"
        # background_color = 
        # self.gui._set_appearance_mode('light')
        self.top_div.configure(fg_color=foregroundColor)
        self.logo_div.configure(fg_color=foregroundColor)
        self.main_div.configure(fg_color=foregroundColor)
        self.switch.configure(bg_color=foregroundColor, fg_color = textColor)
        self.gui.configure(fg_color=foregroundColor)                            
        # self.switch.configure(bg_color=foregroundColor, text_color = '#d7d3d3')
        self.center_div.configure(fg_color =foregroundColor)
        self.action_div.configure(fg_color = foregroundColor)
        self.select_div.configure(fg_color = foregroundColor)
        self.btn_div.configure(fg_color = foregroundColor)
        self.inputText.configure(fg_color = other_foreground, bg_color = foregroundColor, border_width = 1, border_color = textColor, text_color = textColor)
        self.label_speed.configure(text_color = textColor)
        self.label_voice.configure(text_color=textColor)
        self.label_logo_text.configure(text_color=textColor)
        self.select_speed.configure(fg_color = other_foreground, text_color = textColor)
        self.select_voice.configure(fg_color = other_foreground, text_color = textColor)


    def saveText(self):
        if self.inputText.get("1.0", "end-1c"):
            print("ok")
            tts.save_to_file(self.inputText.get("1.0", "end-1c"), "textToSpeach.mp3")
            tts.runAndWait()
        else:
            tts.say("Impossible de sauvegarder le texte")
            tts.runAndWait()
