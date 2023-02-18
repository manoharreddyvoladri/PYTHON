import os
def main():
    i=0
    path = #input of the path where you want to change
    for filename in os.listdir(path):
        my = "img"+ str(i) + ".jpg"
        source =path+filename
        my =path +my 
        os.rename(source, my)
        i+=1
        if __name__ == '__main__':
        main()
