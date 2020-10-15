import sys
import os

class Event(object):
    def __init__(self):
        self.sender_id = ""
        self.event_type = ""

        #type = new_conneciton
        self.client_socket = None
        self.client_ip_port = None

        self.is_running = 0


class Manager(object):
    def __init__(self):
        self.manager_thread = None
        self.semaphore = threading.Semaphore(0)

        self.event_pool = []
        self.MyThreadingQueue = None

    def manager_func(self):
        f = open(file_name, 'rb')

        while True:
            data = f.read(1024)
            if not data:
                break
            other_socket.send(data)
        f.close()

class Solution(object):
    def __init__(self):
        pass

    def solution(self, n, limit):
        cnt = 0
        if (n - limit) > 0 and (n - limit) % 2 == 0:
            cnt1 = self.solution((n - limit)/2, limit)
            cnt2 = self.solution((n - limit)/2 + limit, limit)
            cnt += cnt1
            cnt += cnt2
            return cnt
        else:
            return 1

    def solution_(self, n, limit):
        if n == 0:
            return 0
        elif n <= limit:
            return 1
        elif n > limit:
            return self.solution(n, limit)
        else:
            return 0


if __name__ == "__main__":
    try:
        in_line = sys.stdin.readline().strip()
        in_list = list(map(int, in_line.split()))
        n = in_list[0]
        limit = in_list[1]
    except Exception as e:
        pass
    else:
        S = Solution()
        print(S.solution_(n, limit))