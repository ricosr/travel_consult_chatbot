# -*- coding: utf-8 -*-

import gevent
import zmq.green as zmq

from route_control import Consult

agent = Consult()
context = zmq.Context()


def server():
    print("start listening ......")
    socket = context.socket(zmq.REP)
    socket.setsockopt(zmq.LINGER, 5000)
    socket.bind('tcp://127.0.0.1:10086')
    while True:
        recv_msg = socket.recv()
        recv_msg = str(recv_msg, encoding="utf-8")
        msg, user_id = recv_msg.split("@---@")
        reply = agent.get_answer(msg, user_id)
        # print("server:{}".format(reply))
        socket.send_string(reply)

publisher = gevent.spawn(server)
gevent.joinall([publisher])