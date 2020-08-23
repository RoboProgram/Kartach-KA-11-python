import serial
import time
import io




def send_KA11(s,str_command):
    s.write(f"{str_command}\r\n".encode())
    x=""
    out = ""
    while x != b'\n':
        x = s.read()
        out += x.decode()
    print(out)
    time.sleep(1)
    return out



def read_Card(s):
    for i in range(0,10):
        CC = "0"*(4-len(str(i)))
        C=f"{CC}{i}"
        base_string = f"<10000{C}01200000000000>"
        Card = send_KA11(s,base_string)
        # with open("TagData.txt","a+") as tgf:
        #     tgf.write(Card)
        print(Card)

def read_tag_file(s):
    for line in open("TagData.txt"):
        address = line[6:10]
        tag = line[14:24]
        # <10000063701190006119354>
        write_cmd = f"<10000{address}0119{tag}>"
        send_KA11(s,write_cmd)


        
        
        


if __name__ == "__main__":
    # Open grbl serial port
    s = serial.Serial('COM7',9600)
    sio = io.TextIOWrapper(io.BufferedRWPair(s, s))
    sio.write("\r\n\r\n")
    time.sleep(2)   # Wait for grbl to initialize 
    s.flushInput()  # Flush
    # <10000000010120000000000>
    # send_KA11(s,"<00000000001240006119354>")
    # send_KA11(s,"<10000000010130000000001>") # Mode 1
    # send_KA11(s,"<10000000011050000000000>") # remove Main
    # send_KA11(s,"<10000000011070000000000>") # remove Master
    # send_KA11(s,"<10000000010120000000000>") # Clear all user
    # read_Card(s)
    read_tag_file(s)
    s.close()



# w.close()
#startup (text) in serial (input)

# # Stream g-code to grbl
# for line in f:
#     l = line.strip() # Strip all EOL characters for consistency
#     print ('Sending: ' + l,)
#     s.write((l + '\n').encode()) # Send g-code block to grbl
#     grbl_out = s.readline() # Wait for grbl response with carriage return
#     print (' : ' + grbl_out.decode())
#     if '?' in l:
#         grbl_out = s.readline()
#         print(grbl_out.decode())
#     if 'G38.2' in l:
#         w.write(grbl_out.decode())
#         grbl_out = s.readline()
#         print(grbl_out.decode())
# # Wait here until grbl is finished to close serial port and file.
# #raw_input("  Press <Enter> to exit and disable grbl.")
# print("  Press <Enter> to exit and disable grbl.") 

# # Close file and serial port
