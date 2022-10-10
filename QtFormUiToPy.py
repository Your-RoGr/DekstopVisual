import os

def Main():

    for filename in os.listdir("QtForm"):
        try:
            print(filename)
            name = filename.split(".")

            if name[-1] == "ui":
                os.system(f"cd QtForm && pyuic5 {filename} -o {name[0]}.py")

        except:
            pass

if __name__ == "__main__":
    Main()