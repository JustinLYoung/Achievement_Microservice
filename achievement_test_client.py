import zmq
import json

def send_metric(metric, amount):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5556")

    # send a request
    request = {"metric": metric, "amount": amount}
    socket.send_json(request)

    # receive reply
    response = socket.recv_json()
    message = response["message"]
    print(f"Sent: {request}, Received: {message}")

    socket.close()
    context.term()

if __name__ == "__main__":
    #Test examples - run program several times
    send_metric("login", 1)
    send_metric("entered goal", 1)
    send_metric("new PR", 1)
