import pryzm as pz
red = pz.Pryzm(echo=True).red
red_on_blue = pz.Pryzm().red().BLUE

red("This is red text")                               # These two functions now print directly
red_on_blue("This is red text with blue background")

# great for quickly creating semantic printing to better read console output!
warning = pz.Pryzm(echo=True).yellow
info = pz.Pryzm(echo=True).cyan
error = pz.Pryzm(echo=True).red

error("Error: this text shows as red")
warning("Warning: pay attention, but really just an fyi")
info("Cyan is probably a little strong, maybe green would be better")
