class ResourceAllocator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.resources = 100

    def allocate(self, amount):
        if amount <= self.resources:
            self.resources -= amount
            print(f"Allocated {amount} resources")
        else:
            print("Insufficient resources")

    @staticmethod
    def total_resources():
        return 100

    @classmethod
    def remaining_resources(cls):
        return cls._instance.resources

if __name__ == "__main__":
    allocator = ResourceAllocator()
    allocator.allocate(20)
    print(ResourceAllocator.remaining_resources())
