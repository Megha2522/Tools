from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
import heapq , os

class binaryTree:

    def __init__(self,value,freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self,other):
        return self.freq < other.freq

    def __eq__(self,other):
        return self.freq == other.freq

class HuffmanAlgorithm:

    def __init__(self):
        self.heap = []
        self.code = {} #dict to store binary code of char
        self.reverse_code = {} #dict to store binary code of char in reverse form

    def count_freq(self,text):
        freq_count = {}
        for char in text:
            if char not in freq_count:
                freq_count[char] = 0
            freq_count[char] += 1
        return freq_count

    def build_heap(self,freq_dict):
        for key, value in freq_dict.items():
            frequency = value
            binary_tree_node = binaryTree(key,frequency)
            heapq.heappush(self.heap , binary_tree_node)

    def build_BTree(self):
        while len(self.heap) > 1:
            bTree_node1 = heapq.heappop(self.heap)
            bTree_node2 = heapq.heappop(self.heap)

            # sum freq of both nodes and push back to heap
            sum_n12 = bTree_node1.freq + bTree_node2.freq
            newNode = binaryTree(None,sum_n12)
            newNode.left = bTree_node1
            newNode.right = bTree_node2
            heapq.heappush(self.heap , newNode)
        return

    def build_BTree_code_helper(self,root,curr_bits):
        if root is None:
            return
        if root.value is not None:
            self.code[root.value] = curr_bits
            self.reverse_code[curr_bits] = root.value
            return
        self.build_BTree_code_helper(root.left , curr_bits + '0')
        self.build_BTree_code_helper(root.right , curr_bits + '1')

    def build_BTree_code(self):
        root = heapq.heappop(self.heap)
        self.build_BTree_code_helper(root,'')
    
    def build_encoded_text(self,text):
        encoded_text = ""
        for char in text:
            encoded_text += self.code[char]
        return encoded_text

    def build_padded_text(self , encoded_text):
        padding_value = 8 - len(encoded_text) % 8
        for i in range(padding_value):
            encoded_text += '0'

        padded_info = "{0:08b}".format(padding_value)
        padded_text = padded_info + encoded_text
        return padded_text
    def build_byte_arr(self,padded_text):
        array = []
        for i in range(0,len(padded_text),8):
            byte = padded_text[i:i+8]
            array.append(int(byte,2))
        return array
    
    def get_file_size(self, filePath):
        file_size = os.path.getsize(filePath)
        if file_size < 1024:
            return f"{file_size} bytes"
        elif file_size < 1024**2:
            return f"{file_size / 1024:.2f} KB"
        elif file_size < 1024**3:
            return f"{file_size / 1024**2:.2f} MB"
        else:
            return f"{file_size / 1024**3:.2f} GB"

    def compression(self, path):
 
        fileSize = self.get_file_size(path)
        print('Reading file ' + path + ' with file size: ', fileSize)
        # To access the file and get text of the file
        filename,file_extension = os.path.splitext(path)
        output_path = filename + '.bin'

        with open(path , 'r+') as file , open(output_path,'wb') as output:

            text = file.read()
            text = text.rstrip()

            print('Starting compression...')
 
            # Count frequency of each char in text
            freq_dict = self.count_freq(text)

            # Create min heap to extract 2 min freq 
            min_heap = self.build_heap(freq_dict)

            # Create binary Tree from heap
            self.build_BTree()

            # Construct code [left->0 , right->1] and store in dict
            self.build_BTree_code()

            # Build encoded text
            encoded_text = self.build_encoded_text(text)
            padded_text = self.build_padded_text(encoded_text)

            # Return binary file as output
            bytes_arr = self.build_byte_arr(padded_text)
            final_bytes = bytes(bytes_arr)
            output.write(final_bytes)
        print('Compressed Successfully')
        return output_path

    def remove_padding(self , text):
        padded_info = text[:8]
        padding_value = int(padded_info,2)
        text = text[8:]
        text = text[:-1*padding_value]
        return text
    
    def decoded_text(self , text):
        current_bits = ''
        decoded_txt = ''
        for char in text:
            current_bits += char
            if current_bits in self.reverse_code:
                decoded_txt += self.reverse_code[current_bits]
                current_bits = ''
        return decoded_txt

    def decompress(self , input_path):
        filename,file_extension = os.path.splitext(input_path)
        output_path = filename +'_decompressed'+  '.txt'

        with open(input_path , 'rb') as file , open(output_path,'w') as output:
            bits_string = ''
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8,'0')
                bits_string += bits
                byte = file.read(1)
            text_after_removing_padding = self.remove_padding(bits_string)
            actual_text = self.decoded_text(text_after_removing_padding)
            output.write(actual_text)
        return output_path
    
# path = '.\input.txt' #input("Enter the path of file : ")
# h = HuffmanAlgorithm(path)
# compressesd_file = h.compression()
# h.decompress(compressesd_file)

# making main window
window = Tk() 
window.title("HuffMan Compression/De-Compression")
window.config(background="teal")

# widgets
topFrame=Frame(window)
topFrame.pack()
bottomFrame=Frame(window)
bottomFrame.pack()
heading=Label(topFrame,text="HUFFMAN", background="black",foreground="white",font=("Arial Bold", 50))
heading.pack(fill=X)

COMPRESSION = "Compression"
DE_COMPRESSION = "DeCompression"

operationSelector = Combobox(bottomFrame,width=25,font=("Arial Bold", 15))
operationSelector['values']= ("Select a Property...", COMPRESSION, DE_COMPRESSION)
operationSelector.current(0) #set default property to first element in list of values 
operationSelector.grid(column=6, row=1,columnspan=5,pady=10)

def open_file():
    file_path = filedialog.askopenfilename(title="Select a file")  # Opens the file selection dialog
    selectedOperation = operationSelector.get()
    if file_path:
        print(f"Selected file: {file_path}")
        print(f"Selected operation: {selectedOperation}")
        huffmanAlgorithm = HuffmanAlgorithm()
        if selectedOperation == COMPRESSION:
            huffmanAlgorithm.compression(file_path)
        elif selectedOperation == DE_COMPRESSION:
            huffmanAlgorithm.decompress(file_path)
        else:
            messagebox.showerror("Error", f"Please select operation from dropdown!")
            return
        # Show dialog box, compression/Decompression completed & close the main window
        messagebox.showinfo("Information", f"{selectedOperation} successful!s")
        exit()

convert_button=Button(bottomFrame,text="Select File",command=open_file,width=23)
convert_button.grid(column=6, row=4,columnspan=5,pady=10)

# mainloop
window.mainloop()

