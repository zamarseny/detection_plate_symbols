import numpy as np
import copy 
import cv2

def get_boxes_texts(ann):
    """
    parse anns
    """
    boxes =[]
    texts = []
    for line in ann:
        rec_text, x1, y1, x2, y2 = line.split(' ')
        x1, y1, x2, y2 = map(float, [x1, y1, x2, y2])
        x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
        box = [x1, y1, x2, y2]
        boxes.append(box)
        texts.append(rec_text)
    return boxes, texts

def get_boxes_classes_xml(ann_tree):
    """
    parse anns
    """
    ann_len =  len([elem for elem in ann_root.iter() if elem.tag == 'name'])       
    boxes =np.zeros((ann_len, 4))
    #classes = np.zeros(ann_len)
    classes = []
    N = 0
    for elem in ann_root.iter():
        if elem.tag == 'name':
            #print(elem.tag, elem.text)
            #classes[N]= int(elem.text)
            classes.append(elem.text)
            N+=1
    #print(child.tag, child.attrib)
    #if child.tag=='object':
    #    for attr in child:
    #        print(attr.tag, attr.attrib)
    
    """
    for num, line in enumerate(ann):
        rec_text, x1, y1, x2, y2 = line.split(' ')
        x1, y1, x2, y2 = map(float, [x1, y1, x2, y2])
        #x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
        box = [x1, y1, x2, y2]
        #boxes.append(box)
        #print(boxes)
        boxes[num] = box
        
        classes.append(rec_text)
    """
    return boxes, classes
    
def plot_all_boxes(pic, boxes, classes):
    synth_pic_cp = pic.copy()
    h, w = synth_pic_cp.shape[:2]
    boxes = (boxes*np.array([w,h,w,h])).astype(np.int16)
    #print(boxes)
    for box, cl in zip(boxes, classes):
        x1, y1, x2, y2 = box
        l = int((y1+y2)/2)
        #print(line_num, text, box)
        rand_color = np.random.uniform(0,255, size=(3,)).tolist()
        synth_pic_cp = cv2.rectangle(synth_pic_cp, box[:2], box[2:], rand_color, 2)
        #synth_pic_cp = cv2.putText(synth_pic_cp, str(line_num), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX ,  \
        #               0.5, rand_color, 1, cv2.LINE_AA)
        #synth_pic_cp = cv2.line(synth_pic_cp, (0, l), (w, l), rand_color)
    return synth_pic_cp
    
    
def get_boxes_classes_txt(ann):
    """
    parse anns
    """
    #boxes =[]
    boxes =np.zeros((len(ann), 4))
    classes = np.zeros(len(ann))
    for num, line in enumerate(ann):
        #cl, x1, y1, x2, y2 = line.split(' ')
        #x1, y1, x2, y2 = map(float, [x1, y1, x2, y2])
        
        cl, x, y, w, h = line.split(' ')
        x, y, w, h =map(float, [x, y, w, h ])
        x1 = x- w/2
        x2 = x+w/2
        y1 = y-h/2
        y2 = y+h/2
        """
        cl, x1, y1, w, h = line.split(' ')
        x1, y1, w, h =map(float, [x1, y1, w, h ])
        x2 = x1 + w
        y2 = y1 + h
        """
        #x1, y1, x2, y2 = map(float, [x1, y1, x2, y2])
        box = [x1, y1, x2, y2]
        boxes[num] = box
        
        classes[num] = cl
    
    return boxes, classes
    
