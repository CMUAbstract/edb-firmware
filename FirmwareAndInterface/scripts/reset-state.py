import wispmon

mon = wispmon.WispMonitor()

def main():
    
    mon.sendCmd(wispmon.USB_CMD_RESET_STATE)
    mon.destroy()

if __name__ == '__main__':
    main()