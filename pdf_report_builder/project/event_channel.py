from pdf_report_builder.utils.singleton import Singleton

class EventChannel(metaclass=Singleton):

    def __init__(self):
        self.subscribers = {}

    def unsubscribe(self, event, callback):
        if event is not None or event != ""\
                and event in self.subscribers.keys():
            self.subscribers[event] = list(
                filter(
                    lambda x: not x == callback,
                    self.subscribers[event]
                )
            )

    def subscribe(self, event, callback):
        if not callable(callback):
            raise ValueError("callback must be callable")

        if event is None or event == "":
            raise ValueError("Event cant be empty")

        if event not in self.subscribers.keys():
            self.subscribers[event] = [callback]
        else:
            self.subscribers[event].append(callback)

    def publish(self, event: str, *args):
        if event in self.subscribers.keys():
            for callback in self.subscribers[event]:
                if not args:
                    callback()
                else:
                    callback(args)
