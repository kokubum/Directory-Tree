import os
from PIL import Image,ImageDraw,ImageFont
IDENTATION = 5


def tree_generator(dir_path,limit_level,idt = IDENTATION): 
    height = 1 

    test_file = open('tree.txt','w')
    for root,directories,files in os.walk(dir_path):
        level = root.replace(dir_path,'').count(os.sep)
        if limit_level and level>=limit_level:
            continue

        height+=len(directories)+len(files)

        new_identation =  level * idt
        space,line = (0,0) if level == 0 else ((new_identation-idt),5)

        line_root = ' '*space+ '|'+'─'*line
        test_file.write('{}{}\n'.format(line_root,os.path.basename(root)))
        line_file = ' '*new_identation +'|'+ '─'*idt
        if level == (limit_level-1):         
            for name_dir in directories:
                test_file.write('{}{}\n'.format(line_file,name_dir))
        
        for f in files:
            test_file.write('{}{}\n'.format(line_file,f))

    test_file.close()

    return height

def create_image(height,option):
    if option == 'yes':
        img = Image.new('RGB',(1920,23*height + 20),color=(255,255,255))
        fnt = ImageFont.truetype('DejaVuSans.ttf',20)
        draw = ImageDraw.Draw(img)
        
        with open('tree.txt','r') as f:
            draw.text((10,10), f.read(),font=fnt, fill=(0,0,0))
            img.save('tree.png')
    

def run():
    print('Enter the path of the folder: ',end='')
    path = input()
    print('\nTree depth level\n0: All the tree\n1: Only the directory of the path\n2: The directory and all his sub-directories\n...\n')
    print('Enter the chosen level: ',end='')
    level = int(input())
    height = tree_generator(path,limit_level=level)
    print('\nCreate an image of the tree (yes | no): ',end='')
    option = input()
    create_image(height,option)
    print('\nEnd of the program')



if __name__ == '__main__':
    run()


