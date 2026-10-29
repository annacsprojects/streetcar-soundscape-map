# Creating the main window and setting its title and size
import tkinter as tk
from data.quotes import streetcar_data
from pygame import mixer
mixer.init()
print(tk.TkVersion)

app = tk.Tk()
app.title("A Streetcar Named Desire: Domestic Space and Sound Presentation Map")
app.geometry("1100x650")
app.resizable(False, False)

control_panel = tk.Frame(app, bg="#1a1a24", width=250, height=650)
control_panel.pack_propagate(False)
control_panel.place(x=0, y=0)

floorplan_panel = tk.Frame(app, bg="#09090b", width=450, height=650)
floorplan_panel.pack_propagate(False)
floorplan_panel.place(x=250, y=0)

analysis_panel = tk.Frame(app, bg="#1a1a24", width=400, height=650)
analysis_panel.pack_propagate(False)
analysis_panel.place(x=700, y=0)

kitchen_frame = tk.Frame(floorplan_panel, bg="#11111a", highlightbackground="#3f3f46", highlightthickness=2)
kitchen_frame.pack_propagate(False)
kitchen_frame.place(relx=0.05, rely=0.15, relwidth=0.42, relheight=0.6)

kitchen_label = tk.Label(kitchen_frame, text="🍳 KITCHEN &\n 🛋️LIVING AREA", bg="#11111a", fg="white", font=("Arial", 10, "bold"))
kitchen_label.pack(pady=20)

bedroom_frame = tk.Frame(floorplan_panel, bg="#181826", highlightbackground="#3f3f46", highlightthickness=2)
bedroom_frame.pack_propagate(False)
bedroom_frame.place(relx=0.53, rely=0.15, relwidth=0.42, relheight=0.6)

bedroom_label = tk.Label(bedroom_frame, text="🛌 BEDROOM SANCTUARY", bg="#181826", fg="white", font=("Arial", 10, "bold"))
bedroom_label.pack(pady=20)

control_title = tk.Label(control_panel, text="🔊 SOUND CUES", bg="#1a1a24", fg="white", font=("Arial", 11, "bold"))
control_title.pack(pady=20)

piano_btn = tk.Button(control_panel, text="🎹 Opening Blue Piano", font=("Arial", 10, "bold"), fg="#1a1a24")
piano_btn.pack(pady=10, padx=20, fill='x')

crescendo_btn = tk.Button(control_panel, text="⚡️ Piano Crescendo", font=("Arial", 10, "bold"), fg="#1a1a24")
crescendo_btn.pack(pady=10, padx=20, fill='x')

polka_btn = tk.Button(control_panel, text="👻 Ghostly Polka", font=("Arial", 10, "bold"), fg="#1a1a24")
polka_btn.pack(pady=10, padx=20, fill='x')

poker_btn = tk.Button(control_panel, text="🥊 Sound of the Brutes", font=("Arial", 10, "bold"), fg="#1a1a24")
poker_btn.pack(pady=10, padx=20, fill='x')

analysis_title = tk.Label(analysis_panel, text="👀ANALYSIS", bg="#1a1a24", fg="white", font=("Arial", 11, "bold"))
analysis_title.pack(pady=20)

quote_box = tk.Label(analysis_panel, text="💬 Quote -> Select a sound cue to display text.", bg="#1a1a24", fg="#d4d4d8", font=("Arial", 11, "italic"), wraplength=360, justify="left")
quote_box.pack(pady=10, padx=20, fill="both")

context_box = tk.Label(analysis_panel, text="📜 Context -> Selection will reveal the history and setting of the era.", bg="#1a1a24", fg="#a1a1aa", font=("Arial", 10), justify="left", wraplength=360)
context_box.pack(pady=10, padx=20, fill="both")

analysis_box = tk.Label(analysis_panel, text="🔬 Analysis -> Selection will reveal the breakdown of the domestic space and sound.", bg="#1a1a24", fg="#d4d4d8", font=("Arial", 10), justify="left", wraplength=360)
analysis_box.pack(pady=20, padx=20, fill="both")

subtitle_box = tk.Label(analysis_panel, text="🗝️ Subtitle -> Selection will reveal the purpose of the map's spatial colour choices in relation to sound.", bg="#1a1a24", fg="#93c5fd", font=("Arial", 10), justify="left", wraplength=360)
subtitle_box.pack(pady=10, padx=20, fill="both")

def trigger_sound(cue_key):
    data = streetcar_data[cue_key]
    context_box.config(text=data["context"])
    analysis_box.config(text=data["analysis"])
    quote_box.config(text=data["quote"])
    subtitle_box.config(text=data["subtitle"])

    mixer.stop()

    mixer.music.load(data["music_file"])
    mixer.music.play()

    chatter_path = data.get("chatter_file")
    print("chatter_path:", chatter_path)
    if chatter_path:
        chatter = mixer.Sound(chatter_path)
        chatter.set_volume(0.5)
        chatter.play(loops=-1)
        print("chatter playing, length in seconds :", chatter.get_length())

    if cue_key == "blue_piano":
        kitchen_frame.config(bg=data["colour"], highlightthickness=0)
        bedroom_frame.config(bg="#181826", highlightthickness=0)
    elif cue_key == "piano_crescendo":
        kitchen_frame.config(bg="#1d4ed8", highlightthickness=2)
        bedroom_frame.config(bg="#1d4ed8")
    elif cue_key == "polka_start":
        kitchen_frame.config(bg="#11111a", highlightthickness=0)
        bedroom_frame.config(bg=data["colour"], highlightbackground="#a1a1aa", highlightthickness=2)
    else:
        kitchen_frame.config(bg=data["colour"], highlightthickness=0)
        bedroom_frame.config(bg=data["colour"], highlightthickness=0)

piano_btn.config(command=lambda: trigger_sound("blue_piano"))
crescendo_btn.config(command=lambda: trigger_sound("piano_crescendo"))
polka_btn.config(command=lambda: trigger_sound("polka_start"))
poker_btn.config(command=lambda: trigger_sound("poker_climax"))

footer = tk.Label(
    app,
    text="Interactive Soundscape Exihibit | Designed for a Streetcar Named Desire", 
    font=("Arial", 8, "italic"), 
    fg="#3f3f46",
    bg="white"
)
footer.place(relx=0.5, rely=0.97, anchor="center")

app.mainloop()