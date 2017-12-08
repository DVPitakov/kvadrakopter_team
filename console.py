import websocket
import thread
import time


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    print ('REEEEEEAAAAAAAAAAAD')
    def run(*args):
        while True:
		s = ""
		fin_s = open('fifo', 'r')
		s = fin_s.read()
		fin_s.close()
		print("PRINT = ", s)
		time.sleep(0.2)
		ws.send(s)
        time.sleep(0.2)
        ws.close()
        print("thread terminating...")

    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://node-ws-server-neuro.eu-gb.mybluemix.net/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
