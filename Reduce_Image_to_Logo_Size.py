import tinify
from tkinter import filedialog
from tkinter import *
import time


# Created by Matthew Taylor on 3/6/2018 using Tinify API client.


try:
    tinify.key = "YOUR_API_KEY"  # Go here to get your API key -> https://tinypng.com/developers
    tinify.validate()
    print("Tinify account validated :)")
except tinify.Error:
    print("Not a working number :(")
    pass


root = Tk()
root.withdraw()

root.open = filedialog.askopenfilename(initialdir="c:/Users/%s'/Downloads % user",
                                       title="Select file to resize", defaultextension=".jpg",
                                       filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
root.save = filedialog.asksaveasfilename(initialdir="c:/Users/%s'/Downloads % user",
                                         title="Save re-sized file as", defaultextension=".jpg",
                                         filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))

try:
    # Using the Tinify API client.
    source = tinify.from_file(root.open)
    copyrighted = source.preserve("copyright", "creation")
    print(root.open)
    resized = copyrighted.resize(
        method="fit",
        width=250,
        height=60
    )
    resized.to_file(root.save)
    print(root.save)
    pass
except tinify.AccountError as e:
    print("The error message is: %s" % e.message)
    # Verify your API key and account limit.
except tinify.ClientError as e:
    print("The error message is: %s" % e.message)
    # Check your source image and request options.
    pass
except tinify.ServerError as e:
    print("The error message is: %s" % e.message)
    # Temporary issue with the Tinify API.
    pass
except tinify.ConnectionError as e:
    print("The error message is: %s" % e.message)
    # A network connection error occurred.
    pass
except Exception as e:
    print("The error message is: %s" % e.message)
    # Something else went wrong, unrelated to the Tinify API.
    pass

a = 500
int(a)
b = tinify.compression_count
int(b)
c = (a - b)
str(c)
print("{} and {}".format(c, "image size reductions left this month."))
time.sleep(10)

