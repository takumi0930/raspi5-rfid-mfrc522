import MFRC522
import time

running = True
block = 8 # read block
key = [0xFF]*6 # default key

rfid = MFRC522.MFRC522()

print("Please place your RFID card on the reader...")
print("Press Ctrl-C to stop.")

try:
    while running:
        (status, _) = rfid.MFRC522_Request(rfid.PICC_REQIDL)
        
        if status == rfid.MI_OK: 
            (status, uid) = rfid.MFRC522_SelectTagSN()
            
            if status == rfid.MI_OK:
                uid_str = ''.join(f"{i:02x}" for i in uid)
                
                status = rfid.MFRC522_Auth(rfid.PICC_AUTHENT1A, block, key, uid)
                
                if status == rfid.MI_OK:
                    _, data = rfid.MFRC522_Read(block)
                    
                    if data:
                        text = ''.join(chr(b) for b in data).rstrip('\x00')
                        print(f"uid:{uid_str}\ntext:{text}\n")
                    else:
                        print(f"uid:{uid_str}\ntext:(null)\n")
                    
                    rfid.MFRC522_StopCrypto1()
                    
                else:
                    print("Auth failed")
                    rfid.MFRC522_StopCrypto1()
        
        time.sleep(0.2)

except KeyboardInterrupt:
    print("program finish")