import zmq
import json

#Enter your threshold parameters here for goals you want.
thresholds = {
    "login": 5,
    "entered goal": 1,
    "new PR": 1,
}

streak = {}


def update_streak(metric, amount):
    """Function to increase the current streak for the achievement threshold"""
    key = metric
    streak[key] = streak.get(key, 0) + amount

    if metric not in thresholds:
        return {"award": False, "message": "Achievement has no metric."}

    if streak[key] >= thresholds.get(metric):
        streak[key] = 0
        return {"award": True, "message": f"Reward unlocked: {thresholds[metric]} {metric}!"}
    
    return {"award": False, "message": "No award, keep trying"}

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5558")

    print("Achievement Microservice running on tcp://*:5558")

    while True:
        message = socket.recv_json()

        metric = message["metric"]
        amount = message["amount"]

        response = update_streak(metric, amount)
        socket.send_json(response)


if __name__ == "__main__":
    main()
