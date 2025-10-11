##############################################################################
# Decree by NTNU/IBM/MB High Council on behalf of Lord Science               #
# Try running this python code, it actually works ;)                         #
##############################################################################
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

leaving_office = True
dishwasher_running = True
washed_manually = False  # simulate whether you actually washed manually

if leaving_office and dishwasher_running:
    print("⚠️  Dishwasher is still running!")
    print("Please use the brush and detergent to wash the dishes manually.")

    if washed_manually:
        print("""
😬 You didn’t wash the dishes manually:
as a result:
- The following image will be the first scene in the morning as work 
- Leftover food fermenting over Night or over the Whole Weekend
- Leftover food Dry up on the dish making them Harder to clean
- The first people in the morning / Monday have to empty the dishwasher and 
- touch the fermented remains before putting them in the dishwasher
😊 Remember to wash the dishes next time and 
make a fresh impression for the next morning'
""")

# 👇 Show an image of the consequences
img = mpimg.imread("./theOffice.jpeg")  # put your own file here
plt.imshow(img)
plt.axis("off")
plt.title("Monday Morning Surprise!")
plt.show()