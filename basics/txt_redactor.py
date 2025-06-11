

def get_file(path:str , read=0):

    #try open the file 
    try:
        file = open(path)
    except:
        print("Invalid File Name...\n Exiting to menu")
    
    if(read==1):
        print("PEEK  OF FILE")
        line = 1
        while (line<=5):            
            for i in file:
                print(f'-[{line}]{i}')
                line+=1
                print("\tEND OF FILE")




while(driver ==1 ):
    #menu
    print('exit - q')
    print('**SPL chars are not supported**')
    print('Enter the filename with file extension')
    op = str(input('Type here :')).lower() 
    
driver = 1

