import json
import random
from data import nodes

N = len(nodes)
ACKNOWLEDGED = "ACKNOWLEDGED"
LIST_USERS = "LIST_USERS"
SEND_FAIL = "SEND_FAIL"
def prep_trajectory(message, target, sender):
    """ takes trajectory list (use prep_trajectory) and string message

    returns trajectory and message as nested list in JSON string form
    """
    trajectory = list(nodes.keys())
    random.shuffle(trajectory)

    lista = [target, [message]] #OSTATNI MUSI ZAWIERAĆ NAZWĘ UŻYTKOWNIKA
    for node in trajectory:
        lista = [node, lista]
    target, lista = lista
    return target, json.dumps(lista)

def send(sock, string_message, ip_port):
    bytes_message = bytes(string_message, encoding='utf-8')
    sock.sendto(bytes_message, ip_port)

def receive(sock):
    data, origin_ip = sock.recvfrom(1000)
    received_string= str(data, 'utf-8')
    return received_string, origin_ip
