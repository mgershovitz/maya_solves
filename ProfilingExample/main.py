from time import sleep
from viztracer import VizTracer


def create_list():
    return [1] * 10000000


def remove_from_start(li):
    li.pop(0)


def remove_from_end(li):
    li.pop(len(li) - 1)


def delete_list(my_list):
    while len(my_list) > 0:
        remove_from_start(my_list)
        remove_from_end(my_list)


if __name__ == '__main__':
    tracer = VizTracer()
    tracer.start()
    my_list = create_list()
    delete_list(my_list)
    tracer.stop()
    tracer.save("profile.json")
