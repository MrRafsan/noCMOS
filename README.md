# Description
I am not a profession python coder. I am still learning and I made it on my Kali Linux 21.2. So I can surely say that it will work on kali and similar kind of OS. In future I'll try to add some other feature and make it compatble with Windows, MacOS and other flavor of linux.
# NOTE!!!
You should have _Xfce4_ installed, working internet connection and root/sudo permission. **THIS IS NOT A PERMANENT FIX. YOU STILL NEED TO CHANGE THE CMOS BATTERY LATER**
# Setup
- `git clone https://github.com/MrRafsan/noCMOS.git`
- `pip3 install -r requirements.txt`
- `xfce4-session-settings`. It will open Session and Start-up Manager
![Session and Start-up Manager](https://blog.marcocadete.com/img/posts/xfce4-add-startup-app.jpg)
-  Now go to `Application Autostart` and press the plus icon on the down leftside corner. A "Add Application" window will pop up
-  You can name the appliction anything and Description is optional
-  in command box type `python3 <path_to_the_file>/noCMOS.py` and select trigger on "on login" press ok.
# What is CMOS
CMOS stands for **Complementary Metal Oxide Semiconductor**. The CMOS battery powers the BIOS firmware in your computer. BIOS needs to remain operational even when your computer isn't plugged into a power source. And because of CMOS battery the time of your computer never reset until the juice runs out.
