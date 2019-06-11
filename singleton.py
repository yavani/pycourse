class Singleton:
    __instance = None
    @staticmethod
    def getInstance():
        """Static access method."""
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    def __init__(self):
        """Virtually Private constructor"""
        if Singleton.__instance!= None:
            raise Exception("This class is a singletone")
        else:
            Singleton.__instance = self

s = Singleton()
print(s)

s= Singleton.getInstance()
print(s)


s = Singleton.getInstance()
print(s)

a = Singleton()
print(a)
