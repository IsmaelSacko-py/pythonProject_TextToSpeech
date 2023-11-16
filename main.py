from texttospeech import *
# , root_size = "700x400", root_title = "Text to speach",
#             root_apparance_mode = "Dark", root_resizable_width = False, root_resizable_height = False
gui = ctk.CTk()
gui.geometry('700x400')
gui.title("Text to speech")
# gui._set_appearance_mode('Dark')
gui.resizable(width = False, height = False)

test = TextToSpeech(gui)


gui.mainloop()



