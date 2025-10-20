import time
import pynput

mouse = pynput.mouse.Controller()
stop_script = False


def on_press(key):
    global stop_script

    try:
        if key.char == 'q':
            stop_script = True
            return False
    except AttributeError:
        if key == pynput.keyboard.Key.esc:
            stop_script = True
            return False


def start_auto_click(interval, frequency):
    global stop_script

    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()

    print(f"Auto-clicker started. Clicking {frequency} times every {interval} second(s). Press CTRL+C or q to stop.")

    try:
        while not stop_script:
            mouse.click(pynput.mouse.Button.left, frequency)

            print(f"[+] Clicked {frequency} times after {interval} seconds.")

            time.sleep(interval)
    except KeyboardInterrupt:   
        pass

    print("[-] Killed.")



if __name__ == "__main__":
    interval = float(input("Enter click interval: "))
    frequency = int(input("Enter click frequency: "))

    start_auto_click(interval, frequency)
