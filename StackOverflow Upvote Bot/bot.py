import pyautogui as gui
import time

screenWidth, screenHeight = gui.size()
file = open("links.ykv")
file = file.readlines();

# 223,51
for x in file:
	link = "https://stackoverflow.com/";
	gui.moveTo(223,51)
	time.sleep(0.2)
	gui.click()
	time.sleep(0.2)
	gui.typewrite(link + x)
	time.sleep(4)

	gui.moveTo(167,247)
	time.sleep(0.2)
	gui.click()
	time.sleep(1)
	
print(gui.position());

#js code
# a="";
# $(".question-hyperlink").each(function(){
#    var link=$(this).attr("href");
#    a += link + "||";
# });
# a